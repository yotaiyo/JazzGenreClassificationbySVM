import os
if not os.path.exists('All_results'):
    os.mkdir('All_results')
for genre in ['Bop','Cool','Hard','Post']:
        combined_file = []
        for i in range(1, 151):
            Pass = os.path.join("mp3m4aDir\%s\%d" %(genre,i))
            a = '%s\\results_song.txt'%(Pass)
            with open(a,'rb') as f:
                file = f.read()
                combined_file.append(file)
                f.close
        for n in range(150):
            b = 'All_Results\\All_Results_%s.txt'%genre
            with open(b, 'ab') as f:
                f.write(combined_file[n])
                f.close