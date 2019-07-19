#__author: Think
#date 2019/7/16
import os, sys, json, time

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from config import settings
from user_auth import auth

#以列表形式定义ATM管理菜单
atm_menu_show = [
    "1.账户总览",
    "2.转账",
    "3.提现",
    "4.每月还款",
    "5.冻结解冻",
    "6.打印账单",
    "7.购物结算API",
    "8.用户退出"
]
#定义查询用户接口函数
'''
def select():
    username = input("请输入所需查询用户名：")
    if os.path.isfile(settings.pathfile(username)):
        print(getuserinfo(username))
        log = "查询到此用户：" + username
    else:
        print("无此用户,确认后再重新输入")
        log = "查询" + username + "用户，没有结果"
    atm_logs(log)
'''
def userselect(acc_data):
    print("用户%s账户总览：" %acc_data["username"],acc_data)

#定义转账接口函数
def transfer(acc_data):
    pass

#定义提现接口函数
def withdraw(acc_data):
    print(acc_data)


#定义冻结解冻接口函数
def frozen(acc_data):
    print("\t冻结或解冻账户，请按照指引操作。")
    act = input("\t\t按1:冻结,按2:解冻,按3:查询账户>>>").strip()
    user = acc_data['username']
    if act == "1":
        acc_data["frozon"] = True
        print("冻结%s用户成功!" %user)
        log = "冻结%s用户成功!" %user
    elif act == "2":
        acc_data["frozon"] = False
        print("解冻%s用户成功!" %user)
        log = "解冻%s用户成功!" %user
    elif act == "3":
        if acc_data["frozon"] == False:
            print("\t\t该账户%s目前处于可用状态！" %user)
            log = "该账户%s目前处于可用状态！" %user
        else:
            print("\t\t该账户%s已被冻结，请解冻后再使用！" %user)
            log = "该账户%s已被冻结，请解冻后再使用！" %user
    else:
        print("输入有误")
        return "fail"
    auth.adduserinfo(acc_data['username'], acc_data)
    atm_logs(log)



#定义每月还款接口函数
def repayment():
    pass
#定义打印账单接口函数
def printbill():
    pass

def userlogout():
    pass


def atm_logs(lines):#lines为要写的日志
    with open(BASE_DIR + '/logs/atm.log','a',encoding='utf8') as f:
        curr_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        f.write("%s %s\n" %(curr_time,lines))

def api_paymet():
    pass

#以字典形式定义ATM各个菜单功能接口
atm_menu = {
    "1": userselect,
    "2": transfer,
    "3": withdraw,
    "4": repayment,
    "5": frozen,
    "6": printbill,
    "7": userlogout,
}

def atm_run(acc_data):
    while True:
        print("ATM功能列表：")
        for i in atm_menu_show:  #展示ATM菜单列表
            print("\t"+i)
        choise = input("请选择功能,q返回上一层>>：").strip()
        if choise == "q":
            break
        elif choise and choise in atm_menu: #选择相应的ATM功能
            atm_menu[choise](acc_data)              #执行ATM接口功能
