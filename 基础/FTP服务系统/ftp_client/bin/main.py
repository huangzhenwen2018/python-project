#__author: Think
#date 2019/8/25

import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.client import FtpClient

if __name__ == '__main__':
    ftp = FtpClient()
    ftp.connect('localhost',8080)

    auth_tag = False
    count = 0
    while auth_tag != True:
        count += 1
        if count <= 3:
            auth_tag = ftp.auth()
        else:
            exit()

    ftp.interactive()
    ftp.close()