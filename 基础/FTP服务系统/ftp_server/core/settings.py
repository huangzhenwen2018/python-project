#__author: Think
#date 2019/8/24

import os, configparser, logging

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = os.path.join(base_dir, 'conf/server.conf')

# 初始化
cf = configparser.ConfigParser()
cf.read(config_file,encoding="utf-8")

#####设定用户信息存储位置####
if os.path.exists(cf.get('userinfo', 'userinfo_dir')):
    userinfo_dir = cf.get('userinfo', 'userinfo_dir')
else:
    userinfo_dir = os.path.join(base_dir, 'user_db')

####设定用户上传文件目录，这边用于创建用户家目录使用####
if os.path.exists(cf.get('upload', 'upload_dir')):
    file_dir = cf.get('upload', 'upload_dir')
else:
    file_dir = os.path.join(base_dir, 'home')
