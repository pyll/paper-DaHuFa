# -*- coding: utf-8 -*-
import xlrd, jieba, numpy, codecs, pandas
 
file=codecs.open(r'comments.txt','r','utf-8')
content=file.read()
file.close()
segments=[]
segs=jieba.cut(content)
for seg in segs:
    if len(seg)>1:
        segments.append(seg)
segmentDF=pandas.DataFrame({'segment':segments})
df=segmentDF.groupby('segment')['segment'].agg({'计数':numpy.size})#.reset_index().sort(columns=['计数'],ascending=False)
print(df.head(100))
df.to_excel(r'jbcomments.xls',sheet_name='sheet1')
