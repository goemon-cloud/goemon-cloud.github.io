---
layout: default
parent: Param
grand_parent: リファレンス
nav_order: 3

title: "GOEMON_AUTO_START"
created: 2025-07-30T10:00:00Z
updated: 2025-07-30T10:00:00Z
id: "goemon-auto-start"
views: 0
links: ["Param"]
---

# GOEMON_AUTO_START

一度実行したタスクを自動的に開始するように設定できる真偽値パラメータです。

## 設定値

- **型**: Boolean
- **値**: `true` または `false`
- **デフォルト値**: `false`

## 説明

このパラメータが`true`に設定されている場合、ユーザが以前にタスクを実行したことがあれば、次回アクセス時に自動的にタスクが開始されます。ユーザがタスク開始ボタンをクリックする手間を省くことができます。