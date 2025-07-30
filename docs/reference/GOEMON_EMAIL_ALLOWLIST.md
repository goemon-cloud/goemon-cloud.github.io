---
layout: default
parent: Param
grand_parent: リファレンス
nav_order: 4

title: "GOEMON_EMAIL_ALLOWLIST"
created: 2025-07-30T10:00:00Z
updated: 2025-07-30T10:00:00Z
id: "goemon-email-allowlist"
views: 0
links: ["Param"]
---

# GOEMON_EMAIL_ALLOWLIST

ユーザをEメールアドレスにより制限する場合に定義するパラメータです。

## 設定値

- **型**: String (セミコロン区切り)
- **形式**: `@hogehoge.com;@fugafuga.com` のようなセミコロン区切り文字列
- **デフォルト値**: なし

## 説明

Eメールアドレスのドメインをセミコロン区切り文字列として与えると、そのドメイン外のユーザに対しては再ログインするよう促すメッセージが表示されます。

例：`@university.ac.jp;@research.org`と設定した場合、これらのドメインのメールアドレスを持つユーザのみがタスクを実行できます。