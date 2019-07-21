#__author: Think
#date 2019/7/21

import os, sys, logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

###################第一种 简单配置方式 logging.basicConfig()函数###############
#LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "#配置输出日志格式
LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"
DATE_FORMAT = '%Y-%m-%d %H:%M:%S %a ' #配置输出时间的格式，注意月份和天数不要搞乱了
logging.basicConfig(level=logging.INFO,
                    format=LOG_FORMAT,
                    datefmt = DATE_FORMAT ,
                    filename=r"..\logs\atm.log" #有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                    )

#######################第二种 日志流处理流程###################################

#1.创建logger，如果参数为空则返回root logger
logger = logging.getLogger("atm")
logger.setLevel(logging.DEBUG)

#2.创建handler
fh = logging.FileHandler("..\logs\\atm.log",encoding="utf-8")
ch = logging.StreamHandler()

#3.设置输出日志格式
formatter = logging.Formatter(
    fmt="%(asctime)s %(filename)s %(message)s",
    datefmt="%Y/%m/%d %X"
    )

#4.为handler指定输出格式，注意大小写
fh.setFormatter(formatter)
ch.setFormatter(formatter)













