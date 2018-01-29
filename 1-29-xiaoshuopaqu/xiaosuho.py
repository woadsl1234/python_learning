import re
import requests
from bs4 import BeautifulSoup
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"}
url="http://www.sjtxt.la/soft/"
def novel(url):
    req=requests.get(url,headers=headers)
    reg = r'<a href="/soft/(.*?)"><img src=(.*?)>(.*?)</a>'
    x=re.findall(reg,req.text)
    return x
def novel_content(url):
    reg = r'<a href="/book/(.*?)">(.*?)</a>'
    req = requests.get(url, headers=headers)
    req.encoding='utf-8'
    x = re.findall(reg, req.text)
    return x
def novel_txt(u="http://www.sjtxt.la/book/91218/"):
    req = requests.get(u, headers=headers)
    req.encoding = 'utf-8'
    bs=BeautifulSoup(req.text,'lxml')
    bs.encode('utf-8')
    x=bs.find_all(class_="pc_list")
    return x

for i in range(20):
    url1 = "http://www.sjtxt.la/soft/1/Soft_001_{}.html".format(i)
    x=novel(url1)
    for i1 in range(20):
        url2=url+x[i1][0]
        with open("xiaoshuo//"+x[i1][2]+".html",'w+') as fp:
            x1=novel_content(url+x[i1][0])
            x2=novel_txt("http://www.sjtxt.la/book/"+x1[1][0])
            fp.write(str(x2[1]))
            print("下载完成"+x[i1][2]+"\n------------------------------------------------------------------------------------")

