# encoding:utf8
from paramiko import SSHClient, AutoAddPolicy
from rich.progress import track
from util.color import *

class SSH:
    def __init__(self, ip, port=22):
        self.ip = ip
        self.port = port

    def check(self):
      
        client = SSHClient()
        client.set_missing_host_key_policy(AutoAddPolicy())

        time_out_flag = 0
        
        for user in ['root', 'appadmin']:
            with open('./wordlist/ssh_pass.txt') as f:
                
                for line in track(f.readlines()):
                    pwd = line.strip()
  
                    try:
                        client.connect(self.ip, self.port, user, pwd, timeout=5, auth_timeout=10)
                        return blue + "[+] {0}:{1} -> {2}:{3}".format(self.ip, self.port, user, pwd) + end
                    except Exception as e:
                        pass
  
        return False
