#__author: Think
#date 2019/7/18

import os, sys, json
from atm import atm_main
from config import settings
from shopping import shopping


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

"""
user_data = {
    'username':None,
    'is_authenticated':False,
}
def login_required(func):
    def wrapper(*args,**kwargs):
        if user_data['is_authenticated']:
            return func(*args,**kwargs)
        else:
            exit("暂时还没有用户登录！")
    return wrapper
"""

def loggin():
    username = input("\033[31;1m请输入登录用户名:\033[0m")
    if os.path.isfile(settings.pathfile(username)):
        password = input("\033[31;1m请输入用户密码:\033[0m")
        userinfo_login = getuserinfo(username)
        if password == userinfo_login["password"]:
            print("用户%s登录成功。" % username)
            log = "用户%s登录成功。" % username
            atm_main.atm_logs(log)
            while True:
                print("\033[34;1m\t1.逛商场\033[0m")
                print("\033[34;1m\t2.ATM管理\033[0m")
                choise = input("请选择进入(b返回登录界面)>>>:").strip()
                if choise == "1":
                    shopping.shop_run(userinfo_login)  # 进入购物接口
                elif choise == "2":
                    atm_main.atm_run(userinfo_login)  # 进入ATM管理接口
                elif choise == "b":
                    break
        else:
            print("用户密码不对，请重新输入。")
            log = "用户%s密码不对，请重新输入。"  %username
    else:
        print("无此用户,确认后再重新输入或者注册一个新账号。")
        log = "无此用户%s,确认后再重新输入或者注册一个新账号。" %username
    atm_main.atm_logs(log)


def useradd():
    username = input("请输入用户名：")
    if not os.path.isfile(settings.pathfile(username)):
        passwd = input("请输入密码：")
        balance = int(input("请输入存款金额："))
        limit = int(input("请设置信用额度："))
        info = {'username': username, 'password': passwd, 'balance': balance, 'limit': limit, 'frozon': False}
        adduserinfo(username, info)
        log = "添加用户" + username
    else:
        print("添加的用户%s已经存在" %username)
        log = "添加用户失败，用户%s已经存在" %username
    atm_main.atm_logs(log)

def userdelete():
    username = input("请输入所需销户用户名：").strip()
    if os.path.isfile(settings.pathfile(username)):
        deleteuserinfo(username)
    else:
        print("该用户%s不存在" % username)

def adduserinfo(user, addinfo):
    with open(settings.pathfile(user), 'w', encoding='utf8') as f1:
        f1.write(json.dumps(addinfo))

def deleteuserinfo(user):
    os.remove(settings.pathfile(user))
    print("用户销户%s成功" %user)
    atm_main.atm_logs("用户销户%s成功" %user)

def getuserinfo(user):
    with open(settings.pathfile(user), 'r', encoding='utf8') as f1:
        userinfo=json.loads(f1.read())
    return userinfo