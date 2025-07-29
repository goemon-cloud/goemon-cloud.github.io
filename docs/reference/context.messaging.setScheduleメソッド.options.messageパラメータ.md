---
layout: default
parent: リファレンス
nav_order: 17

title: "context.messaging.setScheduleメソッド.options.messageパラメータ"
created: 2022-06-30T13:23:21Z
updated: 2022-06-30T14:40:30Z
id: "62bd25368f073a001dfbf914"
views: 9
---

# context.messaging.setScheduleメソッド.options.messageパラメータ

context.messaging.setScheduleメソッド.options.messageパラメータ
messageパラメータには scheduled, replyの2つのパラメータが指定可能です。
- scheduled ... 定期実行の際に送信するメッセージをJSON文字列により指定します。このJSON文字列には LINE Messaging API で紹介されている <https://developers.line.biz/ja/docs/messaging-api/overview/#what-you-can-do> メッセージを定義することができます。
- reply ... 利用者からの返信の際に送信するメッセージをJSON文字列により指定します。このJSON文字列には LINE Messaging API で紹介されている <https://developers.line.biz/ja/docs/messaging-api/overview/#what-you-can-do> メッセージを定義することができます。

```javascript
 message: {
   scheduled: JSON.stringify({
     type: 'text',
     text: '30分の時報です！',
   }),
   reply: JSON.stringify({
     type: 'text',
     text: '返信です！',
   }),
 },

```

---
