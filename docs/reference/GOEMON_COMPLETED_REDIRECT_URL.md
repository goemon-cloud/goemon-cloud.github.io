---
layout: default
parent: Param
grand_parent: リファレンス
nav_order: 7

title: "GOEMON_COMPLETED_REDIRECT_URL"
created: 2025-09-17T00:00:00Z
updated: 2025-09-17T00:00:00Z
id: "goemon-completed-redirect-url"
views: 0
links: ["Param"]
---

# GOEMON_COMPLETED_REDIRECT_URL

タスク完了後に参加者を別のページへリダイレクトするためのパラメータです。

## 設定値

- **型**: Object (JSON)
- **設定方法**: 設定タブでGUIフォームから入力
- **デフォルト値**: なし

## 説明

タスク完了後、参加者をGoogle Formなどの外部URLへ誘導できます。URLにはユーザIDやグループIDなどのプレースホルダーを含めることができ、自動的に置換されます。

### 設定方法の解説動画

<iframe width="560" height="315" src="https://www.youtube.com/embed/oOiS9gcX5SY" title="GOEMON_COMPLETED_REDIRECT_URL設定方法" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## 基本構造

```json
{
  "url": "https://example.com/form?id={USER_ID}",
  "text": "アンケートに進む",
  "force": false
}
```

| フィールド | 説明 |
|---------|------|
| `url` | リダイレクト先URL（必須） |
| `text` | ボタンテキスト（デフォルト: "アンケートに進む"） |
| `force` | 自動リダイレクト（デフォルト: false） |

## 利用可能なプレースホルダー

- `{USER_ID}` - 匿名化されたユーザーID
- `{GROUP_ID}` - グループID
- `{TASK_ID}` - タスクID
- `{SEARCH_(name)}` - URLクエリパラメータ

## 使用例

```json
{
  "url": "https://docs.google.com/forms/d/e/XXX/viewform?entry.123={USER_ID}&entry.456={GROUP_ID}",
  "text": "事後アンケート",
  "force": true
}
```