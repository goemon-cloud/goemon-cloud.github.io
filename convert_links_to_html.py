#!/usr/bin/env python3
import re
import os
from pathlib import Path

def convert_links_to_html(file_path):
    """MarkdownファイルのリンクをHTML形式に変換"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # ファイルの場所を取得
    file_dir = os.path.dirname(file_path)
    
    # リンクパターン: [テキスト](path/)
    # 外部URLやアンカーリンクは除外
    pattern = re.compile(r'\[([^\]]+)\]\(([^)]+?)/\)')
    
    def replace_link(match):
        link_text = match.group(1)
        link_path = match.group(2)
        
        # 外部URLの場合はそのまま
        if link_path.startswith('http://') or link_path.startswith('https://'):
            return match.group(0)
        
        # アンカーリンクの場合はそのまま
        if link_path.startswith('#'):
            return match.group(0)
        
        # 画像の場合はそのまま
        if link_path.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            return match.group(0)
            
        # ディレクトリパスはそのまま残す場合
        if link_path in ['..', '../..', '../../..']:
            return match.group(0)
        
        # /で終わるリンクを.htmlに変換
        return f'[{link_text}]({link_path}.html)'
    
    # コンテンツを変換
    new_content = pattern.sub(replace_link, content)
    
    # 変更があった場合のみ書き込み
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    # プロジェクトルート
    root_dir = Path('.')
    
    # 変更されたファイルをカウント
    modified_files = []
    
    # すべてのMarkdownファイルを処理
    for md_file in root_dir.rglob('*.md'):
        # archiveディレクトリは除外
        if 'archive' in str(md_file):
            continue
        
        if convert_links_to_html(md_file):
            modified_files.append(md_file)
    
    # 結果を表示
    if modified_files:
        print(f"修正されたファイル数: {len(modified_files)}")
        print("\n修正されたファイル:")
        for f in sorted(modified_files):
            print(f"  ✓ {f}")
    else:
        print("修正が必要なファイルはありませんでした。")

if __name__ == "__main__":
    main()