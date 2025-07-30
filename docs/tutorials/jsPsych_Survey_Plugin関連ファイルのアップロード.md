---
layout: default
parent: チュートリアル
nav_order: 11

title: "jsPsych Survey Plugin関連ファイルのアップロード"
created: 2022-10-18T11:22:05Z
updated: 2022-10-18T11:30:41Z
id: "634e0dc391eaeb0021fca286"
views: 56
links: ["チュートリアル2:_jspsychを使ったタスク", "files"]
---

# jsPsych Survey Plugin関連ファイルのアップロード

jsPsych Survey Plugin関連ファイルのアップロード
基本手順は[チュートリアル2: jsPsychを使ったタスク](チュートリアル2_jsPsychを使ったタスク.html)と同様です。アップロードすべきファイルが異なります。


# タスクの作成
GO-E-MONダッシュボード <https://goemon.cloud> にアクセスし、*タスクを作る*をクリックし、*新規タスクの追加* ボタンをクリックします。
![](/images/634dfcb739203500207b9077.png)


# タスク名の設定
newTitleというタスクが作成されますので、タスク名を変更します。タスク名右の編集ボタンをクリックします。
![](/images/60d2633d9ffbb100229f5163.png)
タスク名を入力します。タスク名はENTERキーで確定できます。
![](/images/60ea243109e998001cb82b65.png)

# ライブラリの追加(jsPsych配布パッケージ)
jsPsychを使用するには、jsPsychとして配布されているコードをロードするようにGO-E-MONに指示する必要があります。これは以下の手順で実施します。
- jsPsychのパッケージ(Dist archive)をダウンロードする <https://github.com/jspsych/jsPsych/releases>
- jsPsychのパッケージに含まれるファイルのうち、必要なものをGO-E-MONのファイル([Files](../reference/Files.html))タブにアップロードする
- アップロードしたファイルの読み込み優先度を変更する

jsPsych Survey Pluginを利用するためには、jsPsychのパッケージに含まれるファイルのうち、以下のファイルをアップロードします。
- dist/jspsych.css
- dist/jspsych.js
- dist/plugin-survey.js

これらのファイルをファイル([Files](../reference/Files.html))タブにドラッグ＆ドロップします。

jsPsychでは、jspsych.jsが他の.jsファイルよりも先に読み込まれる必要があるので、 *優先度* の項目をクリックし、他のファイルよりも大きな値(例えば1000)を設定します。*優先度* は大きい値であれば先に読み込まれます。
![](/images/60ea307425c67900213d5b76.png)

# ライブラリの追加(Survey Plugin用CSS)
Survey Pluginは <https://www.jspsych.org/7.3/plugins/survey/#css> に記載がある通り追加のStyle Sheetファイルを必要とします。そのため、URL <https://unpkg.com/@jspsych/plugin-survey@0.2.1/css/survey.css> からcssファイルをダウンロードし、ファイル([Files](../reference/Files.html))タブにアップロードします。

この解説を一通り実行すると、以下のようなファイルがアップロードされているはずです。
![](/images/634e0fcce1401e0022496e75.png)


---
