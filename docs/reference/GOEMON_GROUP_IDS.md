---
layout: default
parent: Param
grand_parent: リファレンス
nav_order: 4

title: "GOEMON_GROUP_IDS"
created: 2025-07-30T10:00:00Z
updated: 2025-07-30T10:00:00Z
id: "goemon-group-ids"
views: 0
links: ["Param", "context.groupIdプロパティ"]
---

# GOEMON_GROUP_IDS

実験群を分ける場合などに定義するパラメータです。

## 設定値

- **型**: String (カンマ区切り)
- **形式**: `A,B,C` のようなカンマ区切り文字列
- **デフォルト値**: なし

## 説明

群ラベルをカンマ区切り文字列として与えると、ユーザに対してこれらのラベル数ができるだけ均等になるように割り振ります。割り振られたグループIDはスクリプトから`context.groupId`で参照できます。

例：`control,experiment1,experiment2`と設定した場合、ユーザは3つのグループのいずれかに自動的に割り振られます。

## 関連項目

- [context.groupIdプロパティ](context.groupIdプロパティ.html) - グループIDの参照方法について