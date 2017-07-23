# -*- coding: utf-8 -*-
import requests, re, time, urllib2
 
#短评地址
url='https://movie.douban.com/subject/26811587/comments?start=300&limit=20&sort=new_score&status=P'
for i in range(300,301):
    #url=url1+str(i)+url2
    try:
        r=requests.get(url,headers={'user-agent':'Mozilla/5.0'})
        print r.status_code
        content=r.text  #爬取源代码
         
        #筛选源代码
        #短评
        comments=re.findall(r'<p class=""> .*[\n]*.*[\n]*        </p>',content)
        #写入记事本
        f=open('comments.txt','a')
        for comment in comments:
            f.write(comment)
            f.write('\n')
        f.close()
 
        #星
        stars=re.findall(r'allstar\d',content)
        #写入记事本
        f=open('stars.txt','a')
        for star in stars:
            f.write(star)
            f.write('\n')
        f.close()
 
        #时间
        times=re.findall(r'title="\d\d\d\d-\d\d-\d\d',content)
        #写入记事本
        f=open('times.txt','a')
        for t in times:
            f.write(t)
            f.write('\n')
        f.close()
    except:
        print 'error'
