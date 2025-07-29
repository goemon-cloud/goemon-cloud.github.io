---
layout: default
parent: 高度な機能
nav_order: 10

title: "AWARE Frameworkとの連携"
created: 2024-04-23T07:34:11Z
updated: 2024-04-23T10:24:05Z
id: "6626e5ded583260025e8b253"
views: 14
---

# AWARE Frameworkとの連携

AWARE Frameworkとの連携
(テスト中)
AWARE Framework <https://awareframework.com/> は、スマートフォンで動作する、ユーザーのさまざまな情報を収集可能なツールです。スマートフォンで得られる加速度情報やGPS情報、HealthKitにより得られる睡眠動態などの情報を実験のために収集することができます。

AWARE Frameworkを使用するためには、以下のようなコードを記述します。

```javascript
   context.health.request({
     type: 'aware',
   }, function(result, error) {
     if (!result) {
       console.error('Error', error);
       alert('Error occurred');
       return;
     }
     const script = 'console.log("TEST", source); context.messaging.send({type: "text", text: "AWAREデータが共有されました " + new Date()});';
     context.health.setHandler({
       target: '*',
       awareSensors: ['screen', 'plugin_ios_activity_recognition', 'battery', 'accelerometer', 'google_fused_locaion'],
       messageToPDS: true,
       script: script,
     }, function(error) {
       if (!error) {
         return;
       }
       alert('ERROR!! ' + error);
     });
     /*context.health.getLastData({
       target: 'sleep',
     }, function(data, error) {
       console.log('TEST', data, error);
     });*/  
   });

```
