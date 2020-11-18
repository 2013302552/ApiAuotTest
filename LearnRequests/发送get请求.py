'''
发送get请求
1.get 请求带参数
    方法1：拼接到URL后面
    方法2：使用params传参数
2.# get请求带请求头,例如设置User-Agent伪装成浏览器发送请求，避免服务器屏蔽自动化发的请求
'''
import requests

# 接口地址："http://www.baidu.com"
# 发送一个get请求,r是收到的响应
r = requests.get("http://www.baidu.com")
# 文本格式的相应内容
print(r.text)
# 响应码
print(r.status_code)
assert r.status_code == 200
# OK
print(r.reason)
assert r.reason == 'OK'

# http://主机地址:端口号/futureloan/mvc/api/模块/接口名
# m = requests.get("http://jy001:8081/futureloan/mvc/api/member/list")
# print(m.text)
# print(m.status_code)
# assert m.status_code == 200
# print(m.reason)
# assert m.reason == 'OK'

url = "http://jy001:8081/futureloan/mvc/api/member/list"
r = requests.get(url)
assert r.status_code == 200
assert r.reason == 'OK'
assert r.json()['status'] == 1
assert r.json()['code'] == '10001'

# get 请求带参数
# 方法1：拼接到URL后面（金融项目注册接口）
url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=13811111115&pwd=123456&regname=小蜜蜂"
r = requests.get(url)
print(r.text)
assert r.json()['status'] == 0
assert r.json()['code'] == '20110'
assert r.json()['msg'] == "手机号码已被注册"
# 方法2：使用params传参数
url = "http://jy001:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone":"13811111116","pwd":"123456","regname":"小蜜蜂"}
r = requests.get(url,params=canshu)
print(r.text)
# assert r.json()['status'] == 1
# assert r.json()['code'] == '10001'
# assert r.json()['msg'] == "注册成功"


# get请求带请求头,设置User-Agent伪装成浏览器发送请求，避免服务器屏蔽自动化发的请求
url = "http://www.httpbin.org/get?mobilephone=13811111115&pwd=123456&regname=小蜜蜂" # 一个测试网站，get是接口名字，发送的请求，原封的返回回来
r = requests.get(url) #"User-Agent": "python-requests/2.24.0"
print(r.text)
# User-Agent包含浏览器的版本号、操作系统的版本号等信息
tou = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
r = requests.get(url,headers=tou)
print(r.text)

url = "https://wenku.baidu.com/view/027d607deff9aef8941e06c0.html"
r = requests.get(url,headers=tou)
print(r.text)
print("蜂群算法源代码" in r.text)
