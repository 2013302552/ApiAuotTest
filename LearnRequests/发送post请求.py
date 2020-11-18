'''
发送post请求
    1.使用data传表单格式的参数
    2.使用json传json格式的参数
    3.带请求头使用headers
'''
import requests

# 发送post请求，带参数时，可以使用data或json来传参，具体使用哪个要看系统怎么实现的。
# 上一步注册成功的手机号，验证登录，登录使用post
url = "http://jy001:8081/futureloan/mvc/api/member/login"
denglu = {"mobilephone":"12345678911","pwd":"123456","regname":"小蜜蜂"}

r = requests.post(url,data=denglu) # 表单
print(r.text)

r = requests.post(url,json=denglu) # json，金融系统不支持json方式传参
print(r.text)
assert r.json()['status'] == 0
assert r.json()['code'] == '20103'
assert r.json()['msg'] == "手机号不能为空"

# 发送请求到httpbin，观察区别
r = requests.post("http://www.httpbin.org/post",data=denglu) # "Content-Type": "application/x-www-form-urlencoded"
print(r.text)
r = requests.post("http://www.httpbin.org/post",json=denglu) # "Content-Type": "application/json"
print(r.text)