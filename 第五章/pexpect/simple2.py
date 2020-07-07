from __future__ import unicode_literals	#使用unicode编码

import pexpect
import sys

child = pexpect.spawnu('ftp ftp.openbsd.org')
child.expect('(?i)name .*: ') #(?i)忽略大小写
child.sendline('anonymous')
child.expect('(?i)password')
child.sendline('pexpect@sourceforge.net')
child.expect('ftp> ')
child.sendline('bin') #开启二进制传输
child.expect('ftp> ')
child.sendline('get robots.txt')
child.expect('ftp> ')
sys.stdout.write (child.before)
print("Escape character is '^]'.\n")
sys.stdout.write (child.after)
sys.stdout.flush()
child.interact() # Escape character defaults to ^]
child.sendline('bye')
child.close()
