#__author: Think
#date 2019/8/12
from configs import settings


def student_run():
    while True:
        print('\033[1;35m{}\033[0m'.format(settings.student_user_page))
        admin_login_choice = input("\033[1;34m请输入你的选择： \033[0m").strip()
        if admin_login_choice == '1':
            pass
        elif admin_login_choice == '2':
            pass
        elif admin_login_choice == '3':
            pass
        elif admin_login_choice == 'r':
            print('用户退出！')
            print('\033[1;35m{}\033[0m'.format(settings.student_user_page))
            break
        else:
            print("\033[1;31m您的输入不正确。\033[0m")