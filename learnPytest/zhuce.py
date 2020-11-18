import pytest
import requests


@pytest.fixture(params=[{"casedata": {"mobilephone": '1801234566', "pwd": '123456', "regname": "小蜜蜂"},
                         "expect": {"status": '0', "code": "20109", "data": 'None', "msg": "手机号码格式不正确"}},
                        {"casedata": {"mobilephone": 'null', "pwd": '123456', "regname": "小蜜蜂"},
                         "expect": {"status": '0', "code": "20103", "data": 'None', "msg": "密码不能为空"}},
                        {"casedata": {"mobilephone": '1801234a5672', "pwd": '123456', "regname": "小蜜蜂"},
                         "expect": {"status": '0', "code": "20109", "data": 'None', "msg": "手机号码格式不正确"}}])
def data1(request):
    return request.param


def test_register(data1):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data1)
    return r

def test_register1(data1):
    real = test_register(data1['casedata'])
    a = real.json()
    assert a['msg'] == data1['expect']['msg']
    assert a['code'] == data1['expect']['code']



# import pytest,requests
# @pytest.fixture(params=[{"casedata":{"mobilephone":"137123456789","pwd":"123456abc","regname":"aaa"},
#                         "expect":{"status":"0","code":"20109","msg":"手机号码格式不正确"}},
#                         {"casedata":{"mobilephone":"null","pwd":"123456abc","regname":"aaa"},
#                         "expect":{"status":"0","code":"20109","msg":"参数不能为空"}},
#                         {"casedata":{"mobilephone":"13745241111","pwd":"123456abc","regname":"aaa"},
#                         "expect":{"status":"0","code":"20110","msg":"手机号码已被注册"}}])
# def data2(request):
#     return request.param
# # def test_login4(data2):
# #     print(f"使用手机号码{data2['casedata']}测试注册功能,预期结果为{data2['expect']}")
# def register1(data3):
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     r = requests.post(url,data=data3)
#     return r
# def test_register1(data2):
#     real = register1(data2['casedata'])
#     assert real.json()['msg'] == data2['expect']['msg']
#     assert real.json()['code'] == data2['expect']['code']




#
# """
# 登录接口测试用例
# """
# import requests
# import pytest
#
#
#
# def register(data):
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     r = requests.post(url, data=data)
#     return r
#
# @pytest.fixture(params=[
#     {"data": {"mobilephone": "18012345%$", "pwd": 123456, "regname": "hello"},
#      "expect": {"status": 0, "code": "20109", "data": "None", "msg": "手机号码格式不正确"}},
#     {"data": {"mobilephone": "", "pwd": 123456, "regname": "hello"},
#      "expect": {"status": 0, "code": "20103", "data": "None", "msg": "手机号码不能为空"}},
#     {"data": {"mobilephone": "180123456789", "pwd": 123456, "regname": "hello"},
#      "expect": {"status": 0, "code": "20109", "data": "None", "msg": "手机号码格式不正确"}},
#     {"data": {"mobilephone": "1801234", "pwd": 123456, "regname": "hello"},
#      "expect": {"status": 0, "code": "20109", "data": "None", "msg": "手机号码格式不正确"}},
#     {"data": {"mobilephone": "180123X568", "pwd": 123456, "regname": "hello"},
#      "expect": {"status": 0, "code": "20109", "data": "None", "msg": "手机号码格式不正确"}},
#     {"data": {"mobilephone": "13745241111", "pwd": '123456abc', "regname": "hello"},
#      "expect": {"status": 0, "code": "20110", "data": "None", "msg": "手"}}
# ])
# def register_data(request):  # request是固定写法
#     return request.param  # request.param 是固定写法，取到每一组数据
#
#
#
# def test_register(register_data):
#     real = register(register_data['data'])
#     print(real.text)
#     assert real.json()['msg'] == register_data['expect']['msg']
#     assert real.json()['code'] == register_data['expect']['code']
#
# def test_login4(data2):
#     print(f"使用手机号码{data2['casedata']}测试注册功能,预期结果为{data2['expect']}")
