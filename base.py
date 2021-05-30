# -*- coding: utf-8 -*-
# @Time    : 2021/5/30 22:25
# @Author  : DL
# @Email   : 840806506@qq.com
# @File    : base.py
# @Software: PyCharm
# @ Describe: --------------------
#
#本地执行 ssh -keygen -t rsa ,将公钥拷贝到服务器端的 ~/.ssh/autorized_keys
#免密码远程登录执行命令
import paramiko
def DiskCheck(ip):
    try:
        #建立一个sshclient对象
        ssh = paramiko.SSHClient()
        #允许将信任的主机自动加入到host_allow列表，此方法只需放到connetct方法的前面
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #指定本地的RSA私钥文件，如果建立密钥对时设置的有密码，如无不用指定password参数
        # pkey = paramiko.RSAKey.from_private_key_file('/home/super/.ssh/id_rsa',password='123456')
        pkey = paramiko.RSAKey.from_private_key_file('home/keys/id_rsa')
        #建立连接
        ssh.connect(hostname=ip,
                    port=22,
                    username='root',
                    pkey=pkey)
        #执行命令
        stdin, stdout, stderr = ssh.exec_command("ls")
        #结果放到stdout中，如果有错误就将放在stderr中
        print(stdout.read.decode())
        print(stderr.read())
        #关闭连接
        ssh.close()
    except Exception as e:
        print(e)

#本地执行shell脚本
import shlex,time
import subprocess,datetime

def exexute_command(cmdstring,cwd=None,timeout=None,shell=False):
    if shell:
        cmdstring_list = cmdstring
    else:
        cmdstring_list = shlex.split(cmdstring)
    if timeout:
        end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
    sub = subprocess.Popen(cmdstring_list,cwd=cwd,stdin=subprocess.PIPE,shell=shell,bufsize=4096)
    # subprocess.poll():检查子进程是否结束了，结束了则返回码，放在subprocess.returnncode变量中
    while sub.poll() is None:
        time.sleep(0.1)
        if timeout:
            if end_time <= datetime.datetime.now():
                raise Exception("Timeout: %s" %cmdstring)
    return str(sub.returncode)
