import os
for genre in ['Bop','Cool','Hard','Post']:
        for i in range(1, 151):
            Pass = os.path.join("mp3m4aDir\%s\%d" %(genre,i))
            combined_file=[]
            for m in range(60):
                a = '%s/results%d.txt'%(Pass,m)
                with open(a,'rb') as f:
                    file = f.read()
                    combined_file.append(file)
                    f.close
            for n in range(60):
                b = '%s/results_song.txt'%(Pass)
                with open(b, 'ab') as f:
                    f.write(combined_file[n])
                    f.close