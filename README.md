# Arduino Serial Plot Recorder

シリアルデータのグラフ表示およびデータ保存のための クロスプラットフォーム GUI アプリケーション

https://user-images.githubusercontent.com/47422498/188193987-20007fda-5fae-441a-a0bc-64eb2a458b2b.mov

## Overview

Arduino からのシリアルデータを読み取り、グラフの表示およびデータを保存する PyQt ベースの汎用的なアプリケーションです。[Arduino Sensor Data Viewer](https://github.com/kiyu-git/Arduino-Sensor-Data-Viewer)と組み合わせることで、リアルタイムにセンサー等のデータを解析できます。軽量なので、Raspberry Pi などでも動作します。

## Requirement

### Mac

- PyQt のインストール

```
% brew install pyqt@5
```

- conda のインストール
- conda パッケージのインストール

```
% conda create -n PyQt python=3.9
% conda activate PyQt
% conda install pyqt
% conda install numpy
% conda install pyserial
% conda install pyqtgraph
```

- リポジトリのクローン

```
% git clone https://github.com/kiyu-git/Arduino-Serial-Plot-Recorder
```

## Usage

### Arduino

[サンプルスケッチ](./Arduino%20Sketch/)を参考に、スケッチを Arduino に書き込んでください。

この際、サンプリングレートと測定チャンネル数を覚えておいてください。

### Python

```
% cd Python
% python main.py
```

## Features

GUI のパラメータ説明

**シリアルポート選択**

- シリアルポートを選択する
- [Research serial port] からポートを再検索できる

**Measurement Settings パネル**

- show ports からシリアルポートの変更が可能
- number of channels: Arduino スケッチの測定チャンネル数に一致させる
- sampling rate: Arduino スケッチのサンプリングレートに一致させる
- display duration: 表示する時間の長さを変更できます。表示するデータ数が多くなると、動作が重くなります。長期的な変動を見る場合は[Arduino Sensor Data Viewer](https://github.com/kiyu-git/Arduino-Sensor-Data-Viewer)と組み合わせて使用してください

**Measurement パネル**

- start: 測定データの表示を開始します
- stop: 測定データの表示を停止します

**Record Settings パネル**

- record interval: 保存するデータの間隔を変更します。すべてのデータを保存すると、データ量が大きくなってしうため、この間隔での平均値を保村します
- save path: 記録データの保存先を選択します。記録データは選択されたフォルダ内の Data フォルダの中に保存されます。Data フォルダの中に Data フォルダが作られることのないように注意してください。

**Record パネル**

- start: 記録を開始します
- stop: 記録を停止します
- open folder: 記録データの保存先を開きます

**Note パネル**

Note パネルは測定時のメモのためのパネルです。Note データは、記録データと同じフォルダに保存されます。今後、カスタマイズできるよう、改善していく予定です。

## Related repository

このリポジトリは、『[植物生体電位測定をオープンにするプロジェクト](https://docs.google.com/presentation/d/1Tm0e-mBNrTchN6YlGpvvomUZfy79yOtrTSNHG-l_jFg/edit?usp=sharing)』の一部です。

『[植物生体電位測定をオープンにするプロジェクト](https://docs.google.com/presentation/d/1Tm0e-mBNrTchN6YlGpvvomUZfy79yOtrTSNHG-l_jFg/edit?usp=sharing)に関連する以下のリポジトリと組み合わせることによって、植物生体電位を測定することが可能です。

- 植物生体電位解析器 : https://github.com/kiyu-git/Plant-Bioelectric-Potential-Sensor
- 測定アプリケーション : https://github.com/kiyu-git/-Arduino-Serial-Plot-Recorder
- 解析アプリケーション : https://github.com/kiyu-git/Arduino-Sensor-Data-Viewer
- 照明スイッチの自動化 : https://github.com/kiyu-git/Arduino-Python-Serial-Control-Example

植物生体電位の測定の詳細については[こちら](https://docs.google.com/presentation/d/1Tm0e-mBNrTchN6YlGpvvomUZfy79yOtrTSNHG-l_jFg/edit#slide=id.g15184a93673_0_264)を参考にしてください。

植物生体電位測定の例
![Plant-Bioelectric-Potential-Mearurement](https://github.com/kiyu-git/Plant-Bioelectric-Potential-Sensor/raw/main/images/Plant-Bioelectric-Potential-Mearurement.jpeg)

## Reference

## Author

質問等は twitter または[Issues](https://github.com/kiyu-git/Arduino-Serial-Plot-Recorder/issues)より

twitter: https://twitter.com/kyu_yukirinrin

website: https://untamable.work

## Licence

[GNU General Public License v3.0](./LICENSE)
