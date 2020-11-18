'''


'''

import requests

url = "http://jy001:8081/futureloan/mvc/api/member/login"
denglu = {"mobilephone":"12345678912","pwd":""}

r = requests.post(url,data=denglu) # 表单
print(r.text)
assert r.json()['status'] == 0
assert r.json()['code'] == '20103'
assert r.json()['msg'] == "密码不能为空"