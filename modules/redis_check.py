# encoding:utf8
import socket
from util.color import *

class REDIS:
    def __init__(self, ip, port=6379):
        self.ip = ip
        self.port = port
 

    def check(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((self.ip, int(self.port)))
            s.send("INFO\r\n".encode())
            result = s.recv(1024).decode(encoding='utf-8')
        
            if "redis_version" in result:
                return purple + "[+] {0}:{1} -> 未授权访问".format(self.ip, self.port) + end

            # 简单弱口令检测
            elif "Authentication" in result:
                with open('./wordlist/redis_pass.txt') as f:
                    for line in f.readlines():
                        pwd = line.rstrip()   
               
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((self.ip, int(self.port)))
                        s.send("AUTH {0}\r\n".format(pwd).encode())

                        result = s.recv(1024).decode(encoding='utf-8')

                        if "OK" in result:
                            return blue + "[+] {0}:{1} -> 弱口令：{2}".format(self.ip, self.port, pwd) + end
            s.close()
        except Exception as e:
            pass

        return False
