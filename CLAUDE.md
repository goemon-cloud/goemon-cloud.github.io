# プロジェクトコンセプト

## 概要
このプロジェクトは、Scrapbox.ioでホストしていたドキュメントをGitHub Pagesでホストできるように変換するものです。

## 背景
- archive/ディレクトリにScrapboxからエクスポートしたJSONファイルが保存されている
- これらのJSONファイルには独自のScrapbox記法で記述されたドキュメントが含まれている
- GitHub Pages（github.io）でホストするためにMarkdown形式への変換が必要

## アプローチ
1. **分析フェーズ**
   - JSONファイルの構造を解析
   - Scrapbox記法の特定と理解
   
2. **設計フェーズ**
   - Markdown変換仕様の策定
   - ファイル構成の決定
   
3. **実装フェーズ**
   - PythonスクリプトによるJSON→Markdown変換ツールの作成
   - バッチ処理による全ドキュメントの変換

## 技術スタック
- **言語**: Python
- **入力形式**: Scrapbox JSON
- **出力形式**: Markdown with frontmatter
- **ホスティング**: GitHub Pages