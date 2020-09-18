# JPEG-to-MP4-Converter
複数のJPEG形式の静止画を結合して動画(.mp4)へ変換するPythonコード

OpenCVを使ったJPEG->mp4変換処理です。

本ソースコードを使用するには、別途OpenCVのインストールが必要です。
```
$sudo apt install opencv-python
```

## 本ソースコードの実行方法

本ソースコードは、引数の渡し方で色々な機能を持たせているので、例を挙げて紹介します。

ここでは、例として"/home/user/images"ディレクトリにJPEGファイルが入っているものとします。

### 出力動画の解像度をコマンドで指定する場合

VGA解像度(640x480px)、フレームレート30fpsの動画に変換する例：
```
$python movie_convert.py /home/user/images VGA 30
```
'VGA'のように解像度の呼称を入力することで、動画の解像度を指定できます。

対応するコマンドは以下の通りです。

|解像度指定コマンド|画像サイズ|
|:---|:---|
|QVGA|320 x 240|
|VGA|640 x 480|
|WVGA|800 x 480|
|SVGA|800 x 600|
|XGA|1,024 x 768|
|HD(or WXGA)|1,280 x 768|
|FULLHD|1,920 x 1,080|

コマンドを忘れた！となった場合は、以下のように"help"と入力すると、上記の一覧表がコンソールに表示されます。
```
$python movie_convert.py help
```

### 出力動画の解像度を個別に指定する場合

前述のコマンドで指定できる以外の解像度で動画を作成したい場合は、個別に幅と高さを指定できます。

1280px x 700px、フレームレート10fpsの動画に変換する例：
```
$python movie_convert.py /home/user/images 1280 700 10
```

