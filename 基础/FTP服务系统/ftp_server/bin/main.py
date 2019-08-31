#__author: Think
#date 2019/8/24

import os,sys,socketserver
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import user_manage
from core.server import MyTCPHandler


if __name__ == '__main__':
    main_info = '''
    主页
        1、启动服务器
        2、进入用户管理
        退出请按q
    '''

    while True:
        print('\033[1;35m{}\033[0m'.format(main_info))
        choice = input("请输入你的选择：")
        if choice == 'q':
            exit()
        elif choice == '1':
            print('已启动ftp服务器,请用客户端登录进行访问！')
            HOST, PORT = 'localhost',8080
            server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)

            server.serve_forever()
        elif choice == '2':
            usermanage = user_manage.UserManage()
            usermanage.user_run()
        else:
            print("\033[1;31m输入错误，请重新输入\033[0m")
            continue



