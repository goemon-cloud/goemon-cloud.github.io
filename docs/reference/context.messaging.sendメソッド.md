---
layout: default
parent: context.messagingプロパティ
grand_parent: contextオブジェクト
nav_order: 5

title: "context.messaging.sendメソッド"
created: 2025-10-22T00:00:00Z
updated: 2025-10-22T00:00:00Z
id: "context-messaging-send"
views: 0
---

# context.messaging.sendメソッド

`context.messaging.request` で連携したメッセージサービスに対してメッセージを送信します。送信が完了すると `callback` が呼び出され、第1引数にエラー情報（成功時は `null`）が渡されます。

## 引数

- **message**: 送信内容を表すオブジェクト。サービスによって構造が異なります。
- **callback**: 送信完了時に呼び出される関数。省略可能です。

## LINE / LINEグループ

`type: 'line'` または `type: 'linegroup'` で連携した場合は、LINE Messaging API のメッセージ仕様に従います。

```javascript
context.messaging.send({
  type: 'text',
  text: 'Hello, world'
}, (error) => {
  if (error) {
    context.log('送信に失敗しました', { error });
  }
});
```

利用可能なメッセージ形式の詳細は LINE 公式ドキュメントを参照してください。
- <https://developers.line.biz/ja/reference/messaging-api/#text-message>

## メール

`type: 'mail'` で連携すると、許可ダイアログなしでメール送信用トークユーザーが自動作成されます。`message` には以下のプロパティを指定します。

| フィールド | 必須 | 説明 |
| --- | --- | --- |
| `subject` | ✓ | メール件名 |
| `body` | ✓ | プレーンテキスト本文 |
| `htmlBody` |  | HTML本文。省略時はプレーンテキストのみ送信 |
| `to` | ✓ | 宛先メールアドレス（文字列または文字列配列） |

送信元（From）は環境側で決められたシステムアドレスが利用されます。1時間あたり10通までのレート制限があり、超過すると `callback` の第1引数にエラーが渡されます。

```javascript
context.messaging.send({
  subject: '実験参加の御礼',
  body: 'ご協力ありがとうございました。',
  to: 'participant@example.com'
});
```

## エラーハンドリング

- LINE／メール共通で、送信に失敗した場合は `callback` の第1引数にエラーオブジェクトが設定されます。
- `callback` を省略した場合はエラーがタスクスクリプトに伝播しないため、重要な連絡を送るワークフローではハンドリングを実装してください。

