
import os,sys
#设定BASE_DIR值为项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#指定程序运行路径为项目根目录
sys.path.append(BASE_DIR)

#导入用户管理模块
from user_auth import auth
#导入ATM管理模块
from atm import atm_main
#导入shopping购物模块
from shopping import shopping

while True:
    print("欢迎访问X银行网上商城!")
    print("请你按照提示进行操作，祝购物愉快")
    print("\033[34;1m\t1.用户登录\033[0m")
    print("\033[34;1m\t2.用户注册\033[0m")
    print("\033[34;1m\t3.用户销户\033[0m")
    choise = input("请选择进入(q退出程序)>>>:").strip()
    if choise == "1":
        auth.loggin()
    elif choise == "2":
        auth.useradd()
    elif choise == "3":
        auth.userdelete()
    elif choise == "q":
        exit(0)


