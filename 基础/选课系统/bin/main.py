#__author: Think
#date 2019/8/11

import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from configs import settings
from core import admin_view
from core import teacher_view
from core import models


def main():
    print("program begin running...")
    while True:
        print('\033[1;35m{}\033[0m'.format(settings.main_page))
        yourinput = input("\033[1;34m请输入你的选择： \033[0m").strip()
        if yourinput == '1':
            pass
        elif yourinput == '2':
            teacher_view.teacher_run()
        elif yourinput == '3':
            admin_view.admin_run()
        elif yourinput == 'q':
            print('退出系统!')
            sys.exit()
        else:
            print("\033[1;31m您的输入不正确。\033[0m")


if __name__ == '__main__':
    main()

