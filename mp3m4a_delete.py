# mp3m4aデータを完全に削除してしまうので注意
import os
for genre in ['Bop','Cool','Hard','Post']:
    for i in range(1, 151):
        for file in os.listdir("mp3m4aDir\%s\%d" %(genre,i)):
            mp3File = os.path.join("mp3m4aDir\%s\%d" %(genre,i), file)
            if file.endswith(".wav") :continue
            os.remove(mp3File)