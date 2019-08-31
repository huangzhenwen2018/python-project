#__author: Think
#date 2019/8/24
import time,hashlib,os,json,shutil
from core import settings

def hashmd5(*args):
    m = hashlib.md5()
    m.update(str(*args).encode())
    cipheretexts = m.hexdigest()
    return cipheretexts

def query_user(username):
    filelist = os.listdir(settings.userinfo_dir)
    dict = {}
    for filename in filelist:
        with open(os.path.join(settings.userinfo_dir, filename),'r',encoding='utf-8') as f:
            content = json.load(f)
            if content['username'] == username:
                dict = {'用户名':filename,'用户信息':content}
                return dict

class UserManage(object):
    def __init__(self):
        pass

    def add_userinfo(self,username):
        query_result = query_user(username)
        if query_result == None:
            password = input("请输入用户密码：").strip()
            if password == '':
                print('密码不能为空')
            else:
                id = time.strftime('%Y%m%d%H%M%S', time.localtime())
                userinfo = {
                    'username': username,
                    'id': id,
                    'phonenumber': '',
                    'password': hashmd5(password),
                    'spacesize': 104857600,
                    'level': 1
                }
                with open(os.path.join(settings.userinfo_dir, username), 'w', encoding='utf-8') as f:
                    json.dump(userinfo, f)
                    print("用户信息保存完毕")
                    try:
                        os.mkdir(os.path.join(settings.file_dir, username))
                        print('用户目录创建成功！')
                    except Exception as e:
                        print('用户目录创建失败！', e)
        else:
            print("用户名重复，信息未保存")

    def query_userinfo(self,username):
        query_result = query_user(username)
        if query_result != None:
            print(query_result)
        else:
            print("用户不存在")

    def change_userinfo(self,username):
        query_result = query_user(username)
        if query_result != None:
            filename = query_result['用户名']
            userinfo = query_result['用户信息']
            print('before update: ', userinfo)
            update_item = input("请输入要修改的项目,例如password,phonenumber,spacesize,level：")

            if update_item in ('username','id'):
                print(update_item, "项不可更改")
            elif update_item in ('password','phonenumber','spacesize','level'):
                print("update item: %s" % update_item)
                update_value = input("请输入要修改的项目的新值：")
                if update_item == 'password':
                    userinfo[update_item] = hashmd5(update_value)
                else:
                    userinfo[update_item] = update_value
                with open(os.path.join(settings.userinfo_dir, filename), 'w', encoding='utf-8') as f:
                    json.dump(userinfo, f)
                    print(update_item, "项用户信息变更保存完毕")
                    print('after update: ', userinfo)
            else:
                print('输入信息错误，', update_item, '项不存在')
        else:
            print('用户不存在，无法修改')



    def delete_user(self,username):
        query_result = query_user(username)
        if query_result != None:
            filename = query_result['用户名']
            userfile_path = os.path.join(settings.userinfo_dir,filename)
            os.remove(userfile_path)
            query_result_again = query_user(username)
            if query_result_again == None:
                print('用户信息文件删除成功！')
                try:
                    shutil.rmtree(os.path.join(settings.file_dir,username))
                    print('用户家目录删除成功')
                except Exception as e:
                    print('用户家目录删除失败：',e)
            else:
                print('用户信息文件删除失败！')
        else:
            print('用户不存在或者已经被删除')


    def user_run(self):
        userpage = '''
        用户管理界面
             1、新增用户
             2、查询用户
             3、修改用户
             4、删除用户
             退出请按q
             返回上一界面请按r        
        '''

        userpage_data = {
            '1': 'add_userinfo',
            '2': 'query_userinfo',
            '3': 'change_userinfo',
            '4': 'delete_user'
        }

        while True:
            print('\033[1;35m{}\033[0m'.format(userpage))
            choice = input('请输入你的选择：').strip()
            if choice == 'q':
                exit("退出程序！")
            elif choice == 'r':
                break
            elif choice in userpage_data:
                username = input("请输入用户名：").strip()
                if username == '':
                    print('用户不能为空')
                    continue
                if hasattr(self, userpage_data[choice]):
                    f = getattr(self, userpage_data[choice])
                    f(username)
            else:
                print("\033[1;31m输入错误，请重新输入\033[0m")
                continue





