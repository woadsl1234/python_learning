import time
import re
import requests
from bs4 import BeautifulSoup

class Weibo:
    def __init__(self):
        self.headers={'Cookie':'SINAGLOBAL=8134153024586.574.1513774011178; login_sid_t=6bbe39ed770d8433b6a5ddfa16046ab2; cross_ori\
        gin_proto=SSL; TC-Ugrow-G0=5e22903358df63c5e3fd2c757419b456; TC-V5-G0=784f6a787212ec9cddcc6f4608a78097; WBStorage=c5ff51335af29d81|undefined; _s_tentry=www.baidu.com; UOR=acm.hdu.edu.cn,widget.weibo.com,www.baidu.com; Apache=2409428435677.9116.1517715384668; ULV=1517715384674:3:1:1:2409428435677.9116.1517715384668:1516352940612; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhPlubnVHFT.5uZJNIPUndE5JpX5K2hUgL.FozRehnXehec1h-2dJLoI7U2qgiDqg4k; ALF=1549251358; SSOLoginState=1517715359; SCF=Aj_wts40Qmp_mpJUY08lqarQZ3RXxBoGALjdgKsJwjBVFpfU4sfN1jkzDqnWQIMCE8Fqwxflrv8nvUNlcFR9aYs.; SUB=_2A253cg_ODeRhGeRG61oV8C3KwzmIHXVUBmYGrDV8PUNbmtAKLWTskW9NUj280WHxuT584JlKTRhLic0Ve7-l\
        T5Sz; SUHB=0OMlyBN4SDfjHh; un=18767155950; wvr=6; wb_cusLike_2808403685=N; TC-Page-G0=cdcf495cbaea129529aa606e7629fea7',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.18 Safari/537.36'}
    def get(self,url):
        html=requests.get(url,headers=self.headers)
        return html.json()

with open("pinglun.txt",'w+',encoding='utf-8') as fp:
    for i in range(1,30):
        url='https://m.weibo.cn/api/comments/show?id=4203353188225415&page='+str(i)
        weibo=Weibo()
        l=len(weibo.get(url)['data']['data'])
        for j in range(l):
            try:
                fp.write(''.join(re.findall('[\u4e00-\u9fa5]',weibo.get(url)['data']['data'][j]['text'])) + "\n")
            except:
                pass
        print("下载完第"+str(i)+"页")