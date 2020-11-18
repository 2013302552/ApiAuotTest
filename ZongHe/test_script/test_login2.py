'''
登录测试功能
'''
import pytest

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_data.yaml"))
def login_data(request):
    return request.param


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_setup.yaml"))
def setup_data(request):
    return request.param


# 测试前置和后置
@pytest.fixture()
def register(setup_data, url, baserequests, db):
    # 注册
    phone = setup_data['casedata']['mobilephone']
    DbOp.deleteUser(db, phone)
    Member.register(url, baserequests, setup_data['casedata'])
    yield
    # 删除注册用户
    DbOp.deleteUser(db, phone)


def test_login(register, login_data, url, baserequests):
    # 登录
    print(f"测试数据为:{login_data['casedata']}")
    print(f"预测结果为:{login_data['expect']}")
    # 检查登录结果
    r = Member.login(url, baserequests, login_data['casedata'])
    assert str(r.json()['msg']) == str(login_data['expect']['msg'])
    assert str(r.json()['status']) == str(login_data['expect']['status'])
    assert str(r.json()['code']) == str(login_data['expect']['code'])
