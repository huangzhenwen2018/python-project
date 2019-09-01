#__author: Think
#date 2019/8/31

import  os,configparser,logging

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = os.path.join(base_dir, 'conf/server.conf')
cf = configparser.ConfigParser()
cf.read(config_file, encoding='utf-8')

####设定日志目录####
if os.path.exists(cf.get('log', 'logfile')):
    logfile = cf.get('log', 'logfile')
else:
    logfile = os.path.join(base_dir, 'log/client.log')

####设定下载/上传目录####
if os.path.exists(cf.get('download', 'download_dir')):
    download_dir = cf.get('download', 'download_dir')
else:
    download_dir = os.path.join(base_dir, 'temp')
