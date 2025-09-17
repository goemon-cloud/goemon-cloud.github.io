---
layout: default
parent: リファレンス
nav_order: 13

title: "Param"
created: 2022-02-22T10:38:28Z
updated: 2022-04-12T08:00:05Z
id: "62143deca7badb001de885e9"
views: 45
links: ["contextオブジェクト", "context.pseudonymuseridプロパティ", "context.groupidプロパティ"]
---

# Param

Param
タスクの動作は 設定 タブでカスタマイズできるようにコードを記述することができます。設定タブには **設定名 と 設定値** の組み合わせを登録することができ、この内容をスクリプトから読み出すことができます。

![](/images/62144094f85f1a001d1df588.png)

タスク設定はスクリプトから [contextオブジェクト](contextオブジェクト.html) を介してアクセスすることができます。

設定タブでは以下のパラメータを設定することができます。

## GOEMON_ パラメータ

GOEMONシステムで特別な処理が行われるパラメータです：

- [GOEMON_FRAMEWORK](GOEMON_FRAMEWORK.html) - タスクで使用するフレームワーク（jsPsychなど）を指定する
- [GOEMON_GENERATE_ID_FOR_DISTRIBUTOR](GOEMON_GENERATE_ID_FOR_DISTRIBUTOR.html) - 仮名IDの識別可能範囲を配信者内に拡張する
- [GOEMON_AUTO_START](GOEMON_AUTO_START.html) - 一度実行したタスクを自動的に開始する
- [GOEMON_GROUP_IDS](GOEMON_GROUP_IDS.html) - 実験群を分ける場合の群ラベル定義
- [GOEMON_EMAIL_ALLOWLIST](GOEMON_EMAIL_ALLOWLIST.html) - ユーザをEメールアドレスのドメインで制限する
- [GOEMON_AGREEMENT](GOEMON_AGREEMENT.html) - タスク実行前に参加者の同意を取得する
- [GOEMON_COMPLETED_REDIRECT_URL](GOEMON_COMPLETED_REDIRECT_URL.html) - タスク完了後に参加者を別のページへリダイレクトする

