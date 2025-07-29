---
title: "終了時のoptionsパラメータ"
created: 2022-03-01T11:08:54Z
updated: 2025-07-09T07:29:58Z
id: "621d8033c8881d001dc6a6d0"
views: 32
---

# 終了時のoptionsパラメータ

終了時のoptionsパラメータ
optionsパラメータにはキー - 値形式の値が指定可能です。

```JavaScript
 context.finish("タスクの点数は 50 点です。", {score: 50}, {
   next: {
     url: 'https://goemon.cloud',
     text: '次のページに移動',
   },
 });

```
optionsパラメータには以下のキーを指定することができます。

## next
タスク終了後のリンク先を指定することができます。値には以下のキーを含めることができます。
 **url (必須)**: リンク先のURL。?key1=value1&key2=value2&...
 **text**: 終了時のリンクボタンに与える文字列。省略した場合は「OK」とする。forceにtrueが指定された場合は無視される。
 **force**:終了後即時にリンク先へと移動する場合はtrueとする。
 **@context**: JSON-LDの名前空間を追加定義する。 "@context": { "jspsych": "https://goemon.cloud/ns/jspsych#" } のような形で定義可能
