function SegmentFeatureExtraction

%楽曲の開始と終わりの無音区間をトリミングし，サンプリング周波数22050[Hz]で読み込む
a = 'Folder';
a=miraudio(a,'TrimStart','TrimEnd','Sampling',22050);

%ファイルの長さを取得
length_a = mirlength(a);
t = mirgetdata(length_a);

%楽曲波形全体から均等に1[s]のデータを60個取り出し，セグメント特徴量を計算
for i = 0:59
    %無音部分が多少残ってしまうことがあるため，+2[s]している
    t_middle = t/60 * i+2;
    trim_a = miraudio(a,'Extract',t_middle-0.5,t_middle+0.5);
    %0.05[s]のフレームに分割
    sg_a = mirframe(trim_a,0.05,1);
    
    %rms値
    rms_a = mirrms(sg_a);
    rms_mean = mirmean(rms_a);
    rms_std = mirstd(rms_a);
    
    %lowenergy
    lowenergy_a = mirlowenergy(trim_a);
    
    %Eventdensity
    eventdensity_a = mireventdensity(trim_a);
    
    %Tempo
    tempo_a = mirtempo(trim_a);
    
    %PulseClarity
    pulseclarity_a = mirpulseclarity(trim_a);
    
    %Zerocross
    zerocross_a = mirzerocross(sg_a);
    zerocross_mean = mirmean(zerocross_a);
    zerocross_std = mirstd(zerocross_a);
    
    %RollOff
    rolloff_a = mirrolloff(sg_a);
    rolloff_mean = mirmean(rolloff_a);
    rolloff_std = mirstd(rolloff_a);
    
    %brightness
    brightness_a = mirbrightness(sg_a);
    brightness_mean = mirmean(brightness_a);
    brightness_std = mirstd(brightness_a);
    
    %centroid
    centroid_a = mircentroid(trim_a);
    
    %spread
    spread_a = mirspread(trim_a);
    
    %skewness
    skewness_a = mirskewness(trim_a);
    
    %kurtosis
    kurtosis_a = mirkurtosis(trim_a);
    
    %flatness
    flatness_a = mirflatness(sg_a);
    flatness_mean = mirmean(flatness_a);
    flatness_std = mirstd(flatness_a);
     
    %mfcc
    mfcc_a = mirmfcc(sg_a);
    mfcc_mean = mirmean(mfcc_a);
    mfcc_std = mirstd(mfcc_a);
    
    %roughness
    roughness_a = mirroughness(sg_a);
    roughness_mean = mirmean(roughness_a);
    roughness_std = mirstd(roughness_a);
    
    %mirregularity
    regularity_a = mirregularity(sg_a);
    regularity_mean = mirmean(regularity_a);
    regularity_std = mirstd(regularity_a);
    
    %chromagram
    chromagram_a = mirchromagram(sg_a);
    chromagram_mean = mirmean(chromagram_a);
    chromagram_std = mirstd(chromagram_a);
    
    %keystrength
    keystrength_a = mirkeystrength(sg_a);
    keystrength_mean = mirmean(keystrength_a);
    keystrength_std = mirstd(keystrength_a);
    
    %mode
    mode_a = mirmode(sg_a);
    mode_mean = mirmean(mode_a);
    mode_std = mirstd(mode_a);
    
    results = {rms_mean,rms_std,lowenergy_a,beatspectrum_a, eventdensity_a,tempo_a,pulseclarity_a,zerocross_mean,zerocross_std,rolloff_mean,rolloff_std,brightness_mean,brightness_std,centroid_a,spread_a,skewness_a,kurtosis_a,flatness_mean,flatness_std,mfcc_mean,mfcc_std,roughness_mean,roughness_std,regularity_mean,regularity_std,chromagram_mean,chromagram_std,keystrength_mean,keystrength_std,mode_mean,mode_std};
    
    
    FileName = sprintf('results%d.txt',i);
    %結果を保存
    mirexport(FileName,results);
end
end
    

     


