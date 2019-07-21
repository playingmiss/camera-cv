# camera-cv
このコードはカメラで画像を取得し、毎フレームごとの輝度の平均値を計算しグラフにプロットするものである
このグラフにおける横軸は始点を0フレームとして1フレーム単位、縦軸は256段階の輝度値をあらわしている
このコードを実行するにあたり、OpenCVが利用できる環境を用意する必要がある。

実行方法
- openCVが利用できる環境のコマンドプロンプトでこのリポジトリ内に存在するcv.pyファイルの実行命令を出す
このコードの実装に当たりカメラ画像取得のコードは以下のサイトの記述を参考にして作成した
https://github.com/nrsyed/computer-vision/blob/master/real_time_histogram/real_time_histogram.py

依存ライブラリについて
使用するライブラリが何のライブラリに依存しているかをpip showコマンドで表したものを以下に示す

実行の一例を以下のgifに掲載する

！[](https://github.com/playingmiss/camera-cv/blob/master/sample.gif)

Name: matplotlib

Version: 3.0.3

Summary: Python plotting package

Home-page: http://matplotlib.org

Author: John D. Hunter, Michael Droettboom

Author-email: matplotlib-users@python.org

License: PSF

Location: c:\users\fujiryu-gamer\anaconda3\lib\site-packages

Requires: numpy, cycler, kiwisolver, pyparsing, python-dateutil

Required-by: seaborn, scikit-image
