import requests

class zhihu(object):
    def __init__(self):
        self.cookie={'Cookie':'_zap=a6d9ba10-7900-4985-910a-8e4e12a69649; l_cap_id="YTg4ZDgzNTIyMDA0NDE4ZGI2YjE4ZTNjNWRkNWNlZWI=|1516272041|37f1de4b68480c28ac0842dedd7c5bab5adf8088"; r_cap_id="ZTAyZTQ1YzE2NjM4NGIzN2IwODIzNGY2ZDQxMDVmYjY=|1516272041|6b168b1fb3bb01ee228d1e5df98777abb86203b6"; cap_id="M2Q5Mzc0YzNlOGEzNGQ1YmFlMjUwNDE3ZDFmMzY0Zjc=|1516272041|8c0e2484122e61e76d5bd1d0af14c1fc21c3ab78"; capsion_ticket="2|1:0|10:1516272049|14:capsion_ticket|44:MTdjZjM2YTc5MjBkNDZmMzkzYjA2YmUyZDRmNDZjYWM=|f8dfea435407ebf36d2a5132b3483dd1b75425ffb2e32abd35c52b9cf59cf7b4"; z_c0="2|1:0|10:1516272064|4:z_c0|92:Mi4xVlJ5SUF3QUFBQUFBWUd0QmIwb0NEU1lBQUFCZ0FsVk53TWROV3dEX1J3dDRIb2ZYeFhadFpRakp5X3JEeWVjQ0h3|e5a683e22786586e44e90f73d8d3ea61d217260a2eb4da87b8c8799d77520a86"; aliyungf_tc=AQAAAFw9RS3gagEApIlZfBCSUH/LfWWy; _xsrf=f2a57ff0-d186-4e47-8791-9f242e70ff49; q_c1=43ba91e019b34315bdbbbdef6b770872|1517314737000|1513773879000; d_c0="AMBrxmjVEQ2PTl8_4Eik7xsDWnS0yuV7ADU=|1517315094"; __utma=155987696.383349824.1517315136.1517315136.1517315136.1; __utmb=155987696.0.10.1517315136; __utmc=155987696; __utmz=155987696.1517315136.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'}
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.18 Safari/537.36'
        }
        self.url='https://www.zhihu.com/api/v4/messages'
    def sendmessage(self,data):
        re=requests.post(url=self.url,json=data,headers=self.headers,cookies=self.cookie)
        print(re.status_code)
data={
        'content':"打卡",
        'receiver_hash':'"5783c2bff33bed08202f5c3732ae53b5"',
        'type':'"common"'
        }
test=zhihu()
test.sendmessage(data)