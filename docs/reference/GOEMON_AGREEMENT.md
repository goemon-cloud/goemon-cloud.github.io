---
layout: default
parent: Param
grand_parent: リファレンス
nav_order: 6

title: "GOEMON_AGREEMENT"
created: 2025-08-26T10:00:00Z
updated: 2025-08-26T10:00:00Z
id: "goemon-agreement"
views: 0
links: ["Param"]
---

# GOEMON_AGREEMENT

タスク実行前に参加者の同意を取得するためのパラメータです。

## 設定値

- **型**: Object (JSON)
- **設定方法**: 設定タブでJSON形式またはGUIエディタから設定
- **デフォルト値**: なし

## 説明

GOEMON_AGREEMENTパラメータを使用することで、研究倫理に基づく同意書や実験参加への同意を電子的に取得できます。参加者はタスクを開始する前に、設定された同意プロセスを完了する必要があります。

### 設定方法の解説動画

<iframe width="560" height="315" src="https://www.youtube.com/embed/F4_b3zIHI3I" title="GOEMON_AGREEMENT設定方法" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 基本構造

```json
{
  "title": "同意書タイトル",
  "description": "同意書本文（Markdown形式）",
  "required": true
}
```

### 設定可能な項目

| フィールド | 型 | 必須 | 説明 |
|---------|---|-----|------|
| `title` | string | ✓ | 同意書のタイトル |
| `description` | string | ✓ | 同意書の本文（Markdown形式対応） |
| `required` | boolean | - | 同意が必須かどうか（デフォルト: true） |
| `requirements` | array | - | 追加の同意ステップ |

### 複数ステップの同意（requirements）

より詳細な同意プロセスが必要な場合、以下の3種類のステップを設定できます：

#### 1. ビデオ視聴 (type: "video")
```json
{
  "id": "video-1",
  "title": "説明ビデオ",
  "type": "video",
  "src": "explanation.mp4"
}
```

#### 2. PDF閲覧 (type: "pdf")
```json
{
  "id": "document-1",
  "title": "倫理審査書類",
  "type": "pdf",
  "src": "ethics.pdf"
}
```

#### 3. 電子署名 (type: "sign")
```json
{
  "id": "signature-1",
  "title": "同意書への署名",
  "type": "sign",
  "subjects": ["参加者"]
}
```

## 使用例

### シンプルな同意書（署名付き）

```json
{
  "title": "実験参加への同意",
  "description": "本実験は約30分程度かかります。\n\n実験中は集中できる環境で参加してください。",
  "required": true,
  "requirements": [
    {
      "id": "consent-sign",
      "title": "同意書への署名",
      "type": "sign",
      "subjects": ["参加者"]
    }
  ]
}
```

### 複数ステップの同意書

```json
{
  "title": "研究参加への同意",
  "description": "研究内容の説明",
  "required": true,
  "requirements": [
    {
      "id": "video-explanation",
      "title": "説明ビデオ",
      "type": "video",
      "src": "explanation.mp4"
    },
    {
      "id": "consent-sign",
      "title": "同意書への署名",
      "type": "sign",
      "subjects": ["参加者"]
    }
  ]
}
```