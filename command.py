# import os
# import time

# os.system("ls")
# os.system("scp qb2@172.20.10.2:/home/qb2/helloworld.py .")
# time.sleep(0.5)
# os.system("utaa")


# import subprocess

# subprocess.call('echo "utaa" | scp qb2@172.20.10.2:/home/qb2/helloworld.py .',shell=True)


# import pexpect

# PASSWORD = "utaa"
# scp = pexpect.spawn("scp qb2@172.20.10.2:/home/qb2/helloworld.py .")
# scp.expect('.ssword:*')
# scp.sendline(PASSWORD)
# scp.interact()

# import subprocess

# subprocess.call('sshpass -p 'utaa' scp -o StrictHostKeyChecking=no qb2@172.20.10.2:/home/qb2/helloworld.py .',shell=True)

# sshpass -p 'password' ssh -o StrictHostKeyChecking=no user@host 'command'
# sshpass -p 'password' scp -o StrictHostKeyChecking=no localfile user@host:/path/to/copy



import pexpect.popen_spawn as psp

scp = psp.PopenSpawn("scp qb2@172.20.10.2:/home/qb2/helloworld.py .")
scp.expect('password:*')
scp.sendline('utaa')
print(scp.readlines())
# class WinPexpect():
#     def __init__(self,cmd,pswd):
#         self.process = psp.PopenSpawn(cmd)
#         self.prompt = ">"
#         try:
#             self.process.expect('.ssword:*', timeout=10)
#         except:
#             Exception("cmd expect fail")
#         print(self.cmd_readlines())

#     def cmd_readlines(self):
#         res = ""
#         res = self.process.before.decode("shift-jis", errors="ignore") + self.process.after.decode("shift-jis", errors="ignore")
#         self.prompt = res.splitlines()[-1]
#         self.prompt = self.prompt.replace("\\", "\\\\")
#         return res

#     def cmd_sendline(self, cmd, timeout=10):
#         self.process.sendline(cmd)
#         if cmd.find("cd ") > -1:
#             self.prompt = self.prompt[:-1] + "\\\\" + cmd.split("cd ")[1] + ">"
#         try:
#             self.process.expect(self.prompt, timeout=timeout)
#             return True
#         except:
#             import traceback
#             traceback.print_exc()
#             return False

# if __name__ == '__main__':
#     wincmd = WinPexpect()
#     wincmd.cmd_sendline("dir")
#     print(wincmd.cmd_readlines())
#     wincmd.cmd_sendline(" cd log")
#     print(wincmd.cmd_readlines())
