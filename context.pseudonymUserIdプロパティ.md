---
title: "context.pseudonymUserIdプロパティ"
created: 2022-03-01T17:46:10Z
updated: 2022-03-01T17:46:13Z
id: "621ddd4e813672001d8d90c9"
views: 20
links: ["設定タブ"]
---

# context.pseudonymUserIdプロパティ

context.pseudonymUserIdプロパティ
実行中のユーザの仮名IDを格納したオブジェクトです。以下のように参照することができます。

```JavaScript
 const userId = context.pseudonymUserId;

```
仮名IDはタスクまたは配信者(実験実施者)内で識別可能です。デフォルトではタスク内でのみ仮名IDでユーザを識別することができます。つまり、同じ実験参加者でも、異なるタスクの間では異なる仮名IDが振られます。これにより、実験参加者は意図せず名寄せされる不安から解放されます。
なお、タスク開発の自由度を考慮し、配信者内で識別可能なIDを振ることも可能です。[設定タブ](設定タブ.md) で GOEMON_GENERATE_ID_FOR_DISTRIBUTOR に true を指定することで、pseudonymUserIdが配信者内で識別可能になります。

---

← 戻る: [contextオブジェクト](contextオブジェクト.md) | [Param](Param.md) | [タスクを他のユーザが配信できるようにする](タスクを他のユーザが配信できるようにする.md)