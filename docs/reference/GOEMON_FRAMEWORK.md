---
layout: default
parent: Param
grand_parent: リファレンス
nav_order: 1

title: "GOEMON_FRAMEWORK"
created: 2025-07-30T10:00:00Z
updated: 2025-07-30T10:00:00Z
id: "goemon-framework"
views: 0
links: ["Param", "チュートリアル2_jsPsychを使ったタスク"]
---

# GOEMON_FRAMEWORK

タスクで使用するフレームワークを指定するパラメータです。

## 設定値

- **型**: Object
- **設定方法**: 設定タブのGUIから選択
- **デフォルト値**: なし

## 説明

GOEMON_FRAMEWORKパラメータを使用することで、jsPsychなどの外部フレームワークをタスクに組み込むことができます。設定タブで「+追加」ボタンをクリックし、設定名ドロップダウンから「GOEMON_FRAMEWORK」を選択すると、専用の設定ダイアログが表示されます。

### 設定可能な項目

- **フレームワーク**: 使用するフレームワークの種類（例：jsPsych）
- **バージョン**: フレームワークのバージョン
- **プラグイン**: 有効にするプラグインのリスト（フレームワークによって異なる）

### jsPsychの場合

jsPsychを選択した場合、以下のようなプラグインを個別に有効化できます：

- Preload Plugin
- HTML Keyboard Response Plugin
- Image Keyboard Response Plugin
- その他多数のプラグイン

## 関連項目

- [チュートリアル2: jsPsychを使ったタスク](../tutorials/チュートリアル2_jsPsychを使ったタスク.html) - GOEMON_FRAMEWORKの具体的な設定方法