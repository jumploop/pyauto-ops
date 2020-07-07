from pexpect import pxssh
import getpass

try:
    s = pxssh.pxssh() #创建pxssh对象
    hostname = input('hostname: ')
    username = input('username: ')
    password = getpass.getpass('password: ')  #接收密码输入
    s.login(hostname, username, password) #建立ssh连接
    s.sendline('uptime')  # run a command #运行uptime命令
    s.prompt()  # match the prompt #匹配系统提示符
    print(s.before)  # print everything before the prompt.  #打印出现系统提示符前的命令输出
    s.sendline('ls -l') #运行命令
    s.prompt()#匹配系统提示符
    print(s.before) #打印出现系统提示符前的命令输出
    s.sendline('df')#运行命令
    s.prompt()#匹配系统提示符
    print(s.before)#打印出现系统提示符前的命令输出
    s.logout() #断开ssh连接
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(str(e))
