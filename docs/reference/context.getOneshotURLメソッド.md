---
layout: default
parent: contextオブジェクト
grand_parent: リファレンス
nav_order: 12

title: "context.getOneshotURLメソッド"
created: 2025-10-22T13:56:36Z
updated: 2025-10-22T13:56:36Z
id: "context-get-oneshot-url"
views: 0
---

# context.getOneshotURLメソッド

ログイン中のタスクから一時的に共有できる実行リンク（ワンショットURL）を発行する非同期メソッドです。生成したリンクを参加者へ共有すると、ログインなしで同じ擬似ユーザーIDやグループ割当を引き継いで再開できます。`await context.getOneshotURL(...)` のように呼び出してください。

## オプション

| 項目 | 型 | 必須 | 説明 |
| --- | --- | --- | --- |
| `label` | string |  | ダッシュボードの一覧で判別しやすくする任意ラベル。 |
| `expiresInMinutes` | number |  | 有効期限を分単位で指定。未指定時はシステム既定値。 |
| `metadata` | object |  | リンクに添付する任意データ（2KB程度まで）。oneshot セッション開始時に `context.oneshot.metadata` として参照できます。 |
| `inheritStorage` | boolean |  | `true` で現在の `context.userStorage` を新しいリンクへ引き継ぎます。 |

## 返り値

成功時は次のフィールドを持つオブジェクトが返ります。

| フィールド | 説明 |
| --- | --- |
| `id` | ワンショットリンクの識別子。 |
| `url` | 参加者に共有する完全URL（例: `https://goemon.cloud/t/XXXX?oneshot=YYYY`）。 |
| `expiresAt` | ミリ秒単位の有効期限タイムスタンプ。 |
| `metadata` | 発行時に指定した `metadata`。 |

## 制限と注意点

- ログイン済みユーザーが実行中のタスクでのみ利用できます。匿名タスクやプレビューでは発行できません。
- タスクごと・ユーザーごとに発行できる未失効リンク数には上限があります（既定で20件）。上限に達した場合は古いリンクを失効させてください。
- `context.finish()` でタスクが完了すると、発行済みリンクは自動的に失効します。途中離脱や `context.abort()` の場合は再入場の可否を運用で判断してください。
- リンクを開いたブラウザは oneshot セッションとして扱われ、完了までは同じURLで再入場できます。
- 発行元のタスクからは `context.oneshot.metadata` を参照することで配布時に添付した情報を受け取れます。

## 例

```javascript
context.getOneshotURL({
  label: 'Day2',
  expiresInMinutes: 60 * 24,
  metadata: { participantId: participant.id }
}).then((link) => {
  context.messaging.send({
    subject: '明日の測定用リンク',
    body: `以下のURLから再開してください。\n${link.url}`,
    to: participant.email
  });
}).catch((error) => {
  context.log('Oneshot URLの発行に失敗しました', { error: error.message });
});
```

発行済みのリンクはタスク内の別のリクエストからも再取得できます。oneshot セッション内で再度 `context.getOneshotURL` を呼び出すと、新しいリンクを連鎖的に発行できます。
