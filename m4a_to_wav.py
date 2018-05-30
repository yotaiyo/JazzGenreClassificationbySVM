#coding:utf-8
import os
import sys

def m4aToWav(m4aFile, wavFile):
    # m4aをmp3に変換
    os.system("ffmpeg -i '%s' temp.mp3" %m4aFile)
    # mp3を16kHz, 32bitでリサンプリング
    os.system("lame --resample 16 -b 32 -a temp.mp3 temp1.mp3")
    # mp3をwavに変換
    os.system("lame --decode temp1.mp3 '%s'" %wavFile)
    os.remove("temp.mp3")
    os.remove("temp1.mp3")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: python mp3_to_wav.py [mp3m4adir]"
        sys.exit()

    mp3m4aDir = sys.argv[1]

    for genre in ['Bop','Cool','Hard','Post']:
        for i in range(1, 151):
            for file in os.listdir("mp3m4aDir\%s\%d" %(genre,i)):
                if not file.endswith(".m4a"): continue
                m4aFile = os.path.join("mp3m4aDir\%s\%d" %(genre,i), file)
                wavFile = os.path.join("mp3m4aDir\%s\%d" %(genre,i), file.replace('m4a','wav'))

                try:
                    m4aToWav(m4aFile, wavFile)
  
                    print("%s => %s" % (m4aFile, wavFile))

                except:
                    continue