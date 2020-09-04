# encoding:utf8
import ftplib
from util.color import *

class FTP:
    def __init__(self, ip, port=21):
        self.ip = ip
        self.port = port

    def check(self):
        time_out_flag = 0
        for user in ['ftp', 'admin', 'www']:
            with open('./wordlist/ftp_pass.txt') as f:
                for line in f.readlines():
                    pwd = line.strip()
                    try:
                        ftp = ftplib.FTP()
                        ftp.timeout = 5

                        ftp.connect(self.ip, self.port)
                        if ftp.login(user, pwd).startswith('2'):
                            return blue + "[+] {0}:{1} -> {2}:{3}".format(self.ip, self.port, user, pwd) + end
                    except Exception as e:
                        if not str(e).startswith('530'):
                            print(e)
                        if e.args[0] == 113 or e.args[0] == 111 or 'timed out' in str(e):
                            time_out_flag += 1
                        if time_out_flag > 2:
                            print('connection timeout , break the loop .')
                            return False
                        else:
                            pass
        return False
