---
layout: default
parent: context.messagingプロパティ
grand_parent: contextオブジェクト
nav_order: 10
has_children: true
title: "context.messaging.setScheduleメソッド"
created: 2022-06-30T12:30:39Z
updated: 2022-07-23T18:08:36Z
id: "62bd189c450abc001d44f8ca"
views: 44
links: ["context.messaging.setscheduleメソッド.options.scriptパラメータ", "context.messaging.setscheduleメソッド.options.messageパラメータ", "context.messaging.setscheduleメソッド.options.urlパラメータ", "context.messaging.requestメソッド"]
---
# context.messaging.setScheduleメソッド

context.messaging.setScheduleメソッド
タスクのチャットをスケジュールします。引数には以下の2つが指定可能です。

## optionsパラメータ
スケジュールの設定を定義します。
- schedule: cronexpression(ex: '0 7-21 * * *') ... 自動送信間隔。Cron Expression <https://en.wikipedia.org/wiki/Cron> が指定可能です。
- messageToPDS: true|false ... やり取りされたメッセージをPersonaryに保存する場合はtrue
- script: スクリプトの実行をスケジュールしたい場合、JavaScriptで記述したスクリプトを設定します。message, url, scriptのいずれかを設定する必要があります。詳細は [context.messaging.setScheduleメソッド.options.scriptパラメータ](context.messaging.setScheduleメソッド.options.scriptパラメータ.html) を参照してください。
- message: 固定メッセージをスケジュールしたい場合、メッセージの内容を定義します。message, url, scriptのいずれかを設定する必要があります。詳細は [context.messaging.setScheduleメソッド.options.messageパラメータ](context.messaging.setScheduleメソッド.options.messageパラメータ.html) を参照してください。
- url: 外部サービスでメッセージを生成したい場合、外部サービスのURLを定義します。詳細は [context.messaging.setScheduleメソッド.options.urlパラメータ](context.messaging.setScheduleメソッド.options.urlパラメータ.html) を参照してください。

## callbackパラメータ
要求成功時・失敗時に呼び出されるfunctionを指定することができます。functionには以下の引数が指定されます。
- error ... 連携時にエラーが発生した場合、null以外の値が入ります

[context.messaging.requestメソッド](context.messaging.requestメソッド.html) を事前に実施しておく必要があります。
