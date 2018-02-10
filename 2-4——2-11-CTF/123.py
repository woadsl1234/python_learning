import requests

url='http://118.25.18.223:10002/'
data={'str1':"0",
      'str2[]':" "}
req=requests.post(url,data=data)
print(req.text)