---
layout: default
parent: contextオブジェクト
grand_parent: リファレンス
nav_order: 1

title: "context.groupIdプロパティ"
created: 2022-03-25T15:22:52Z
updated: 2022-03-25T15:27:14Z
id: "623d5fa28c86be0023b45f8f"
views: 29
links: ["param"]
---

# context.groupIdプロパティ

context.groupIdプロパティ
GO-E-MONでは、設定タブ [Param](Param.html) に GOEMON_GROUP_IDSを指定することで、各ユーザにグループを示すラベルを設定することができます。
GOEMON_GROUP_IDSに *A,B,C* などと群ラベルをカンマ区切り文字列として与えると、ユーザに対してこれらのラベル数ができるだけ均等になるように割り振ります。設定されたラベルは context.groupId プロパティで取得できます。
また、Personaryへ送信されるデータ中には cogPDSGroup プロパティとしてこの値が格納されます。

> タスクへのアクセスがあった順番に各ラベルを振っていきます。同時アクセスが発生した場合は各ラベルの数が前後する可能性があります。



---
