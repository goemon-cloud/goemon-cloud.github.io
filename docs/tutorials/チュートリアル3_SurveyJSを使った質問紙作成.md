---
layout: default
title: "チュートリアル3: SurveyJSを使った質問紙作成"
parent: チュートリアル
nav_order: 3
---

# チュートリアル3: SurveyJSを使った質問紙作成

GO-E-MONで[SurveyJS](https://surveyjs.io/)を使用して、アンケートフォームを作成するチュートリアルです。SurveyJSを使うことで、条件分岐や複雑なバリデーション、多様な質問形式を簡単に実装することができます。

## 全体の流れ

このチュートリアルでは、以下の手順でSurveyJSを使った実験タスクを作成します：

1. [タスクの作成](#タスクの作成) - 新規タスクを作成
2. [タスク名の設定](#タスク名の設定) - タスクに名前を付ける
3. [SurveyJSフレームワークの設定](#surveyjsフレームワークの設定) - GOEMON_FRAMEWORKパラメータの設定
4. [アンケートフォームの作成](#アンケートフォームの作成) - SurveyJSエディタでフォームをデザイン
5. [JSONの設定](#jsonの設定) - DEFAULT_SURVEY_JSONにフォーム定義を設定
6. [テスト実行](#テスト実行) - 動作確認
7. [デバッグ確認](#デバッグ確認) - 結果データの形式を確認
8. [説明文の設定](#説明文の設定) - タスクの説明を追加
9. [配備](#配備) - 他のユーザーがアクセスできるように公開
10. [データの取得](#データの取得) - 収集したデータの分析方法

## 動画チュートリアル

操作については以下の動画で詳しく説明しています。

<iframe width="560" height="315" src="https://www.youtube.com/embed/GCzWxOJXNpI" title="GO-E-MONチュートリアル: SurveyJSを使った実験タスク作成" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## タスクの作成

GO-E-MONダッシュボード <https://goemon.cloud> にアクセスし、*タスクを作る*タブをクリックして、*新規タスクの追加* ボタンをクリックします。

![](/images/634dfcb739203500207b9077.png)


実験は「タスク」という単位で管理されます。

## タスク名の設定

作成されたタスクのタスク名を変更します。ダッシュボードから見つけ出しやすい名前を付けておきましょう。

![newTitle表示](/images/goemon-new-title.png)

タスク名を入力します。タスク名はENTERキーで確定できます。

![名前設定](/images/goemon-tutorial-1.png)

## SurveyJSフレームワークの設定

タスク設定から、SurveyJSを使うことを指定します。

1. *設定*タブを開き、*追加*をクリックします
2. *設定名*をクリックし、[GOEMON_FRAMEWORK](../reference/GOEMON_FRAMEWORK.html)を選択します
3. *フレームワーク*に`SurveyJS`を選び、*バージョン*は`2.2.3`を選びます
4. SurveyJSはさまざまなテーマを提供しています。お好みのテーマを選択してください

## アンケートフォームの作成

SurveyJSへの指示は`DEFAULT_SURVEY_JSON`設定で行います。

1. `DEFAULT_SURVEY_JSON`の*設定値*をクリックしてください
2. アンケートエディタはWebで提供されています。表示されているリンク https://surveyjs.io/create-free-survey をクリックしてください
3. エディタにはサンプルデータが設定されています。消しゴムボタンを押してクリアして編集をしましょう
4. フォームの情報を設定し、必要な質問項目を追加していきます

SurveyJSエディタでは、以下のような質問形式が利用できます(一例)：
- テキスト入力
- ラジオボタン
- 評価（星評価）
- マトリックス形式の質問

## JSONの設定

1. フォームを作ったら、エディタ上部の*JSON Editor*をクリックします
2. JSONと呼ばれる形式でフォームの定義を得ることができます
3. これをクリップボードにコピーして、`DEFAULT_SURVEY_JSON`の*設定値*に貼り付けます

再編集したい場合は、DEFAULT_SURVEY_JSONの設定値に表示されているJSONをコピーして、SurveyJSエディタの*JSON Editor*に貼り付けることで再度編集が可能です。

## テスト実行

これでアンケートの設定は完了です。タスクのテスト実行をするには、*はじめる*をクリックしてください。

アンケートが正しく実行されることを確認します。

## デバッグ確認

実行時のログなどは*デバッグ*タブから確認できます。

デバッグログから、結果がどのような形で記録されたかを確認することができます。出力データはSurveyJSの形式に準拠します。

## 説明文の設定

タスク開始前の説明文を更新します。*説明文*タブに実験の説明や注意事項を記載してください。

説明文の記述には[Markdown](../reference/Markdown.html)を使用することができます。

## 配備

他の人から使ってもらえるようサーバーに配備します。

1. *配備*タブをクリックします
2. *配備*ボタンをクリックします
3. 配備が完了したら、配布用のURLを取得します

配布用のURLやQRコードを実験参加者に渡すことで、実験に参加してもらうことができます。

> タスクの設定や説明文を変更したあとは、必ず配備ボタンを押して他のユーザーにも最新版を利用可能にする必要があります。

## データの取得

実験参加者がタスクを実施すると、実験結果は実験タスクの所有者と、実験参加者両方のPDS（個人ストレージ）に保存されます。

### 分析環境の利用

個人データを管理するPersonaryアプリには、データを分析ツールへと送り出す機能はありません。そこで、データ送り出し用の管理ツールを提供しています。

1. [github.com/goemon-cloud/notebook](https://github.com/goemon-cloud/notebook) を開きます
2. *launch binder*ボタンをクリックしてください
3. 分析環境が起動したら、Personaryからデータを取得できます

データ取り出し操作の詳細は[Personaryデータの分析](../basic/Personaryデータの分析.html)を参考にしてください。

## 関連リンク

- [SurveyJS公式サイト](https://surveyjs.io/)
- [SurveyJSエディタ](https://surveyjs.io/create-free-survey)
- [GOEMON_FRAMEWORKパラメータ](../reference/GOEMON_FRAMEWORK.html)
- [Personaryデータの分析](../basic/Personaryデータの分析.html)