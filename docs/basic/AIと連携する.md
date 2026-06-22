---
layout: default
title: AIと連携する
parent: 基本操作
nav_order: 1
---

# AIと連携する

GO-E-MONは [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) に対応しています。ChatGPTなどのMCPクライアントをGO-E-MONに接続すると、**コードを自分で書かなくても、AIとの会話でタスクを操作できます**。

「Stroop課題を作って」「このアンケートに自由記述欄を追加して」のように指示するだけで、AIがあなたのGO-E-MONタスクを直接読み書きします。JavaScriptやHTMLに不慣れな方でも、GO-E-MONを使うことができます。

手作業でコードを書く方法（[タスクの作成](タスクの作成.html) や各チュートリアル）と組み合わせることもできます。AIに任せる部分と自分で調整する部分を、自由に使い分けてください。

## 動画で見る

AI連携の使い方を、以下の動画で解説しています。

<iframe width="560" height="315" src="https://www.youtube.com/embed/Qfa0eK9q4eE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## できること

接続したAIから、次のような操作を行えます。

- タスクの一覧の確認、コード・タイトル・説明・設定・関連ファイルの読み取り
- コードやタイトル・説明の編集、設定値の変更、ファイルの作成・更新・削除
- 新規タスクの作成
- タスクの配備（デプロイ）、デバッグの実行

どこまで許可するかは接続するときにあなたが選びます。読み取りだけを許可して、編集や新規作成は許可しない、といった使い分けも可能です。

## 接続のしかた

1. お使いのMCPクライアント（ChatGPTなど）に、GO-E-MONのMCPサーバーを追加します。サーバーURLは以下です（クライアントごとの追加方法は [関連リンク](#関連リンク) を参照してください）。

   ```
   https://goemon.cloud/mcp
   ```

2. クライアントから接続すると、GO-E-MONの認可画面「**MCPアクセスの許可**」が開きます。GO-E-MONにログインしてください（GO-E-MONアカウントの作成に使ったGoogleアカウントを利用します）。

3. 認可画面で、このクライアントに許可する範囲を選びます。

   - **MCPから利用を許可するタスク**: 「すべてのタスクの操作を許可」するか、特定のタスクを絞り込んで選びます。
   - **書き込み操作を許可する**: オンにすると編集・配備などの変更操作を許可します。オフのままなら読み取りのみです。
   - **新規タスク作成を許可する**: オンにするとAIが新しいタスクを作成できます。

4. 「**許可**」を押すと、クライアントがGO-E-MONに接続され、選んだ範囲でタスクを操作できるようになります。

## 権限と安全性

- AIやMCPクライアントは、あなたが認可した範囲でのみ操作できます。操作のたびにGO-E-MON側で許可内容を再確認するため、認可していないタスクや操作は実行されません。
- 書き込みを許可しなければ、AIはタスクを読み取るだけで変更はできません。
- 認可は、あなたが解除するまで有効です。権限を増やす場合は、認可画面で対象タスクと権限を選び直します。

## 連携の管理・解除

接続中のAI連携は、GO-E-MONの設定画面の「**MCP接続**」で管理できます。ここでは、接続先のクライアント、許可したタスク、書き込み可否、新規タスク作成可否、最終利用日時を確認できます。

不要になった連携は、この画面から取り消せます。

## 関連リンク

クライアントへのGO-E-MONの登録方法は、各クライアントの公式ドキュメントを参照してください。

- **Claude**: [カスタムコネクタ（リモートMCP）を追加する](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) — claude.ai や Claude Desktop の設定から追加できます。
- **ChatGPT**: [デベロッパーモードでMCPコネクタを追加する](https://help.openai.com/en/articles/12584461-developer-mode-apps-and-full-mcp-connectors-in-chatgpt-beta) — 設定でデベロッパーモードを有効にしてから追加します。
- **Google（Gemini）**: 一般向けのGeminiアプリやGoogle AI Studioは、現状カスタムリモートMCPコネクタに対応していません。接続するにはAntigravityやGemini Enterpriseなどの開発者向けツールが必要です（[AIアプリケーションでMCPを設定する](https://docs.cloud.google.com/mcp/configure-mcp-ai-application)）。
- [Model Context Protocol 公式サイト](https://modelcontextprotocol.io/)
