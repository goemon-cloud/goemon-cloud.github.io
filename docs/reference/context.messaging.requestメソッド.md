---
layout: default
parent: context.messagingプロパティ
grand_parent: contextオブジェクト
nav_order: 1

title: "context.messaging.requestメソッド"
created: 2022-06-30T12:23:58Z
updated: 2022-06-30T13:13:45Z
id: "62bd174ae1c50a001e6e5bb2"
views: 23
---
# context.messaging.requestメソッド

タスクとメッセージ(チャット)サービスの連携を要求します。引数には以下の2つが指定可能です。

## optionsパラメータ
options には最低限 `type` を指定します。サポートされている値と挙動は以下の通りです。

| type | 説明 |
| --- | --- |
| `'line'` | GO-E-MON LINEアカウントと1対1のトークを開始します。ユーザー側で友達追加と許可操作が必要です。 |
| `'linegroup'` | LINEグループとのやり取りを開始します。ユーザーがトークグループを選択し、許可ダイアログで承認します。 |
| `'mail'` | メール送信用のトークユーザーを自動生成します。許可ダイアログは表示されず、即座に送信可能になります。 |

## callbackパラメータ
要求成功時・失敗時に呼び出されるfunctionを指定することができます。functionには以下の引数が指定されます。
- result ... 連携がキャンセルされた場合、nullが入ります。連携に成功した場合、null以外の値が入ります
- error ... 連携時にエラーが発生した場合、null以外の値が入ります

