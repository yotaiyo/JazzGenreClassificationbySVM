#coding:utf-8
import os
import sys

def mp3ToWav(mp3File,wavFile):
    # mp3を16kHz, 32bitでリサンプリング
    os.system("lame --resample 16 -b 32 -a '%s' temp.mp3" % mp3File)
    # mp3をwavに変換
    os.system("lame --decode temp.mp3 '%s'" %wavFile)
    os.remove("temp.mp3")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: python mp3_to_wav.py [mp3m4adir] "
        sys.exit()

    mp3m4aDir = sys.argv[1]

    for genre in ['Bop','Cool','Hard','Post']:
        for i in range(1, 151):
            for file in os.listdir("mp3m4aDir\%s\%d" %(genre,i)):
                if not file.endswith(".mp3"): continue
                mp3File = os.path.join("mp3m4aDir\%s\%d" %(genre,i), file)
                wavFile = os.path.join("mp3m4aDir\%s\%d" %(genre,i), file.replace('mp3','wav'))

                try:
                    # MP3を変換
                    mp3ToWav(mp3File, wavFile)
  
                    print("%s => %s" % (mp3File,wavFile))

                except:
                    continue