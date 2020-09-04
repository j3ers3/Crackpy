# encoding:utf8
import requests
from util.color import *

class TOMCAT:
    def __init__(self, ip, port=8080):
        self.ip = ip
        self.port = port


    def check(self):
        url = 'http://'+self.ip+':'+str(self.port)+'/manager/html/'

        for user in ['admin', 'tomcat']:
            with open('./wordlist/top100.txt') as f:
                for line in f.readlines():
                    pwd = line.rstrip()
                    auth = (user, pwd)
                    try:
                        r = requests.get(url, auth=auth, timeout=8)
                        if r.status_code == 200:
                            return blue + "[+] {0}:{1} -> {2}:{3}".format(self.ip, self.port, user, pwd) + end
                    except Exception as e:
                        #print(e)
                        pass
        return False
