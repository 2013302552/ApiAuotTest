import pytest

from ZongHe.baw import DbOp, Member
from ZongHe.caw import DataRead

# 登录失败
# 登录成功
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_pass.yaml"))
def pass_data(login):  # 固定写法
    return login.param
def test_login_pass(pass_data, url, db, baserequests):
    print(f"测试数据为:{pass_data['casedata']}")
    print(f"预测结果为:{pass_data['expect']}")
    phone = pass_data['casedata']['mobilephone']



    r = Member.login(url, baserequests, pass_data['casedata'])

    assert str(r.json()['msg']) == str(pass_data['expect']['msg'])
    assert str(r.json()['status']) == str(pass_data['expect']['status'])
    assert str(r.json()['code']) == str(pass_data['expect']['code'])

    r = Member.getList(url, baserequests)
    assert str(phone) in r.text
