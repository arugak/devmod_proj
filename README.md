# devmod_proj
NDA free [PHENITECH SEMICONDUCTOR](https://www.phenitec.co.jp/en/) CMOS 0.6um SPICE model

- 0.6um CMOS 5V --- PHENITECH SEMICONDUCTOR
- BSIM3 v3.3.0

## シミュレータごとの設定
- SPICE3, LTSpice, ngspice --- 修正なしで利用可能です
- HSPICE --- Level=8を、Level=53に書き換えてください

## これは何？
このモデル開発は、[MakeLSI:](http://ifdl.jp/make_lsi/)に集まった人たちが行いました。

- TEG(特性測定用の試作デバイス)設計 --- 高橋誓さん
- 特性測定 --- 秋田純一先生
- モデリング --- arugak
- 助言等 --- MakeLsi: MLの住人達

半導体デバイスの製造を受託するファウンダリは、ユーザ企業にモデルを提供しますが、一般に、これを利用するためにはNDAを締結する必要があります。そのため、個人が利用することは、ほとんど不可能です。NDAフリーのSPICEモデルは、個人がホビーで利用する場合に役立ちます。
