---
title: "context.userStorageプロパティ"
created: 2022-06-21T15:28:25Z
updated: 2022-06-21T15:32:40Z
id: "62b165060b1139001d0db7ce"
views: 24
---

# context.userStorageプロパティ

context.userStorageプロパティ
GO-E-MONでは、実施中のユーザごとにキー-値の形式で情報を保存することができます。
context.userStorage.setItem(key, value)メソッドを使用することで、キー文字列に対して値を設定し、context.userStorage.getItem(key)メソッドを使用することで、キー文字列に対する値を取得することができます。
context.userStorageはStorageオブジェクト https://developer.mozilla.org/en-US/docs/Web/API/Storage に準拠します。
