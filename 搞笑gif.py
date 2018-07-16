
# -*- coding: utf-8 -*-
import random
import requests
import re
# import requesocks
import subprocess
from threading import Timer
import time


import time
from urllib import request
x=3145
url = 'http://www.gaoxiaogif.com/index_{}.html'
for page in range(337,350):


     # pageurl = ("http://www.xxhh.com/tag/%E5%8A%A8%E6%80%81%E5%9B%BE/page/%s/")
     pageurl = url.format(page)

     rex = re.compile(r'gifsrc="(http://.*?\.gif)"',re.S)

     heade = [
         'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
         'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
         'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
         'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
         'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
         'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
         'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
         'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
         'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
         'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
         'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
         'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
         'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
         'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
         'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
         'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11'

     ]

     headers = {
     'User-Agent': random.choice(heade)
    }
     print(pageurl)
     try:
        html1 = requests.get(pageurl, headers=headers,timeout=10).content.decode('gbk')
     # time.sleep(5)
     # print(html1)

        html = rex.findall(html1)
     # print(html)
        lensofpage=len(html)
        print (lensofpage)

     # picname = 'page' + page
     # print (picname)

        for picurl in html:
            path = 'D:\pic\%s.gif' % x
            try:
                # session = requesocks.session()
                # response = session.get(URL, headers=headers, timeout=10)
                request.urlretrieve(picurl,path)
                timeout = 10
                print(x)
         # print (page+picurl)
                x=x+1
            except Exception as e:
                print("错误",pageurl)
     except Exception as e:
         print("错误", pageurl)


        # print 'DownLoadPicOver'