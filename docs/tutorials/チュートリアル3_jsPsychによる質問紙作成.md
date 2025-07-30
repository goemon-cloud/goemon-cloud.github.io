---
layout: default
title: "チュートリアル3: jsPsychによる質問紙作成"
parent: チュートリアル
nav_order: 3
---

# チュートリアル3: jsPsychによる質問紙作成

チュートリアル3: jsPsychによる質問紙作成
jsPsychを使うと質問紙を簡単に作成することができます。

# jsPsych Survey Pluginを使う準備
GO-E-MONでjsPsych Survey Pluginを使うためには、以下の**いずれかの**方法でjsPsych Survey Plugin関連ファイルを準備する必要があります。
- <https://goemon.cloud/t/aTzSoAnzDyQw1TOwPrPn> を[タスクのコピー](../basic/タスクのコピー.html)により複製する
または、
- [jsPsych Survey Plugin関連ファイルのアップロード](jsPsych_Survey_Plugin関連ファイルのアップロード.html)を参考に新規タスクを作成し、関連ファイルをアップロードする

# タスク名の設定
タスクの準備をしたら、必要に応じてタスク名を変更します。タスク名右の編集ボタンをクリックします。
![](/images/60d2633d9ffbb100229f5163.png)
タスク名を入力します。タスク名はENTERキーで確定できます。

![](/images/634e172d3dcdc8001d3f3ee0.png)

# コードの記述
タスクとして実行する [JavaScript](../reference/JavaScript.html) コードを記述します。ここでは、Survey Plugin <https://www.jspsych.org/7.3/plugins/survey/> のデモ *Single and multiple item Likert-style scales* 相当のコードを記述します。(jsPsychによるデモ: <https://www.jspsych.org/7.3/demos/jspsych-survey-demo3.html> )

以下は  *Single and multiple item Likert-style scales* の例に対してGO-E-MON用の初期化処理を追加したものです。変更点には **// goemon:** というコメントを記載しています。

> 実施したい質問紙の内容に合わせて変更する とコメントを記載した箇所を変更すると、質問項目を変更することができます。

```javascript
  // goemon: jsPsych関係の関数・オブジェクトをスクリプトで利用できるようにします。
  const initJsPsych = context.getGlobal('initJsPsych');
  // Plugin typeごとに以下を定義
  const jsPsychSurvey = context.getGlobal('jsPsychSurvey');
 
  // goemon: jsPsychの表示領域を作る
  const expRoot = $('<div></div>').attr('id', 'exp_main').css({
    height: '80vh',
  });
  context.root.append(expRoot);
  
  /* initialize jsPsych */
  var jsPsych = initJsPsych({
    // goemon: jsPsych用に準備した表示領域に刺激を表示することを示す
    display_element: 'exp_main',
    // goemon: 結果を送信するため、on_finishハンドラには以下のようなコードを記述する。
    // 出力内容は [デバッグ]タブで確認できる。
    // `context.finish('人間が読める結果サマリ', 保存するデータ)`
    on_finish: function(data) {
      context.finish(`回答を受け付けました`, {
        data: data.values(),
        variables: jsPsych.getAllTimelineVariables(),
      });
    }
  });
  
  /* create timeline */
  var timeline = [];
  
  // Single and multiple item Likert-style scales: https://www.jspsych.org/7.3/demos/jspsych-survey-demo3.html
  // 実施したい質問紙の内容に合わせて変更する: ここから
  const trial = {
    type: jsPsychSurvey,
    pages: [
      [
        {
          type: 'likert',
          prompt: 'I like to eat vegetables.',
          likert_scale_min_label: 'Strongly Disagree',
          likert_scale_max_label: 'Strongly Agree',
          likert_scale_values: [
            {value: 1},
            {value: 2},
            {value: 3},
            {value: 4},
            {value: 5}
          ]
        }, 
        {
          type: 'likert',
          prompt: 'I like to eat fruit.',
          likert_scale_min_label: 'Strongly Disagree',
          likert_scale_max_label: 'Strongly Agree',
          likert_scale_values: [
            {value: 1},
            {value: 2},
            {value: 3},
            {value: 4},
            {value: 5}
          ]
        },
        {
          type: 'likert',
          prompt: 'I like to eat meat.',
          likert_scale_min_label: 'Strongly Disagree',
          likert_scale_max_label: 'Strongly Agree',
          likert_scale_values: [
            {value: 1},
            {value: 2},
            {value: 3},
            {value: 4},
            {value: 5}
          ]
        },  
      ],
      [
        {
          type: 'likert-table',
          prompt: ' ',
          statements: [
            {prompt: 'I like to eat vegetables', name: 'VeggiesTable'},
            {prompt: 'I like to eat fruit', name: 'FruitTable'},
            {prompt: 'I like to eat meat', name: 'MeatTable'},
          ],
          options: ['Strongly Disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly Agree'],
        }
      ]
    ],
  };
  // 実施したい質問紙の内容に合わせて変更する: ここまで
  timeline.push(trial);
 
  // goemon: 上部メニューを隠す
  context.appMenu.hide();
  jsPsych.run(timeline);

```
## コードの実行
コードを記述したら、実行してみましょう。

![](/images/6350af739d777b001dc570ec.png)

GO-E-MONのエディタが邪魔で*はじめる*ボタンが見えない場合は、*閉じる* ボタンを押してみてください。
![](/images/60eaa745029d5c001e8cfe86.png)


*はじめる*をクリックするとタスクが開始されます。実行画面は以下のようになります。

![](/images/6350afc8fb7191001d5735ce.png)



## コードの動作確認
タスクを最後まで実施したら、どのようなログが送信されたか確認してみましょう。*デバッグ*タブから確認することができます。

![](/images/60eaa91adc695d001ec4f5b4.png)


送信されたログは *スクリプトを終了しました* ログから内容を確認できます。
また、スクリプトの誤りなどでエラーが発生した場合は、デバッグタブから警告・エラーを確認することができます。

# 説明文の設定
説明文にはタスクの説明を記述することができます。*説明文* タブに以下の文字列を記述します。説明文の記述には[Markdown](../reference/Markdown.html)を使用することができます。

```markdown
 [jsPsych](https://www.jspsych.org/)のSurvey Pluginを
 GO-E-MONで実行する例です。
 
 [チュートリアル3: jsPsychによる質問紙作成](https://scrapbox.io/cogtask-me/%E3%83%81%E3%83%A5%E3%83%BC%E3%83%88%E3%83%AA%E3%82%A2%E3%83%AB3:_jsPsych%E3%81%AB%E3%82%88%E3%82%8B%E8%B3%AA%E5%95%8F%E7%B4%99%E4%BD%9C%E6%88%90)で紹介しているサンプルです。
  
 紹介文はMarkdownで記述することができます。**太字**や*斜体*などをテキストにより記述することができます。

```
すると、開始時の画面に以下のように説明文を表示することができます。あらかじめ実施に必要な注意事項などを記載するのに利用してください。

![](/images/634e16c0b97d14001da6eced.png)

# 配備
以上でタスクに必要な情報は定義できました。
ただし、このままではタスク作成者しか試すことはできません。作成したタスクを他のユーザからも参照できるようにすることを*配備*と呼びます。

*配備*タブの*配備*ボタンを押すことで、タスク作成者以外のユーザが最新のタスクを試すことができるようになります。
![](/images/60eaa9e96c34da001c027802.png)

*配備*を実施したら、タスクへの参加 に記載されているURLか、QRコードをユーザーに配布してください。これにより、ユーザーはこのタスクを実施することができるようになります。

> タスクのJavaScriptや説明文を変更したあとは、必ず配備ボタンを押して他のユーザーにも最新版を参照できるようにする必要があります。


# 実施確認
タスクがユーザーにより実施されると、タスク提供者のPersonaryの `cog-pds-log` チャネルに実施記録が格納されます。Personaryを自身のアカウントと紐付けていると、以下のように実施記録が送信されます。Personaryのデータ分析については[Personaryデータの分析](../basic/Personaryデータの分析.html)を参照してください。
![](/images/personary-channel.png)
