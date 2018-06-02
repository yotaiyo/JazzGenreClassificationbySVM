# JazzGenreClassificationbySVM
### Overview  
楽曲波形から特徴量と呼ばれる楽曲特性を反映した値を抽出し，機械学習アルゴリズムの1つであるSVMを用いて特徴量を抽出することで，楽曲のジャンルを推定するアルゴリズムです．

### Dataset  
* 所有していた600曲のmp3，m4aジャズ音源データを使用しました．  
* 600曲のデータをDicogs[https://www.discogs.com/ja/]とAll Music[https://www.allmusic.com/]から収集したクラスラベル情報を用いてBop，Cool Jazz，Hard Bop，Post Bopと呼ばれる4つのジャンルに区分しました．今回は，これらのジャンルを高い精度で予測することが目的です．

### Feature Extraction
* Matlabのパッケージの1つであるMIRtoolbox[<https://www.jyu.fi/hytk/fi/laitokset/mutku/en/research/materials/mirtoolbox>]を用いて，特徴量を抽出します．MIRtoolboxには，便利な特徴量抽出アルゴリズムが多く実装されています．　　
* MIRtoolboxで使用可能な特徴量抽出アルゴリズムの中で，rms値やMFCC，Zerocrossといった代表的な19種類を使用します．
* 特徴量は20[ms]から80[ms]程度のフレーム単位で抽出されることが一般的ですが，抽出されるデータ量が多すぎるといった問題があります．
* 今回は，抽出された値から1[s]単位で平均値や標準偏差といった統計量を計算することでデータを圧縮します．（これをセグメント特徴量と呼びます）
* 最終的に，楽曲から均等に1[s]のデータを60個取り出し，19種類のセグメント特徴量を抽出することで，機械学習のインプットデータとして使用します．

### Machine Learning
* rbf SVMを使用．

### Requirement
* MatlabR2014a  
    - MIRtoolbox 1.6.3
    
* Python 3.6.4  
    - pandas 0.22.0  
    - numpy 1.14.0  
    - scikit-learn 0.19.1  

* lame[<http://lame.sourceforge.net/>]
* ffmpeg[<https://www.ffmpeg.org/>]

### Usage　　
* 以下のようなディレクトリ構成を想定しています.
JazzGenreClassificationbySVM/  
　　　├ mp3_to_wav.py  
　　　├ m4a_to_wav.py  
　　　├ mp3m4a_delete.py  
　　　├ combining_results.py  
　　　├ Create_All_Results.py  
　　　├ SVM.py  
　　　├ SegmentFeatureExtraction.m  
　　　├ Exection_SegmentFeatureExtraction.m  
　　　├ mp3m4adir/  
　　　　　　├ Bop/  
　　　　　　├ Cool/  
　　　　　　├ Hard/  
　　　　　　├ Post/  
　　　　　　　　├ 1/  
　　　　　　　　├ ~150/  
　　　　　　　　　　├ songname.mp3or.m4a  
1. mp3_to_wav.py，m4a_to_wav.py    
今回使用するデータセットには，ビットレートの違うmp3，m4aファイルが含まれています．
そこで，16[kHz]，32[bit]でリサンプリングし，wav形式に変換します．
2. mp3m4a_delete.py  
mp3，m4aデータは使用しないため削除します．
復元できないため，コピーを取っておくことをお勧めします．
3. Exection_SegmenttFeatureExtraction(GenreName).m  
セグメント特徴量を抽出し，results0.txt~results59.txtとして保存します．
4. combining_results.py  
results0.txt~results59.txtをresults_song.txtとしてまとめます．
5. Create_All_Results.py  
各曲から得られたresults_song.txtをAll_results/All_results_GenreName.txtとしてまとめます．
得られたAll_results_GenreName.txtをコピペしてAll_results/All_results.csvとして作成してください．
6. SVM.py  
SVMを用いてトレーニングと評価を行います．
