#__author: Think
#date 2019/8/25
import socketserver,json,os,sys,time

from core import user_manage
from core import settings

def timestamp_to_formatstringtime(timestamp):####时间戳转化为格式化的字符串
    structtime = time.localtime(timestamp)
    formatstringtime = time.strftime("%Y%m%d %H:%M:%S", structtime)
    return formatstringtime


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        auth_tag = False
        while auth_tag != True:
            auth_result = self.auth()
            print("the authentication result is:", auth_result)
            if auth_result != None:
                self.username = auth_result['用户信息']['username']
                self.spacesize = auth_result['用户信息']['spacesize']
                auth_tag = True
                user_homedir = os.path.join(settings.file_dir,self.username)
                if os.path.isdir(user_homedir):
                    self.position = user_homedir
                    print(self.position)


        while True:
            print("当前连接：", self.client_address)
            self.data = self.request.recv(1024).strip()
            #print(self.data.decode())
            if not self.data:
                print(self.client_address, "断开了")
                break
            cmd_dic = json.loads(self.data.decode('utf-8'))
            #print(cmd_dic)
            action = cmd_dic["action"]
            if hasattr(self, action):
                func = getattr(self, action)
                func(cmd_dic)
            else:
                print("未支持指令：", action)


    def auth(self):
        self.data = json.loads(self.request.recv(1024).decode('utf-8'))
        print(self.data)
        recv_username = self.data['username']
        recv_password = self.data['password']
        query_result = user_manage.query_user(recv_username)
        print(query_result)
        if query_result == None:
            self.request.send(b'user does not exist')
        elif query_result['用户信息']['password'] == recv_password:
            self.request.send(b'ok')
            return query_result ####返回查询结果
        elif query_result['用户信息']['password'] != recv_password:
            self.request.send(b'password error')
        else:
            self.request.send(b'unkonwn error')


    def pwd(self, *args):
        current_position = self.position
        result = current_position.replace(settings.file_dir,'')
        print(result)
        self.request.send(json.dumps(result).encode('utf-8'))

    def ls(self,*args):
        result = ['%-30s%-7s%-10s%-23s' % ('filename', 'type', 'bytes', 'creationtime')]
        for f in os.listdir(self.position):
            f_abspath = os.path.join(self.position, f)
            if os.path.isdir(f_abspath):
                type = 'd'
            elif os.path.isfile(f_abspath):
                type = 'f'
            else:
                type = 'unknown'
            fsize = os.path.getsize(f_abspath)
            ftime = timestamp_to_formatstringtime(os.path.getctime(f_abspath))
            result.append('%-30s%-7s%-10s%-23s' % (f, type, fsize, ftime))
        self.request.send(json.dumps(result).encode('utf-8'))

    def du_calc(self):
        # 注意不能使用os.path.getsize('D:\python-study\s14')返回的是所有目录大小的和
        '''统计纯文件和目录占用空间大小，结果小于在OS上使用du -s查询，因为有一些（例如'.','..'）隐藏文件未包含在内'''
        totalsize = 0
        if os.path.isdir(self.position):
            dirsize, filesize = 0, 0
            for root, dirs, files in os.walk(self.position):
                for d in dirs:
                    dirsize += os.path.getsize(os.path.join(root, d))
                for f in files:  # 计算文件占用空间
                    filesize += os.path.getsize(os.path.join(root, f))
            totalsize = dirsize + filesize
            return totalsize

    def du(self,*args):
        totalsize = self.du_calc()
        result = 'current directory total sizes: %d 字节' % totalsize
        print(result)
        self.request.send(json.dumps(result).encode('utf-8'))
        return totalsize

    def cd(self, *args):####切换目录，这个函数没怎么看懂
        user_homedir = os.path.join(settings.file_dir,self.username)
        cmd_dic = args[0]
        error_tag = False
        if cmd_dic['dirname'] == '':
            self.position = user_homedir
        elif cmd_dic['dirname'] in ('.','/') or '//' in cmd_dic['dirname']:
            pass
        elif cmd_dic['dirname'] == '..':
            if user_homedir != self.position and user_homedir in self.position:  ####当前目录不是家目录，并且当前目录是家目录下的子目录
                self.position = os.path.dirname(self.position)
        elif '.' not in cmd_dic['dirname'] and os.path.isdir(os.path.join(self.position,cmd_dic['dirname'])):####'.' not in cmd_dict['dir'] 防止../..输入
            self.position = os.path.join(self.position, cmd_dic['dirname'])
        else:
            error_tag = True

        if error_tag:
            result = 'Error,%s is not path here,or path does not exist!' % cmd_dic['dirname']
            self.request.send(json.dumps(result).encode('utf-8'))
        else:
            self.pwd()

    def mkdir(self, *args):
        try:
            dirname = args[0]['dirname']
            if dirname.isalnum():
                if os.path.exists(os.path.join(self.position, dirname)):
                    result = 's% have existed' % dirname
                else:
                    os.mkdir(os.path.join(self.position, dirname))
                    result = 's% created success' % dirname
            else:
                result = 'Illegal character %s, dirname can only by string and num here.' % dirname
        except TypeError:
            result = 'please input dirname'

        self.request.send(json.dumps(result).encode('utf-8'))






