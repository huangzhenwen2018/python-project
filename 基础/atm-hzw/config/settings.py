#__author: Think
#date 2019/7/17
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

def pathfile(user):
    path = [BASE_DIR,'\\db\\',"%s"%user,'.json']
    db_file = "".join(path)
    return db_file
