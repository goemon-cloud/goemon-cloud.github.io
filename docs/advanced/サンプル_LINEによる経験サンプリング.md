---
layout: default
parent: 高度な機能
nav_order: 21

title: "サンプル: LINEによる経験サンプリング"
created: 2024-04-25T18:44:18Z
updated: 2025-07-30T07:17:01Z
id: "662a25ee63d8c900251d07df"
views: 41
links: ["チュートリアル1:_簡単なアンケート", "javascript"]
---

# サンプル: LINEによる経験サンプリング

サンプル: LINEによる経験サンプリング
GO-E-MONはLINE連携機能をサポートするため、LINEを使った経験サンプリングが可能です。このサンプルを利用すると、LINEでのやり取りで得られた回答を収集することができます。

![](/images/662a26f614655a00242da018.png)

このタスクは、以下の論文で紹介されている Ecological Momentary Assessment (EMA) をGO-E-MON + LINEでやってみるテストです。

Hur J, Kuhn M, Grogans SE, Anderson AS, Islam S, Kim HC, Tillman RM, Fox AS, Smith JF, DeYoung KA, Shackman AJ. Anxiety-Related Frontocortical Activity Is Associated With Dampened Stressor Reactivity in the Real World. <https://pubmed.ncbi.nlm.nih.gov/35657777/> Psychol Sci. 2022 Jun;33(6):906-924.


# タスクの作成
[チュートリアル1:_簡単なアンケート](チュートリアル1_簡単なアンケート.html) を参考に、新規にタスクを作成し、適当なタスク名を設定してください。

# コードの記述
タスクとして実行する [JavaScript](../reference/JavaScript.html) コードを記述します。ここでは、以下のような簡単なアンケートを実装してみます。

```javascript
  // このタスクのURL
  const window = context.getGlobal('window');
  const goemonUrl = window.location.origin + window.location.pathname;
  console.log('GO-E-MON URL', goemonUrl);
  const taskUrl = goemonUrl + '?_talklogin=line';
  
  // 画面初期化
  initUI();
  printDebugInformation();
  
  // メッセージ定義
  const paMessage = {
    type: 'text',
    text: '現在の肯定的感情（陽気、満足、熱狂、喜び、リラックス、穏やか）を5段階で評価してください。',
    // 参考: https://developers.line.biz/ja/reference/messaging-api/#quick-reply
    quickReply: {
      items: [
        {
          type: 'action',
          action: {
            type: 'message',
            label: '全くあてはまらない',
            text: '全くあてはまらない(PA:0)',
          },
        },
        {
          type: 'action',
          action: {
            type: 'message',
            label: 'あてはまらない',
            text: 'あてはまらない(PA:1)',
          },
        },
        {
          type: 'action',
          action: {
            type: 'message',
            label: 'どちらとも言えない',
            text: 'どちらとも言えない(PA:2)',
          },
        },
        {
          type: 'action',
          action: {
            type: 'message',
            label: 'あてはまる',
            text: 'あてはまる(PA:3)',
          },
        },
        {
          type: 'action',
          action: {
            type: 'message',
            label: '非常にあてはまる',
            text: '非常にあてはまる(PA:4)',
          },
        },
      ],
    },
  };
  const naMessage = {
    type: 'text',
    text: '現在の否定的感情（恐怖、緊張、不安、絶望、悲しみ）を5段階で評価してください。',
    // 参考: https://developers.line.biz/ja/reference/messaging-api/#quick-reply
    quickReply: {
      items: [
        {
          type: 'action',
          action: {
            type: 'message',
            label: '全くあてはまらない',
            text: '全くあてはまらない(NA:0)',
          },
        },
        {
          type: 'action',
          action: {
            type: 'message',
            label: 'あてはまらない',
            text: 'あてはまらない(NA:1)',
          },
        },
        {
          type: 'action',
          action: {
            type: 'message',
            label: 'どちらとも言えない',
            text: 'どちらとも言えない(NA:2)',
          },
        },
        {
          type: 'action',
          action: {
            type: 'message',
            label: 'あてはまる',
            text: 'あてはまる(NA:3)',
          },
        },
        {
          type: 'action',
          action: {
            type: 'message',
            label: '非常にあてはまる',
            text: '非常にあてはまる(NA:4)',
          },
        },
      ],
    },
  };
  const stressorMessage = {
    type: 'text',
    text: '過去1時間に1つ以上の否定的な出来事を経験しましたか？',
    // 参考: https://developers.line.biz/ja/reference/messaging-api/#quick-reply
    quickReply: {
      items: [
        {
          type: 'action',
          action: {
            type: 'message',
            label: 'なかった',
            text: 'なかった(ST:0)',
          },
        },
        {
          type: 'action',
          action: {
            type: 'message',
            label: 'あった',
            text: 'あった(ST:1)',
          },
        },
      ],
    },
  };
  const pstressorMessage = {
    type: 'text',
    text: '過去1時間に1つ以上の肯定的な出来事を経験しましたか？',
    // 参考: https://developers.line.biz/ja/reference/messaging-api/#quick-reply
    quickReply: {
      items: [
        {
          type: 'action',
          action: {
            type: 'message',
            label: 'なかった',
            text: 'なかった(PT:0)',
          },
        },
        {
          type: 'action',
          action: {
            type: 'message',
            label: 'あった',
            text: 'あった(PT:1)',
          },
        },
      ],
    },
  };
  
  function printDebugInformation() {
    console.log('History', context.userStorage.getItem('history'));
    
    context.messaging.getLastResult(function(result, error) {
      if (error) {
        console.error('最終実行結果が取得できませんでした。', error);
        return;
      }
      if (!result) {
        console.log('実行された記録はありません。');
      } else {
        console.log('最後の実行結果', result);
      }
      requestLINEAccount();
    });
  }
  
  function initUI() {
    context.root.append($('<div></div>')
      .attr('id', 'alert').hide().css('color', 'red').css('font-weight', 'bold'));
    context.root.append($('<div></div>')
      .attr('id', 'status')
      .text('LINEアカウントとGO-E-MONアカウントの連携をおこなっています...'));
  }
  
  function sendMessage(callback) {
    context.messaging.send(paMessage, callback);
  }
  
  function requestLINEAccount() {
    context.messaging.request({
      type: 'line'
    }, function(result, error) {
      if (error) {
        $('#alert').text('不明なエラーが発生しました: ' + error).show();
        console.error('不明なエラーが発生しました。', error);
        return;
      }
      if (!result) {
        $('#status').text('LINEアカウントとGO-E-MONアカウントの連携がキャンセルされました。');
        return;
      }
      const history = context.userStorage.getItem('history') || [];
      $('#status').text('')
        .append($('<div></div>').text('LINEアカウントとGO-E-MONアカウントの連携が成功しました。'))
        .append($('<div></div>').text('このタスクはLINEで定期的にアンケートを送信します。回答してみてください。'))
        .append($('<button></button>').text('試しにアンケートを送信！').click(function(event) {
          $(event.target).attr('disabled', true);
          sendMessage(function() {
            $(event.target).attr('disabled', false);
          });
        }))
        .append($('<div></div>').css('text-align', 'left').css('margin-top', '2em').css('border', '1px solid #444').append($('<pre></pre>').text('-- 回答履歴(デバッグ用) --:\n' + JSON.stringify(history, null, '\t'))));
      // メッセージ処理用のスクリプトを生成する。以下は `` (バッククォート)で囲まれているため、文字列リテラルとして評価される。
      var script = `
        const pa = extractPAReply(source);
        const na = extractNAReply(source);
        const stressor = extractStressorReply(source);
        const pstressor = extractPStressorReply(source);
  
        if (pa !== null) {
            context.userStorage.setItem('last.positive', { time: Date.now(), value: pa });
            context.messaging.send(${JSON.stringify(naMessage)});
        } else if (na !== null) {
            context.userStorage.setItem('last.negative', { time: Date.now(), value: na });
            context.messaging.send(${JSON.stringify(pstressorMessage)});
        } else if (pstressor !== null) {
            context.userStorage.setItem('last.pstressor', { time: Date.now(), value: pstressor });
            context.messaging.send(${JSON.stringify(stressorMessage)});
        } else if (stressor !== null) {
            context.userStorage.setItem('last.stressor', { time: Date.now(), value: stressor });
            recordLog();
            context.messaging.send({ type: 'text', text: 'ありがとうございます！回答経過はタスク画面で確認可能です(テスト用)\\n${taskUrl}' });
        } else {
            context.messaging.send(${JSON.stringify(paMessage)});
        }
  
        function extractPAReply(source) {
            return extractReply(source, /.+PA:([0-9]+).+/);
        }
        function extractNAReply(source) {
            return extractReply(source, /.+NA:([0-9]+).+/);
        }
        function extractStressorReply(source) {
            return extractReply(source, /.+ST:([0-9]+).+/);
        }
        function extractPStressorReply(source) {
            return extractReply(source, /.+PT:([0-9]+).+/);
        }
        function extractReply(source, regexp) {
            if (!source || !source.message || !source.message.text) {
                return null;
            }
            const m = source.message.text.match(regexp);
            if (!m) {
                return null;
            }
            return parseInt(m[1]);
        }
        function recordLog() {
            const positive = context.userStorage.getItem("last.positive");
            const negative = context.userStorage.getItem("last.negative");
            const stressor = context.userStorage.getItem("last.stressor");
            const pstressor = context.userStorage.getItem("last.pstressor");
            context.userStorage.removeItem("last.positive");
            context.userStorage.removeItem("last.negative");
            context.userStorage.removeItem("last.stressor");
            context.userStorage.removeItem("last.pstressor");
            const history = context.userStorage.getItem("history") || [];
            const item = { positive: positive, negative: negative, stressor: stressor, pstressor: pstressor };
            history.push(item);
            context.userStorage.setItem("history", history)
            context.log("アンケートに回答しました。", item)
        }
  `;
      // どのようなコードが定期実行されるかは、コードを実行して「デバッグ」タブを参照してください。
      console.log("定期実行コード:", script);
      // 3時間おきに実施
      context.messaging.setSchedule({
        schedule: '0 7-21/3 * * *',
        messageToPDS: true,
        script: script,
      });
    });
  }

```
このプログラムは以下の要素から構成されます。

1. UIの初期化:「initUI」関数により、アラート用の領域とステータス用の領域が作成されます。
2. メッセージの送信:「sendMessage」関数により、設定したメッセージがLINEから送信されます。
3. LINEアカウントの要求:「requestLINEAccount」関数では、LINEとの連携を行います。連携成功後には、「history」に保存された履歴などを表示します。
4. スクリプトの設定:LINEへのアンケート回答の取得や保存、及び固定時間にアンケートを送るためのスケジュール設定が行われます。

送信間隔は schedule のパラメータで指定されます。ここでは '0 7-21/3 * * *' と設定しているため、7時から21時までの間、3時間おきに毎時0分にメッセージ処理が実施されます。このパラメータには crontab のフォーマットが使われます(参考: <https://crontab.guru/> )。このフォーマットでは 5つのフィールド (分、時、日、月、曜日) を設定でき、それぞれのフィールドは '*' (任意の値)、'-' (範囲)、',' (列挙)、'/' (ステップ) を使って表現することができます。
また、scriptには定期処理と、メッセージに対する応答を行うスクリプトを文字列で指定することができます。メッセージ応答の場合は、スクリプト呼び出し時のsource変数にメッセージが格納されます。source.messageはLINE Messaging APIのメッセージイベント <https://developers.line.biz/ja/reference/messaging-api/#message-event> に準拠します。定期処理の場合はsourceがnullとなります。
この例では、ユーザーが送信したメッセージ文字列を解析し、その回答によって次の質問を出すようなロジックを記述しています。scriptを生成するscriptを記述しているため、非常に読みづらいですが、この例では以下のようなスクリプトを生成し、定期実行するように指示しています。

```javascript
     const pa = extractPAReply(source);
     const na = extractNAReply(source);
     const stressor = extractStressorReply(source);
     const pstressor = extractPStressorReply(source);
     if (pa !== null) {
         context.userStorage.setItem('last.positive', { time: Date.now(), value: pa });
         context.messaging.send({"type":"text","text":"現在の否定的感情（恐怖、緊張、不安、絶望、悲しみ）を5段階で評価してください。","quickReply":{"items":[{"type":"action","action":{"type":"message","label":"全くあてはまらない","text":"全くあてはまらない(NA:0)"}},{"type":"action","action":{"type":"message","label":"あてはまらない","text":"あてはまらない(NA:1)"}},{"type":"action","action":{"type":"message","label":"どちらとも言えない","text":"どちらとも言えない(NA:2)"}},{"type":"action","action":{"type":"message","label":"あてはまる","text":"あてはまる(NA:3)"}},{"type":"action","action":{"type":"message","label":"非常にあてはまる","text":"非常にあてはまる(NA:4)"}}]}});
     } else if (na !== null) {
         context.userStorage.setItem('last.negative', { time: Date.now(), value: na });
         context.messaging.send({"type":"text","text":"過去1時間に1つ以上の肯定的な出来事を経験しましたか？","quickReply":{"items":[{"type":"action","action":{"type":"message","label":"なかった","text":"なかった(PT:0)"}},{"type":"action","action":{"type":"message","label":"あった","text":"あった(PT:1)"}}]}});
     } else if (pstressor !== null) {
         context.userStorage.setItem('last.pstressor', { time: Date.now(), value: pstressor });
         context.messaging.send({"type":"text","text":"過去1時間に1つ以上の否定的な出来事を経験しましたか？","quickReply":{"items":[{"type":"action","action":{"type":"message","label":"なかった","text":"なかった(ST:0)"}},{"type":"action","action":{"type":"message","label":"あった","text":"あった(ST:1)"}}]}});
     } else if (stressor !== null) {
         context.userStorage.setItem('last.stressor', { time: Date.now(), value: stressor });
         recordLog();
         context.messaging.send({ type: 'text', text: 'ありがとうございます！回答経過はタスク画面で確認可能です(開発中)\nhttps://goemon.cloud/t/bHOuo9KvUkyI0HzwiqPg?_talklogin=line' });
     } else {
         context.messaging.send({"type":"text","text":"現在の肯定的感情（陽気、満足、熱狂、喜び、リラックス、穏やか）を5段階で評価してください。","quickReply":{"items":[{"type":"action","action":{"type":"message","label":"全くあてはまらない","text":"全くあてはまらない(PA:0)"}},{"type":"action","action":{"type":"message","label":"あてはまらない","text":"あてはまらない(PA:1)"}},{"type":"action","action":{"type":"message","label":"どちらとも言えない","text":"どちらとも言えない(PA:2)"}},{"type":"action","action":{"type":"message","label":"あてはまる","text":"あてはまる(PA:3)"}},{"type":"action","action":{"type":"message","label":"非常にあてはまる","text":"非常にあてはまる(PA:4)"}}]}});
     }
     function extractPAReply(source) {
         return extractReply(source, /.+PA:([0-9]+).+/);
     }
     function extractNAReply(source) {
         return extractReply(source, /.+NA:([0-9]+).+/);
     }
     function extractStressorReply(source) {
         return extractReply(source, /.+ST:([0-9]+).+/);
     }
     function extractPStressorReply(source) {
         return extractReply(source, /.+PT:([0-9]+).+/);
     }
     function extractReply(source, regexp) {
         if (!source || !source.message || !source.message.text) { return null; }
         const m = source.message.text.match(regexp);
         if (!m) { return null; }
         return parseInt(m[1]);
     }
     function recordLog() {
         const positive = context.userStorage.getItem("last.positive");
         const negative = context.userStorage.getItem("last.negative");
         const stressor = context.userStorage.getItem("last.stressor");
         const pstressor = context.userStorage.getItem("last.pstressor");
         context.userStorage.removeItem("last.positive");
         context.userStorage.removeItem("last.negative");
         context.userStorage.removeItem("last.stressor");
         context.userStorage.removeItem("last.pstressor");
         const history = context.userStorage.getItem("history") || [];
         const item = { positive: positive, negative: negative, stressor: stressor, pstressor: pstressor };
         history.push(item);
         context.userStorage.setItem("history", history) context.log("アンケートに回答しました。", item)
     }

```
# 実行
コードを記述したら、「はじめる」をクリックして実行してみましょう。

実行すると、LINEの友だち登録用のQRコードが表示されますので、LINEでGO-E-MONを友だち登録してください。
![](/images/662a28f551d4f70024c04fbb.png)

友だち登録すると、LINEに登録用のコードが送信されますので、上の画面の「次へ」をクリックして、そのコードを入力してください。
![](/images/662a296141c0bc0024ee5e49.png)

この登録を行うと、タスクの実行画面に、 **このタスクはLINEで定期的にアンケートを送信します。回答してみてください。** というボタンが表示されますので、これをクリックしてください。
すると、LINEにメッセージが表示されます。このアンケートに回答すると、結果がPersonaryに送信されます。
また、タスクの実行画面をリロードすると、最後に回答した内容が表示されます。

# 配備
[チュートリアル1:_簡単なアンケート](チュートリアル1_簡単なアンケート.html) を参考に、タスクの配備を実施してください。設定されたURLを配布することで、他の人に試してもらうことができます。

