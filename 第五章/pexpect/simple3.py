import pexpect
import sys

ip = "192.168.1.21"
user = "root"
passwd = "H6DSY#*$df32"
target_file = "/data/logs/nginx_access.log"

child = pexpect.spawn('/usr/bin/ssh', [user + '@' + ip])
fout = open('mylog.txt', 'w')
child.logfile = fout

try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect('#')
    child.sendline('tar -czf /data/nginx_access.tar.gz ' + target_file)
    child.expect('#')
    print(child.before)
    child.sendline('exit')
    fout.close()
except pexpect.EOF:
    print("expect EOF")
except pexpect.TIMEOUT:
    print("expect TIMEOUT")

child = pexpect.spawn('/usr/bin/scp', [user + '@' + ip + ':/data/nginx_access.tar.gz', '/home'])
fout = open('mylog.txt', 'a')
child.logfile = fout
try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect(pexpect.EOF)
except pexpect.EOF:
    print("expect EOF")
except pexpect.TIMEOUT:
    print("expect TIMEOUT")
