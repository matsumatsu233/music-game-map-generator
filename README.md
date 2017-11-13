# music-game-map-generator

音ゲーのキャプチャ動画から譜面を自動生成するものを作っています。最終的に出来るかどうか分かりませんが、とりあえずドラムマニアで頑張ってみます。

### 今の状況：
template matchingを使用してノートを認識するつもりですが、画像認識のこと全く分からなくて困ります。

黄色ノート（つまりスネア）だけ認識させてみました。結果は[outputフォルダー](https://github.com/matsumatsu233/music-game-map-generator/tree/master/output)でご覧になれます。プレイ画面の上の部分では、単独のノートならもれなく全部認識できそうです。他のノートも認識してしまいますが、あとの処理でなんとかなるでしょう。

こんな感じで全てのノーツが全部認識できればいいですが、ノートの間隔が少なすぎる場合（例えば32分）、あるいはノートが同時に降ってくる場合（例えば隣接の同時押し）にはどうなるかちょっと心配ですが、テンプレ画像をいじればなんとかなる気がします。

ゆっくり進んでいきたいと思います。

### ソースコードを動かす(適当)
環境: python 3.5
1. このリポジトリをクローンする
```
git clone https://github.com/matsumatsu233/music-game-map-generator.git
```
2. opencvといろいろをインストールする
```
pip install opencv-python
python -mpip install -U matplotlib
```
3. ソースコードを実行
```
cd music-game-map-generator
python yellow_note_recognition.py
```

### [ソース画像](https://github.com/matsumatsu233/music-game-map-generator/tree/master/frames_jpg)について
1.動画は[keepvid.com](https://keepvid.com/sites/download-youtube-video.html)を使ってyoutubeからダウンロード

2.ffmpegでフレーム抽出
```
ffmpeg -i ***.mp4 frames/$filename%03d.jpg
```
3. 名前は0から始まるやつがあって面倒くさくてpythonでstripした
```
python strip_zero_from_filename.py
```
