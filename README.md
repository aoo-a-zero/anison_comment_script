[English](README.md)

# anison_comment_script

iTunes(Music)ライブラリに登録されているすべての楽曲に対し、コメント欄にアニソン情報を自動付与するPythonスクリプトです  
[AnisonGeneration](http://anison.info/) 様 が公開している [各種csvデータ](http://anison.info/data/download.html) を使用します

# 動作確認環境

- macOS 13
- Python 3.11.3
- Music 1.3.5.8 (ja)

# 使い方

1. pythonと関連ツールをインストール

```bash
pip install regex jaconv appscript
```

2. 以下のように [AnisonGeneration](http://anison.info/)様 で配布している [各種csvデータ](http://anison.info/data/download.html) を配置

```
anison_comment_script
├── anison_comment.py
├── anison.csv
├── game.csv
└── sf.csv
```

3. 実行

```bash
python anison_comment.py 
```

うまく実行できない場合、「フルディスクアクセス」の権限をPythonに与えてみてください

# 仕様

csv側とiTunes(Music)側のタイトルとアーティスト名を正規化し、マッチするかどうかを判断します  
楽曲名とアーティスト名がマッチしたら番組名をコメント欄に登録します  

マッチしたかどうかの条件は以下の通りです
- csv側もしくはiTunes(Music)名が3文字以下の場合、完全一致であればマッチ
- csv側もしくはiTunes(Music)名が4文字以上の場合、片方がもう片方の文字列を含んでいるならマッチ

また、アーティスト名については複数表記や別名を考慮する処理を含めています  

詳細は [スクリプト内のコード](anison_comment.py) をご確認ください

# 注意

- コメントを上書きしないように考慮していますが、念のためバックアップを取った上で実行してください
  - 本スクリプトを実行したことによるトラブル・損失・損害は一切の責任を負いません
- 仕様上、期待しない番組名が登録されることがあります
  - ex) `Release Tha Power / M-PROJECT` = `POWER / JAM Project`  
  （無関係にも関わらず、互いに文字列が含まれているため同一曲と誤判断する）
  - より良いマッチ条件があれば、Pull Requestを待っています

# ライセンス

[THE BEER-WARE LICENSE](https://en.wikipedia.org/wiki/Beerware)

> If we meet some day, and you think this stuff is worth it, you can buy me a beer in return.

🍺🐟