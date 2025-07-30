---
layout: default
parent: 基本操作
nav_order: 6
title: "Personaryデータの分析"
---

# Personaryデータの分析

GO-E-MONで収集されたデータはPersonaryに保存されます。ここでは、Personaryに保存されたデータの基本的な分析方法を説明します。

## 動画チュートリアル

Personaryデータの分析方法について、以下の動画で詳しく解説しています。

<iframe width="560" height="315" src="https://www.youtube.com/embed/UDnVzIcem0U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## 分析の流れ

### 1. 分析環境の起動

Personaryアプリ自体にはデータを分析ツールへ送り出す機能がないため、専用の管理ツールを使用します。

分析ツールは以下で公開しています：
<https://github.com/goemon-cloud/notebook>

1. **[launch binder]ボタンをクリック** - 分析環境（JupyterLab）が起動します
2. **[00_PLR初期設定]を選択** - Jupyter Notebookが開きます

### 2. Personaryとの連携設定

1. **Googleアカウントを選択** - Personaryを使用しているGoogleアカウントを選択
2. **認証URLのコピー** - エラー画面に表示されるURLをコピー
3. **URLをペースト** - Jupyter Notebookのテキストボックスに貼り付け
4. **設定完了の確認** - エラー（赤文字）が表示されなければ連携成功

### 3. データの取得

**[01_PersonaryデータをExcelで取得する例]**を使用すると、実行記録をExcelファイルとして取得できます。

1. **取得条件の指定**
   - 取得期間を設定
   - タスクのURL（配備時に取得したURL）を入力
2. **実行と待機** - データ取得が完了するまで待つ
3. **ファイルのダウンロード** - 左側のファイルリストからExcelファイルをダウンロード

### 4. 取得したデータ

- タスクの実行記録は**仮名化された状態**で取得されます
- jsPsychのデータが**列として並んだ形式**でExcelファイルに保存されます
- このExcelファイルを使って実行記録の分析が可能です

## より高度な分析

より詳細な分析を行う場合は、以下のページを参照してください：

- [Jupyter NotebookでPersonaryのデータを分析する](../advanced/Jupyter_NotebookでPersonaryのデータを分析する.html)
- [分析環境の利用](../advanced/分析環境の利用.html)