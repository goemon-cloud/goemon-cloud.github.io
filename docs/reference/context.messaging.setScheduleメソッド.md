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

タスクのチャットをスケジュールします。引数には以下の2つが指定可能です。

## optionsパラメータ
スケジュールの設定を定義します。
- schedule: cronexpression(ex: '0 7-21 * * *') ... 自動送信間隔。Cron Expression <https://en.wikipedia.org/wiki/Cron> が指定可能です。
- messageToPDS: true または false ... やり取りされたメッセージをPersonaryに保存する場合はtrue
- script: スクリプトの実行をスケジュールしたい場合、JavaScriptで記述したスクリプトを設定します。message, url, scriptのいずれかを設定する必要があります。詳細は [context.messaging.setScheduleメソッド.options.scriptパラメータ](context.messaging.setScheduleメソッド.options.scriptパラメータ.html) を参照してください。
- message: 固定メッセージをスケジュールしたい場合、メッセージの内容を定義します。message, url, scriptのいずれかを設定する必要があります。詳細は [context.messaging.setScheduleメソッド.options.messageパラメータ](context.messaging.setScheduleメソッド.options.messageパラメータ.html) を参照してください。
- url: 外部サービスでメッセージを生成したい場合、外部サービスのURLを定義します。詳細は [context.messaging.setScheduleメソッド.options.urlパラメータ](context.messaging.setScheduleメソッド.options.urlパラメータ.html) を参照してください。
- delayMinutes: 単発の遅延実行を設定します。現在時刻から指定分後に1度だけ実行されます（5〜525600の整数分）。`schedule` と同時に指定することはできません。

### 遅延実行（delayMinutes）
`delayMinutes` を指定すると、単発の実行スケジュールが作成されます。実行が完了するとスケジュールは自動的に解除され、再実行は行われません。遅延時間の計算やバックエンドの混雑状況により、実際の実行タイミングには数分程度のばらつきが生じる場合があります。

制約事項：
- 指定可能な値は 5 以上 525600 以下の整数（5分〜1年相当）です。
- `schedule` と `delayMinutes` を同時に指定するとエラーになります。
- バックオフが発生した場合は内部的に次回実行時刻が先送りされ、成功後は自動でクリアされます。

## callbackパラメータ
要求成功時・失敗時に呼び出されるfunctionを指定することができます。functionには以下の引数が指定されます。
- error ... 連携時にエラーが発生した場合、null以外の値が入ります

[context.messaging.requestメソッド](context.messaging.requestメソッド.html) を事前に実施しておく必要があります。
