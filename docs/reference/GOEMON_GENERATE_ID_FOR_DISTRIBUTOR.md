---
layout: default
parent: Param
grand_parent: リファレンス
nav_order: 1

title: "GOEMON_GENERATE_ID_FOR_DISTRIBUTOR"
created: 2025-07-30T10:00:00Z
updated: 2025-07-30T10:00:00Z
id: "goemon-generate-id-for-distributor"
views: 0
links: ["Param", "context.pseudonymUserIdプロパティ"]
---

# GOEMON_GENERATE_ID_FOR_DISTRIBUTOR

仮名IDの識別可能範囲を配信者内に拡張するパラメータです。

## 設定値

- **型**: Boolean
- **値**: `true` または `false`
- **デフォルト値**: `false`

## 説明

デフォルトではタスク内でのみ仮名IDでユーザを識別することができます。つまり、同じ実験参加者でも、異なるタスクの間では異なる仮名IDが振られます。

このパラメータに`true`を指定することで、pseudonymUserIdが配信者内で識別可能になります。これにより、同じ配信者（実験実施者）の異なるタスク間で同一ユーザを追跡できるようになります。

## 関連項目

- [context.pseudonymUserIdプロパティ](context.pseudonymUserIdプロパティ.html) - 仮名IDの詳細な動作について