#!/usr/bin/env python3
"""
Scrapbox to Markdown Converter

Description:
A single Python script to convert Scrapbox JSON files to Markdown files

Features:
1. Read and parse JSON files
2. Convert Scrapbox notation to Markdown
3. Generate and save Markdown files
4. Preserve metadata (frontmatter format)

Conversion rules:
- [* text] → **text**
- [/ text] → *text*
- [link] → [link](link.md)
- [https://...png] → ![](https://...png)
- code:lang → ```lang
- > quote → > quote
- Tab indent → - list item

Usage:
    python convert_scrapbox.py archive/project.json -o docs/
    python convert_scrapbox.py archive/project.json --dry-run

Options:
    -o, --output: Output directory (default: .)
    --dry-run: Show what would be done without creating files
    -v, --verbose: Enable verbose output
"""

import json
import re
import os
import sys
import argparse
import difflib
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path


def parse_scrapbox_line(text, max_heading_level=3, page_titles=None, output_dir=None, dry_run=False, verbose=False):
    """Convert Scrapbox notation to Markdown
    
    Args:
        text: Line text to convert
        max_heading_level: Maximum asterisk count found in the document (for heading conversion)
        page_titles: Set of page titles for hashtag validation
        output_dir: Output directory for downloading images
        dry_run: If True, don't actually download images
        verbose: If True, print verbose output
    """
    if not text:
        return text
    
    # Code block start
    if text.startswith('code:'):
        lang = text[5:].strip()
        return f'```{lang}'
    
    # Quote
    if text.startswith('>'):
        return text
    
    # Store original indentation information
    original_text = text
    indent_prefix = ''
    content_to_process = text
    
    # Check for list items with asterisks
    if text.lstrip().startswith('*') and (text.startswith(' ') or text.startswith('*')):
        # Count leading spaces
        space_count = len(text) - len(text.lstrip(' '))
        # Remove spaces and asterisk to get content
        content_to_process = text.lstrip(' ').lstrip('*').lstrip()
        
        # Calculate indentation level based on 4-space increments
        if space_count == 0 and text.startswith('*'):
            # Top level: no spaces, starts with *
            indent_prefix = '- '
        elif space_count % 4 == 0:
            # Each 4 spaces = one indent level
            indent_level = space_count // 4
            indent_prefix = '  ' * indent_level + '- '
        else:
            # Non-standard spacing, keep as is
            return text
    # Check for other indented content
    elif text.startswith(' '):
        # Check for space + tab pattern (second level)
        if len(text) > 1 and text[1] == '\t':
            # Second level: 1 space + tab
            indent_prefix = '  - '
            content_to_process = text[2:]
        else:
            # First level: single space (or multiple spaces in code block)
            # Count leading spaces
            space_count = len(text) - len(text.lstrip(' '))
            if space_count == 1:
                # Single space = first level list
                indent_prefix = '- '
                content_to_process = text[1:]
            else:
                # Multiple spaces = keep as is (likely code)
                pass  # Keep original text
    
    # Now process the content (without indentation)
    text = content_to_process
    
    # Skip hashtag conversion for lines that look like jQuery code
    if '$(' in text and '#' in text:
        convert_hashtags = False
    else:
        convert_hashtags = True
    
    # Inline notation conversion
    # [*** heading] - headings with 2+ asterisks
    def replace_heading(match):
        asterisks = match.group(1)
        heading_text = match.group(2)
        asterisk_count = len(asterisks)
        
        # Convert to markdown heading
        # max_heading_level asterisks = # (H1)
        # fewer asterisks = lower heading levels
        heading_level = max_heading_level - asterisk_count + 1
        heading_level = max(1, min(6, heading_level))  # Clamp between 1-6
        
        return '#' * heading_level + ' ' + heading_text
    
    text = re.sub(r'\[(\*{2,})\s+([^\]]+)\]', replace_heading, text)
    
    # [* bold] - single asterisk remains as bold
    text = re.sub(r'\[\*\s+([^\]]+)\]', r'**\1**', text)
    
    # [/ italic]
    text = re.sub(r'\[/\s+([^\]]+)\]', r'*\1*', text)
    
    # [https://...] image - download and convert
    def replace_image(match):
        url = match.group(1)
        if output_dir is None:
            raise ValueError("output_dir is required for image download")
        local_path = download_image(url, output_dir, dry_run, verbose)
        return f'![]({local_path})'
    
    text = re.sub(r'\[(https?://[^\]]+\.(png|jpg|jpeg|gif|svg))\]', replace_image, text, flags=re.IGNORECASE)
    
    # #hashtag - convert to links if page exists
    if convert_hashtags and page_titles:
        def replace_hashtag(match):
            tag = match.group(1)
            if tag in page_titles:
                # Generate safe filename
                filename = tag.replace(' ', '_').replace('/', '_')
                filename = re.sub(r'[<>:"|?*]', '', filename)
                return f'[{tag}]({filename}.md)'
            else:
                # Page doesn't exist - this will be caught later
                return match.group(0)
        
        text = re.sub(r'#([^\s\[\]]+)', replace_hashtag, text)
    
    # [link](https://scrapbox.io/project/page) - convert to local link
    def replace_scrapbox_link(match):
        link_text = match.group(1)
        url = match.group(2)
        
        # Parse scrapbox.io URL
        parsed = urllib.parse.urlparse(url)
        if parsed.netloc == 'scrapbox.io':
            path_parts = parsed.path.strip('/').split('/', 1)
            if len(path_parts) == 2:
                project_name = path_parts[0]
                page_title_encoded = path_parts[1]
                
                # Decode the page title
                page_title = urllib.parse.unquote(page_title_encoded)
                
                # Check if page exists
                if page_titles:
                    # Try exact match first
                    if page_title in page_titles:
                        # Generate safe filename
                        filename = page_title.replace(' ', '_').replace('/', '_')
                        filename = re.sub(r'[<>:"|?*]', '', filename)
                        return f'[{link_text}]({filename}.md)'
                    # Try with underscores converted to spaces
                    elif '_' in page_title:
                        page_title_with_spaces = page_title.replace('_', ' ')
                        if page_title_with_spaces in page_titles:
                            # Generate safe filename
                            filename = page_title_with_spaces.replace(' ', '_').replace('/', '_')
                            filename = re.sub(r'[<>:"|?*]', '', filename)
                            return f'[{link_text}]({filename}.md)'
                
                # Page doesn't exist - this will be caught in validation
                return match.group(0)
        
        return match.group(0)
    
    text = re.sub(r'\[([^\]]+)\]\((https://scrapbox\.io/[^)]+)\)', replace_scrapbox_link, text)
    
    # [link] internal link - process last to avoid conflicts
    def replace_internal_link(match):
        full_match = match.group(0)
        link_text = match.group(1)
        
        # Skip if it's a formatting pattern
        if link_text.startswith('*') or link_text.startswith('/'):
            return full_match
        
        # Skip if it's a URL
        if link_text.startswith('http://') or link_text.startswith('https://'):
            return full_match
        
        # Process as internal link
        if page_titles:
            # Try exact match first
            if link_text in page_titles:
                filename = link_text.replace(' ', '_').replace('/', '_')
                filename = re.sub(r'[<>:"|?*]', '', filename)
                return f'[{link_text}]({filename}.md)'
            # Try with spaces converted to underscores
            elif ' ' in link_text:
                link_text_with_underscores = link_text.replace(' ', '_')
                if link_text_with_underscores in page_titles:
                    filename = link_text_with_underscores.replace(' ', '_').replace('/', '_')
                    filename = re.sub(r'[<>:"|?*]', '', filename)
                    return f'[{link_text}]({filename}.md)'
            # Try with underscores converted to spaces
            elif '_' in link_text:
                link_text_with_spaces = link_text.replace('_', ' ')
                if link_text_with_spaces in page_titles:
                    filename = link_text_with_spaces.replace(' ', '_').replace('/', '_')
                    filename = re.sub(r'[<>:"|?*]', '', filename)
                    return f'[{link_text}]({filename}.md)'
        
        # Default: just convert to .md link
        filename = link_text.replace(' ', '_').replace('/', '_')
        filename = re.sub(r'[<>:"|?*]', '', filename)
        return f'[{link_text}]({filename}.md)'
    
    # Match [text] but not [text](url) - use negative lookahead
    text = re.sub(r'\[([^\]]+)\](?!\()', replace_internal_link, text)
    
    # Convert plain text URLs to markdown links
    # Match URLs that are not already in markdown link format or brackets
    def replace_plain_url(match):
        url = match.group(0)
        # Check if URL is already part of markdown link or bracketed
        full_text = match.string
        start = match.start()
        
        # Check if preceded by [ or (
        if start > 0 and full_text[start-1] in '[(':
            return url
        
        # Check if followed by ] or )
        end = match.end()
        if end < len(full_text) and full_text[end] in '])':
            return url
            
        return f'<{url}>'
    
    # Match http:// or https:// URLs
    text = re.sub(r'https?://[^\s\[\]()<>]+', replace_plain_url, text)
    
    # Apply indent prefix if any
    if indent_prefix:
        return indent_prefix + text
    
    return text


def convert_page(page, max_heading_level=3, page_titles=None, output_dir=None, dry_run=False, verbose=False, incoming_links=None):
    """Convert page to Markdown format, returns (filename, content)"""
    title = page['title']
    
    # Generate filename (handle special characters)
    filename = title.replace(' ', '_').replace('/', '_')
    filename = re.sub(r'[<>:"|?*]', '', filename)
    filename = f"{filename}.md"
    
    # Generate frontmatter
    created = datetime.fromtimestamp(page['created']).isoformat() + 'Z'
    updated = datetime.fromtimestamp(page['updated']).isoformat() + 'Z'
    
    content_lines = [
        '---',
        f'title: "{title}"',
        f'created: {created}',
        f'updated: {updated}',
        f'id: "{page["id"]}"',
        f'views: {page["views"]}',
    ]
    
    if page.get('linksLc'):
        links_str = ', '.join([f'"{link}"' for link in page['linksLc']])
        content_lines.append(f'links: [{links_str}]')
    
    content_lines.extend(['---', '', f'# {title}', ''])
    
    # Convert body text
    in_code_block = False
    for line in page['lines']:
        text = line.get('text', '')
        
        # Handle code blocks
        if text.startswith('code:'):
            in_code_block = True
        elif in_code_block and text and not text.startswith(' '):
            # End code block
            content_lines.append('```')
            in_code_block = False
        
        # Convert line
        if in_code_block and not text.startswith('code:'):
            # Keep code block content as-is
            content_lines.append(text)
        else:
            converted_text = parse_scrapbox_line(text, max_heading_level, page_titles, output_dir, dry_run, verbose)
            content_lines.append(converted_text)
    
    # Close code block if still open
    if in_code_block:
        content_lines.append('```')
    
    # Add back links if any
    if incoming_links and title in incoming_links and incoming_links[title]:
        content_lines.extend(['', '---', ''])
        linking_pages = incoming_links[title]
        
        if len(linking_pages) == 1:
            # Single back link
            page_name = linking_pages[0]
            safe_filename = page_name.replace(' ', '_').replace('/', '_')
            safe_filename = re.sub(r'[<>:"|?*]', '', safe_filename)
            content_lines.append(f'← [{page_name}に戻る]({safe_filename}.md)')
        else:
            # Multiple back links
            links = []
            for page_name in linking_pages:
                safe_filename = page_name.replace(' ', '_').replace('/', '_')
                safe_filename = re.sub(r'[<>:"|?*]', '', safe_filename)
                links.append(f'[{page_name}]({safe_filename}.md)')
            content_lines.append(f'← 戻る: {" | ".join(links)}')
    
    return filename, '\n'.join(content_lines)


def download_image(url, output_dir, dry_run=False, verbose=False):
    """Download image from URL and save to images directory
    
    Returns:
        str: Local path to the image file
    """
    # Create images directory
    images_dir = os.path.join(output_dir, 'images')
    if not dry_run:
        os.makedirs(images_dir, exist_ok=True)
    
    # Generate filename from URL
    parsed_url = urllib.parse.urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:
        # Use hash of URL if no filename found
        import hashlib
        ext = '.png'  # Default extension
        if '.' in url:
            ext = '.' + url.split('.')[-1].lower()[:4]  # Limit extension length
        filename = hashlib.md5(url.encode()).hexdigest()[:16] + ext
    
    local_path = os.path.join('images', filename)
    full_path = os.path.join(output_dir, local_path)
    
    if dry_run:
        if verbose:
            print(f"Would download: {url} -> {local_path}")
        return local_path
    
    # Download image if it doesn't exist
    if not os.path.exists(full_path):
        if verbose:
            print(f"Downloading: {url} -> {local_path}")
        urllib.request.urlretrieve(url, full_path)
    
    return local_path


def convert_json_file(json_path, output_dir, dry_run=False, verbose=False):
    """Convert entire JSON file"""
    # Read JSON file
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    project_name = data.get('displayName', 'unknown')
    pages = data.get('pages', [])
    
    # Create set of page titles for hashtag validation
    page_titles = {page['title'] for page in pages}
    
    # Build incoming links map (which pages link to each page)
    incoming_links = {}
    for page in pages:
        source_title = page['title']
        
        # Extract all links from the page text
        linked_pages = set()
        
        for line in page.get('lines', []):
            text = line.get('text', '')
            
            # Skip jQuery code patterns
            if '$(' in text and '#' in text:
                continue
            
            # Find [text] style links (but not special patterns)
            bracket_links = re.findall(r'\[([^\]]+)\](?!\()', text)
            for link in bracket_links:
                # Skip special patterns
                if (not link.startswith('http') and 
                    not link.startswith('*') and 
                    not link.startswith('/')):
                    # Check if this page exists
                    for target_page in pages:
                        if target_page['title'] == link:
                            linked_pages.add(link)
                            break
                        # Try with space/underscore conversion
                        elif target_page['title'].replace(' ', '_') == link:
                            linked_pages.add(target_page['title'])
                            break
                        elif target_page['title'].replace('_', ' ') == link:
                            linked_pages.add(target_page['title'])
                            break
            
            # Find #hashtag style links
            hashtags = re.findall(r'#([^\s\[\]]+)', text)
            for tag in hashtags:
                # Check if this page exists
                for target_page in pages:
                    if target_page['title'] == tag:
                        linked_pages.add(tag)
                        break
            
            # Find [text](page.md) style links
            md_links = re.findall(r'\[([^\]]+)\]\(([^)]+\.md)\)', text)
            for link_text, link_path in md_links:
                if not link_path.startswith('http'):
                    page_name = link_path[:-3]  # Remove .md
                    # Check if this page exists
                    for target_page in pages:
                        if target_page['title'] == page_name:
                            linked_pages.add(page_name)
                            break
                        # Try with space/underscore conversion
                        elif target_page['title'].replace(' ', '_') == page_name:
                            linked_pages.add(target_page['title'])
                            break
                        elif target_page['title'].replace('_', ' ') == page_name:
                            linked_pages.add(target_page['title'])
                            break
            
            # Find scrapbox.io links
            scrapbox_links = re.findall(r'\[([^\]]+)\]\((https://scrapbox\.io/[^)]+)\)', text)
            for link_text, url in scrapbox_links:
                parsed = urllib.parse.urlparse(url)
                if parsed.netloc == 'scrapbox.io':
                    path_parts = parsed.path.strip('/').split('/', 1)
                    if len(path_parts) == 2:
                        page_title_encoded = path_parts[1]
                        page_title = urllib.parse.unquote(page_title_encoded)
                        # Check if this page exists
                        for target_page in pages:
                            if target_page['title'] == page_title:
                                linked_pages.add(page_title)
                                break
                            # Try with space/underscore conversion
                            elif target_page['title'].replace(' ', '_') == page_title:
                                linked_pages.add(target_page['title'])
                                break
                            elif target_page['title'].replace('_', ' ') == page_title:
                                linked_pages.add(target_page['title'])
                                break
        
        # Add to incoming links map
        for target_title in linked_pages:
            if target_title not in incoming_links:
                incoming_links[target_title] = []
            if source_title not in incoming_links[target_title]:
                incoming_links[target_title].append(source_title)
    
    # Find maximum heading level (asterisk count) in the document
    max_heading_level = 1
    for page in pages:
        for line in page.get('lines', []):
            text = line.get('text', '')
            match = re.search(r'\[(\*{2,})\s+[^\]]+\]', text)
            if match:
                asterisk_count = len(match.group(1))
                max_heading_level = max(max_heading_level, asterisk_count)
    
    # Check for invalid hashtags, scrapbox.io links, and local markdown links
    invalid_hashtags = set()
    invalid_scrapbox_links = []
    invalid_local_links = []
    
    # Get project name from JSON data
    project_name = data.get('name', '')
    
    for page in pages:
        for line in page.get('lines', []):
            text = line.get('text', '')
            # Skip jQuery code
            if '$(' in text and '#' in text:
                continue
            # Find hashtags
            hashtag_matches = re.findall(r'#([^\s\[\]]+)', text)
            for tag in hashtag_matches:
                if tag not in page_titles:
                    invalid_hashtags.add(tag)
            
            # Find scrapbox.io links
            link_matches = re.findall(r'\[([^\]]+)\]\((https://scrapbox\.io/[^)]+)\)', text)
            for link_text, url in link_matches:
                parsed = urllib.parse.urlparse(url)
                if parsed.netloc == 'scrapbox.io':
                    path_parts = parsed.path.strip('/').split('/', 1)
                    if len(path_parts) == 2:
                        link_project = path_parts[0]
                        page_title_encoded = path_parts[1]
                        page_title = urllib.parse.unquote(page_title_encoded)
                        
                        # Only check if it's the same project
                        if link_project == project_name:
                            # Try exact match first
                            found = page_title in page_titles
                            # Try with underscores converted to spaces
                            if not found and '_' in page_title:
                                page_title_with_spaces = page_title.replace('_', ' ')
                                found = page_title_with_spaces in page_titles
                            
                            if not found:
                                invalid_scrapbox_links.append({
                                    'url': url,
                                    'page_title': page_title,
                                    'in_page': page['title']
                                })
            
            # Find local markdown links [text](file.md)
            local_link_matches = re.findall(r'\[([^\]]+)\]\(([^)]+\.md)\)', text)
            for link_text, link_path in local_link_matches:
                # Skip if it's a URL
                if link_path.startswith('http://') or link_path.startswith('https://'):
                    continue
                
                # Extract page name from link path (remove .md extension)
                if link_path.endswith('.md'):
                    page_name = link_path[:-3]
                    
                    # Try exact match first
                    found = page_name in page_titles
                    
                    # Try with spaces converted to underscores
                    if not found and ' ' in page_name:
                        page_name_with_underscores = page_name.replace(' ', '_')
                        found = page_name_with_underscores in page_titles
                    
                    # Try with underscores converted to spaces
                    if not found and '_' in page_name:
                        page_name_with_spaces = page_name.replace('_', ' ')
                        found = page_name_with_spaces in page_titles
                    
                    if not found:
                        invalid_local_links.append({
                            'link': f'[{link_text}]({link_path})',
                            'page_name': page_name,
                            'in_page': page['title']
                        })
    
    if invalid_hashtags:
        print(f"Warning: Found hashtags referencing non-existent pages:", file=sys.stderr)
        for tag in sorted(invalid_hashtags):
            print(f"  #{tag}", file=sys.stderr)
    
    if invalid_scrapbox_links:
        print(f"Error: Found scrapbox.io links referencing non-existent pages:", file=sys.stderr)
        for link in invalid_scrapbox_links:
            print(f"  {link['url']} -> \"{link['page_title']}\" (in {link['in_page']})", file=sys.stderr)
        return 1
    
    if invalid_local_links:
        print(f"Warning: Found local markdown links referencing non-existent pages:", file=sys.stderr)
        for link in invalid_local_links:
            print(f"  {link['link']} -> \"{link['page_name']}\" (in {link['in_page']})", file=sys.stderr)
    
    if verbose:
        print(f"Converting project: {project_name}")
        print(f"Total pages: {len(pages)}")
        print(f"Max heading level: {max_heading_level} asterisks")
        if invalid_hashtags:
            print(f"Warning: {len(invalid_hashtags)} invalid hashtags found (dry-run mode)")
    
    # Create output directory
    if not dry_run:
        os.makedirs(output_dir, exist_ok=True)
    
    # Convert each page
    for i, page in enumerate(pages):
        filename, content = convert_page(page, max_heading_level, page_titles, output_dir, dry_run, verbose, incoming_links)
        output_path = os.path.join(output_dir, filename)
        
        if dry_run:
            if os.path.exists(output_path):
                # Show diff for existing files
                with open(output_path, 'r', encoding='utf-8') as f:
                    old_content = f.read()
                
                # Generate unified diff format
                old_lines = old_content.splitlines()
                new_lines = content.splitlines()
                
                print(f"\n--- {output_path}")
                print(f"+++ {output_path}")
                
                # Use difflib
                diff = difflib.unified_diff(
                    old_lines,
                    new_lines,
                    lineterm='',
                    n=3
                )
                # Skip first 2 lines (filenames)
                for _ in range(2):
                    next(diff, None)
                
                has_diff = False
                for line in diff:
                    has_diff = True
                    print(line)
                
                if not has_diff:
                    print("(no changes)")
            else:
                # New file
                print(f"\n{output_path}: (new file)")
                print(content)
        else:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
            if verbose:
                print(f"Created: {output_path}")
    
    if verbose:
        print(f"\nConversion completed!")


def main():
    """Command line processing"""
    parser = argparse.ArgumentParser(
        description='Convert Scrapbox JSON to Markdown files'
    )
    parser.add_argument('json_file', help='Path to Scrapbox JSON file')
    parser.add_argument('-o', '--output', default='.',
                        help='Output directory (default: .)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be done without creating files')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose output')
    
    args = parser.parse_args()
    
    # Check input file
    if not os.path.exists(args.json_file):
        print(f"convert_scrapbox.py: {args.json_file}: No such file or directory", file=sys.stderr)
        return 1
    
    # Execute conversion
    result = convert_json_file(args.json_file, args.output, args.dry_run, args.verbose)
    if result == 1:
        return 1
    return 0


if __name__ == '__main__':
    exit(main())