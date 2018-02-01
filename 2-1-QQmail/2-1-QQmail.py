import requests
class Mail:
    def __init__(self):
        self.Cookie={'cookie':'pgv_pvi=610611200; RK=6MU7AuZbOV; ptcz=6fb159c251e4e13f53fb0ec86d740924dc1d866543f19a1581428648e8cfef56; pt2gguin=o0491565693; pgv_pvid=5634983248; edition=mail.qq.com; webp=1; o_cookie=491565693; pac_uid=1_491565693; luin=o0491565693; lskey=0001000085593db0d8a3d1dbc4530f49966b28a2e18df050bffb37e741d54574071525b1690d3d2c6d202688; tvfe_boss_uuid=1ced0b6f65d0ed40; pgv_si=s9889549312; uin=o0491565693; skey=@jJE85vOKc; ptisp=cnc; p_uin=o0491565693; pt4_token=L5Igm3mhQbNRQCuHNPeDaUjBpYulAHBh6kPHYBnFcOs_; p_skey=bLExUpV33J88saJy7Zt6ARQ*9EIqd6zrOkHSY9OQRMs_; wimrefreshrun=0&; qm_flag=0; qqmail_alias=491565693@qq.com; sid=491565693&d4c803425d21c4d49ded4325b5df6dc5,qYkxFeFVwVjMzSjg4c2FKeTdadDZBUlEqOUVJcWQ2enJPa0hTWTlPUVJNc18.; qm_username=491565693; qm_domain=https://mail.qq.com; qm_ptsk=491565693&@jJE85vOKc; qm_ptlsk=491565693&0001000085593db0d8a3d1dbc4530f49966b28a2e18df050bffb37e741d54574071525b1690d3d2c6d202688; foxacc=491565693&0; ssl_edition=sail.qq.com; \
                 qm_loginfrom=491565693&wpt; username=491565693&491565693; new_mail_num=491565693&237; CCSHOW=000000'}
        self.headers={'referer':'https://mail.qq.com/zh_CN/htmledition/ajax_proxy.html?mail.qq.com&v=140521',
                'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.18 Safari/537.36'
        }
        self.url='https://mail.qq.com/cgi-bin/compose_send?sid=TTDZccNTCkY0Ql8F'
    def sendmessage(self):
        self.data = {'a5f9f7485b2afff7b2cb02401887d611': 'd4c803425d21c4d49ded4325b5df6dc5',
                     'sid': 'TTDZccNTCkY0Ql8F',
                     'from_s': 'cnew',
                     'to': '3429275949@qq.com',
                     'subject': 'xixixi成功了',
                     'content__html': '<div>=。=</div>',
                     'sendmailname': '491565693@qq.com',
                     'savesendbox': '1',
                     'actiontype': 'send',
                     'sendname': '浪迹天崖',
                     'acctid': '0',
                     'separatedcopy': 'false',
                     's': 'comm',
                     'hitaddrbook': '0',
                     'selfdefinestation': '-1',
                     'domaincheck': '0',
                     'cgitm': '1517457641939',
                     'clitm': '1517457663487',
                     'comtm': '1517457724160',
                     'logattcnt': '0',
                     'logattsize': '0',
                     'cginame': 'compose_send',
                     'ef': 'js',
                     't': 'compose_send.json',
                     'resp_charset': 'UTF8'
                     }
        re=requests.post(self.url,json=self.data,headers=self.headers,cookies=self.Cookie)
        print(re.status_code)

re=Mail()
re.sendmessage()