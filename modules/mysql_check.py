# encoding:utf8
import pymysql
from rich.progress import track
from util.color import *

class MYSQL:
    def __init__(self, ip, port=3306):
        self.ip = ip
        self.port = port
 

    def check(self):
        for user in ['root']:
            with open('./wordlist/mysql_pass.txt') as f:
                for line in track(f.readlines()):
                    pwd = line.rstrip()
            
                    try:
                        pymysql.connect(host=self.ip, port=self.port, user=user, password=pwd, connect_timeout=2)
                        return blue + "[+] {0}:{1} -> {2}:{3}".format(self.ip, self.port, user, pwd) + end
                    except Exception as e:
                        #print(e)
                        pass
        return False