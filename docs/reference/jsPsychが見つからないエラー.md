---
layout: default
parent: リファレンス
nav_order: 23

title: "jsPsychが見つからないエラー"
created: 2021-06-16T13:55:21Z
updated: 2021-06-16T13:55:30Z
id: "60c984365c3ea20022c4db30"
views: 45
---

# jsPsychが見つからないエラー

jsPsychが見つからないエラー
jsPsychの場合は、 jspsych.js が他のファイル(プラグイン等)よりも先に読み込まれる必要があります。そのため、jspsych.jsの優先度の値(数値)を、他よりも大きい値に設定してください。

![](/images/60c984132531b8001c2dba24.png)


