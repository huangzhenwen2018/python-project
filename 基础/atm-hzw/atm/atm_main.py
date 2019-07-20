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
    "4.还款",
    "5.冻结解冻",
    "6.打印账单",
    "7.用户退出"
]
#定义查询用户信息函数
def userselect(acc_data):
    print("用户%s账户总览：" %acc_data["username"],acc_data)

#定义提现接口函数
def withdraw(acc_data):
    print("\t\t感谢您使用提现系统！")
    user = acc_data["username"]
  #  balance = acc_data["balance"]
    limit = acc_data["limit"]
    if acc_data["frozon"]:
        print("%s用户已经被冻结,不支持提现" %user)
        atm_logs("%s用户已经被冻结,不支持提现" %user)
        return "fail"
    bill = int(input("请输入提现金额："))
    if acc_data["balance"] - bill < - limit:
        print("你的提现额度超过信用额度了。")
        atm_logs("%s提现%s元失败，可用额度不够" % (user, bill))
    else:
        acc_data["balance"] = acc_data["balance"] - bill - bill*5/100
        auth.adduserinfo(user,acc_data)
        atm_logs("用户%s提现%s元成功" %(user,bill))
        print("用户%s提现%s元成功" %(user,bill))

#定义转账接口函数
"""
1.已登录用户是否冻结
2. 转入用户不能为已登录用户
3.转入用户是否冻结
4.已登录用户的可用额度是否够用
"""
def transfer(acc_data):
    print("\t\t感谢您使用转账系统！")
    user = acc_data["username"]
    if acc_data["frozon"]:
        print("该登录用户%s已经被冻结,不支持转账" %user)
        atm_logs("该登录用户%s已经被冻结,不支持转账" %user)
        return "fail"
    tousername = input("请输入转入方账号：").strip()
    touser = auth.getuserinfo(tousername)
    if touser['username'] != acc_data['username']:
        if touser["frozon"]:
            print("%s转入用户已经被冻结" % tousername)
            atm_logs("%s用户已经被冻结,不支持转入" %tousername)
            return "fail"
        tobill = int(input("请输入转入金额："))
        if acc_data["balance"] - tobill < - acc_data["limit"]:
            print("你的信用额度不够，少转点。")
            atm_logs("%s转账给%s失败，可用额度不够" %(acc_data['username'],tousername))
            return "fail"
        else:
            acc_data["balance"] -= tobill
            touser['balance'] += tobill
            auth.adduserinfo(user, acc_data)
            auth.adduserinfo(tousername, touser)
            atm_logs("%s用户转账给%s用户%s元成功" %(acc_data['username'],tousername,tobill))
            print("%s用户转账给%s用户%s元成功" %(acc_data['username'],tousername,tobill))
    else:
        print("转入用户%s不能为已登录用户,无法转账！" %touser['username'])
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

#定义还款接口函数
def repayment(acc_data):
    print("\t\t欢迎访问还款系统！")
    balance = acc_data["balance"]
    if balance > 0:
        print("你目前的余额为%s元,不需要还款" % balance)
        return "do not repayment"
    else:
        print("你目前的余额为%s元,需要还款%s元" % (balance, abs(balance)))
    rebill = int(input("请输入要还款的金额："))
    acc_data["balance"] = acc_data["balance"]+rebill
    auth.adduserinfo(acc_data['username'], acc_data)
    atm_logs("%s还款%s元成功" %(acc_data['username'],rebill))
    print("%s还款%s元成功" %(acc_data['username'],rebill))

#定义打印账单接口函数
def printbill(acc_data):
    date1 = input("输入打印账单开始日期,格式:2018-04-03 12:00:00>>>:")
    date2 = input("输入打印账单结束日期,格式:2018-04-03 20:00:00>>>:")
    with open(BASE_DIR+'/logs/'+acc_data["username"]+'.log','r',encoding='utf8') as f:
        for i in f:
            if i[:19] >= date1 and i[:19] < date2:
                print(i.strip())


def api(userinfo,num):
    if userinfo["frozon"]:
        print("%s用户已经被冻结" % userinfo["username"])
        atm_logs("%s用户已经被冻结,支付失败" % userinfo["username"])
        return "fail"
    if userinfo["balance"] - int(num) < - userinfo["limit"]:
        print("超过信用卡透支额度，无法购买")
        atm_logs("%s购物支付失败" % userinfo["username"])
        return "fail"
    else:
        userinfo["balance"] -= int(num)
        print("%s用户购物支付成功" % userinfo["username"])
    auth.adduserinfo(userinfo["username"], userinfo)
    atm_logs("%s用户购物支付成功,感谢欢迎使用。" % userinfo["username"])
    return userinfo["balance"]



def userlogout(acc_data):
    user = acc_data["username"]
    print("用户%s已退出,返回到首页！" %user)
    log = "用户%s已退出,返回到首页！" %user
    atm_logs(log)

    print("\t1.用户登录")
    print("\t2.用户注册")
    print("\t3.用户销户")
    choise = input("选择进入(q退出程序)>>>:").strip()
    if choise == "1":
        auth.loggin()
    elif choise == "2":
        auth.useradd()
    elif choise == "3":
        auth.userdelete()
    elif choise == "q":
        exit(0)

def atm_logs(lines):#lines为要写的日志
    with open(BASE_DIR + '/logs/atm.log','a',encoding='utf8') as f:
        curr_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        f.write("%s %s\n" %(curr_time,lines))


#以字典形式定义ATM各个菜单功能接口
atm_menu = {
    "1": userselect,
    "2": transfer,
    "3": withdraw,
    "4": repayment,
    "5": frozen,
    "6": printbill,
    "7": userlogout
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

