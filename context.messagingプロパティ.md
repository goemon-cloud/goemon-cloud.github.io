---
title: "context.messagingプロパティ"
created: 2022-06-28T19:01:39Z
updated: 2022-06-30T14:56:04Z
id: "62bad180cdf6fc001d65353e"
views: 56
links: ["context.messaging.requestメソッド", "context.messaging.setscheduleメソッド"]
---

# context.messagingプロパティ

context.messagingプロパティ
GO-E-MONでは、ユーザーとWebブラウザを介してやり取りするほかに、LINEを通じたチャットベースのタスクも実現することができます。チャットベースのタスクを実現するためには、以下の手順を踏む必要があります。
- ユーザーが当該GO-E-MONタスクにWebブラウザを通じてアクセスする
- 当該GO-E-MONタスクのスクリプト中で、 context.messaging.request メソッドを通じてGO-E-MONアカウントとLINEアカウントとの連携要求を発行する
- 定期実行のスケジュールを設定する

定期実行は**最短で5分間隔**で実行可能ですが、以下の制限があります。
- GO-E-MONサーバーにおける定期実行タスクの実行状況により、予定時間よりも遅れて実行される場合があります
- 定期実行に設定したスクリプトの実行に失敗したり、URLが30秒以上経過してもレスポンスを返さない場合、その実行から24時間後以降に再スケジュールされます
- 定期実行は、スケジュール設定後2週間の間、継続的に実行されます。2週間を超えて定期実行を設定したい場合は、2週間以内にユーザーをGO-E-MONタスクのURLに誘導し、定期実行スケジュールを再設定する必要があります

## context.messaging.request(options, callback) メソッド
[context.messaging.requestメソッド](context.messaging.requestメソッド.md)(context.messaging.requestメソッド.md) を参照してください。

## context.messasging.send(message, callback) メソッド
context.messaging.requestによって連携されたLINEアカウントに対してメッセージを送信します。
message引数には LINE Messaging API で紹介されている https://developers.line.biz/ja/docs/messaging-api/overview/#what-you-can-do メッセージを定義することができます。
例えば、テキストメッセージを送信したい場合は、 https://developers.line.biz/ja/reference/messaging-api/#text-message を参考に以下のような値を設定します。

```javascript
  // テキストメッセージの例
  {
    "type": "text",
    "text": "Hello, world"
  }

```
メッセージの送信が完了すると、callback関数が呼び出されます。第1引数にはメッセージの送信に失敗した場合にエラーオブジェクトが格納されます。

## context.messaging.setSchedule(options, callback) メソッド
[context.messaging.setScheduleメソッド](context.messaging.setScheduleメソッド.md)(context.messaging.setScheduleメソッド.md) を参照してください。

## context.messaging.clearSchedule(callback) メソッド
[context.messaging.setScheduleメソッド](context.messaging.setScheduleメソッド.md)(context.messaging.setScheduleメソッド.md)  により設定されたタスクの定期実行指定をキャンセルします。定期実行が未指定の場合は何もしません。

## context.messaging.getLastResult(callback) メソッド
このユーザーに関して実行された定期実行結果のうち、最後に検出されたエラーと、コンソール出力を取得します。
callbackに指定したfunctionの第1引数には { error: 最後に検出されたエラーの内容, console: 最後に実行されたコンソール出力 } が、定期実行が未スケジュールの場合はnullが格納されます。第2引数には結果の取得に失敗した場合にエラーオブジェクトが格納されます。
