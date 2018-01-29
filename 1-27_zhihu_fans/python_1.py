import requests
import json

url="https://zhuanlan.zhihu.com/api/columns/wajuejiprince/followers?limit={}".format(1000)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
         'Cookie':'q_c1=fb437e82f5fd400293174d3d9fc30f86|1515595896000|1515595896000; _zap=df3125f2-b30e-4000-8fbf-90c37049b226; r_cap_id="ZDVmZjJlNzc4YmEwNDYyYWJjMGQxYjQ2MThhMWIzOTk=|1515604991|52163f959b90d1f118cf2df531f087341ecf1e3c"; cap_id="MDc2YjllZjg2YzQ2NDE5N2IwMmI4ZWVhN2JlNjA3NDY=|1515604991|dc2d43758b2025fe3d04345819b8ef8d2ec2d9f9"; l_cap_id="Mjk2YWEwMjc3NzYwNGQ0Mjk2NzUwNThjODU4ZmE5NmU=|1515604991|f027419c22ec69a663be94a3ebe04c0d55eac8a3"; aliyungf_tc=AQAAAEqbmFyw3w0AIjEWJJMuXB/zQpsM; _xsrf=2|9cdda69d|4eef2c8b7eac5f1e2b38408ce3597287|1517040702; XSRF-TOKEN=2|9cdda69d|4eef2c8b7eac5f1e2b38408ce3597287|1517040702'}
re=requests.get(url,headers=headers)
js=json.loads(re.text)
with open("test.txt","w+") as fp:
    for i, js in enumerate(js):
        i = i + 1
        name = js['name']
        fp.write(str(i)+" ")
        fp.write(name+"\n")
