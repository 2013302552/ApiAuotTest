'''
cookie
'''

import requests


head = {"Cookie": '__auc=0412d3f5175935539b08c9ae290; MEIQIA_TRACK_ID=1juMNUDqGur9ZIJ0QnMQu26m7zl; _ga=GA1.2.1590643183.1604649993; _gid=GA1.2.303004742.1605422228; __asc=112e0fe0175ca9f264f1c78abba; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1604735582,1604735735,1605422229,1605422483; MEIQIA_VISIT_ID=1kJdSM4EeocRGlIs6LgqXQLUZyO; BAGSESSIONID=cb83798e-9cc0-4732-baa7-c6c85aa8ffab; JSESSIONID=C729667E32DCBD524A5C369C08569700; _gat=1; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1605422639access_type=1&loginType=1&emailLoginWay=0&account=2013302552%40qq.com&password=fengkai3364524&imgVerifyCodeByEmailLogin=&remindmeBox=on&remindme=1&cell_phone=&geetest_challenge=&geetest_validate=&geetest_seccode=&sms_code=&returnPage='}
r = requests.get("https://www.bagevent.com/account/dashboard", headers = head)
print(r.text)
# 没登录时，title <title></title>

'''
requests中自动管理cookies的机制
'''
s = requests.session()  # 创建了一个sessions,通过sessions  发送请求
print("登录之前的cookies", s.cookies)
# 登录
canshu = {
    "access_type": 1,
    "loginType": 1,
    "emailLoginWay": 0,
    "account": "2780487875@qq.com",
    "password": "qq2780487875",
    "remindmeBox": "on",
    "remindme": 1,

}
r = s.post("https://www.bagevent.com/user/login", data=canshu)
print("登录之后的cookies", s.cookies)
# print(r.text)
# 调用dashboard的接口
r = s.get("https://www.bagevent.com/account/dashboard")
print("<title>百格活动 - 账户总览</title>" in r.text)
# 获取活动列表
r = s.get("https://www.bagevent.com/account/myevents?published=1")
print(r.text)
# 查看某个活动的详细信息
