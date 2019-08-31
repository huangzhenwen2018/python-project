#__author: Think
#date 2019/8/25

import socket,hashlib,json

def hashmd5(*args):
    m = hashlib.md5()
    m.update(str(*args).encode())
    cipheretexts = m.hexdigest()
    return cipheretexts

class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()

    def connect(self, ip, port):
        self.client.connect((ip, port))

    def auth(self):
        username = input("请输入用户名>>>:").strip()
        # password = getpass.getpass("请输入密码>>>:").strip()  ####在linux上输入密码不显示，此模块在pycharm中无法使用
        password = input("请输入密码>>>:").strip()  ####Windows测试用
        #password = hashmd5(password)
        msg = {
            'username': username,
            'password': hashmd5(password)
        }
        self.client.send(json.dumps(msg).encode('utf-8'))
        server_response = self.client.recv(1024).decode('utf-8')
        if server_response == 'ok':
            print("认证通过！")
            return True
        else:
            print(server_response)
            return False

    def interactive(self):
        while True:
            #self.pwd('pwd')
            cmd = input(">>").strip()
            if len(cmd) == 0: continue
            cmd_str = cmd.split()[0]
            if hasattr(self, cmd_str):
                func = getattr(self, cmd_str)
                func(cmd)
            else:
                self.help()

    def help(self):
        msg= '''
        仅支持如下命令：
         ls
         du
         pwd
         cd dirname/cd ./cd ..
         mkdir dirname
         rm  filename
         rmdir dirname
         mv filename/dirname filename/dirname  
         get filename [True] (True代表覆盖)
         put filename [True] (True代表覆盖)
         newget filename [o/r] (后续增加的新功能，支持断点续传,o代表覆盖，r代表断点续传)
         newput filename [o/r] (后续增加的新功能，支持断点续传,o代表覆盖，r代表断点续传)
        '''
        print(msg)

    def exec_linux_cmd(self,dict):
        self.client.send(json.dumps(dict).encode('utf-8'))
        server_reponse = json.loads(self.client.recv(4096).decode('utf-8'))
        if isinstance(server_reponse,list):
            for i in server_reponse:
                print(i)
        else:
            print(server_reponse)

    def pwd(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) == 1:
            msg = {'action': 'pwd'}
            self.exec_linux_cmd(msg)
        else:
            self.help()

    def ls(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) == 1:
            msg = {'action': 'ls'}
            self.exec_linux_cmd(msg)
        else:
            self.help()

    def du(self, *args):
        cmd_split = args[0].split()
        if len(cmd_split) == 1:
            msg = {'action': 'du'}
            self.exec_linux_cmd(msg)
        else:
            self.help()

    def cd(self, *args): ####切换目录
        cmd_split = args[0].split() ## 以空格为分隔符，包含 \n
        if len(cmd_split) == 1:
            dirname = ''
        elif len(cmd_split) == 2:
            dirname = cmd_split[1]
        else:
            self.help()
        msg = {
            "action": 'cd',
            "dirname": dirname
        }
        self.exec_linux_cmd(msg)

    def mkdir(self, *args):
        cmd_split = args[0].split()  ## 以空格为分隔符，包含 \n
        if len(cmd_split) == 2:
            dirname = cmd_split[1]
            msg = {
                "action": 'mkdir',
                "dirname": dirname
            }
            self.exec_linux_cmd(msg)
        else:
            help()


    def close(self):
        self.client.close()