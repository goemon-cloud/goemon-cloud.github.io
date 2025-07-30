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

context.messaging.requestメソッド
タスクとメッセージ(チャット)サービスの連携を要求します。引数には以下の2つが指定可能です。

## optionsパラメータ
optionsには以下の値が指定できます。
- type: 'line' | 'linegroup' ... 要求するサービスのタイプ。'line' の場合GO-E-MON LINEアカウントとのトークでのやり取り、'linegroup' の場合GO-E-MON LINEアカウントとの**トークグループでの**やり取りを要求します。

## callbackパラメータ
要求成功時・失敗時に呼び出されるfunctionを指定することができます。functionには以下の引数が指定されます。
- result ... 連携がキャンセルされた場合、nullが入ります。連携に成功した場合、null以外の値が入ります
- error ... 連携時にエラーが発生した場合、null以外の値が入ります

