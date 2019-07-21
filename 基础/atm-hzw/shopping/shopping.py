#__author: Think
#date 2019/7/16

import os,sys,json,time
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
from atm import atm_main

goods_list = {
    "1":{"icar":281100},
    "2":{"ipad":7888},
    "3":{"iphone":5888},
    "4":{"huawei P3":4999},
    "5":{"mi fan":19},
    "6":{"hong mi":999},
    "7":{"hat":9},
    "8":{"pen":7},
    "9":{"wrap":38}
}
goods = []  #购物车列表
curr_goods = '' #当前用户商品选择情况

def showgoods_list():
    print("商品列表展示:")
    print("\033[34;1m\t%-7s%-10s%-10s\033[0m" % ("商品号", "商品名", "价格"))
    for i in goods_list:
        for j in goods_list[i]:
            print("\033[34;1m\t%-10s%-13s%-13s\033[0m"%(i,j,goods_list[i][j]),end='\n')

#购物车物品展示
def showcar(data):
    print("你的购物车列表：")
    sum = 0
    for i in data:
        for j in i:
            print("\033[34;1m商品名：%-10s  价格：%s元\033[0m" % (j, i[j]))
            sum += i[j]
    print("\033[34;1m\t\t\t\t合计：%s元\033[0m" % sum)
    return int(sum)

#商品加到购物车里
def shopcar(name):
    goods.append(name)

def shop_logs(username,goodslist):  #user为要记录的用户文件名，goodslist为货物列表
    with open(username,'a',encoding='utf8') as f:
        curr_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        for i in goodslist:
            for j in i:
                f.write("%s 购买：%-10s  价格：%s元\n" % (curr_time,j, i[j]))

def shop_run(acc_data):
    print("欢迎光临本购物商城，优惠多多，祝购物愉快！")
    while True:
        showgoods_list()
        choise = input("请选择你要购买的商品号（按q返回上一层,c查看购物车和结算）：").strip()
        if choise and choise in goods_list:
            global curr_goods  # 定义为全局变量
            shopping = input("该商品是否加入到购物车：\033[31;1m1.是 2.否 \033[0m>>>:")
            if shopping == "1":
                curr_goods = shopcar(goods_list[choise])
                print("加入购物车成功")
            elif shopping == "2":
                print("返回商品列表")
            else:
                print("输入有误，返回商品列表")
        elif choise == "c":
            user = acc_data
            bill = showcar(goods)
            bill_choise = input("\033[31;1m结算按1，取消按2：\033[0m")
            if bill_choise == "1":
                if curr_goods != '':  # 判断购物车为空时
                    k = atm_main.api(user, bill)  # 调用atm接口扣款
                    if k != "fail":
                        shop_logs(BASE_DIR + '/logs/' + user["username"] + '.log', goods)  # 记录购物清单日志
                        with open(BASE_DIR + '/logs/' + user["username"] + '.log', 'a', encoding='utf8') as f:
                            f.write("\t\t\t\t\t你目前的余额：%s\n" % k)
                        goods.clear()  # 结账成功清空购物车
                    break
                else:
                    print("购物车为空，请购买商品后再结算。")

        elif choise == 'b':
            break
        else:
            print("你选择的商品不存在，请重新选择:")
