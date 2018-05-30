function Execution_SegmentFeatureExtraction(Genre)
for n=1:150
    s = 'C:\\Users\\yota\\Documents\\MATLAB\\JazzGenreClassificationbySegmentFeature\\mp3m4adir\\%s\\%d';
    pass = sprintf(s,Genre,n);
    cd(pass);
    SegmentFeatureExtraction;
end
end