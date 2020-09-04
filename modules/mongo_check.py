# encoding:utf8
from util.color import *
import socket
import binascii

class MONGO:
    def __init__(self, ip, port=27017):
        self.ip = ip
        self.port = port

    def check(self):
        try:
            socket.setdefaulttimeout(2)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.ip, int(self.port)))
            data = binascii.a2b_hex("3a000000a741000000000000d40700000000000061646d696e2e24636d640000000000ffffffff130000001069736d6173746572000100000000")
            s.send(data)
            res = s.recv(1024)

            if "ismaster" in str(res):
                getlog_data = binascii.a2b_hex("480000000200000000000000d40700000000000061646d696e2e24636d6400000000000100000021000000026765744c6f670010000000737461727475705761726e696e67730000")
                s.send(getlog_data)
                res = s.recv(1024)
                if "totalLinesWritten" in str(res):
                    return purple + "[+] {0}:{1} -> 未授权访问".format(self.ip, self.port) + end
                else:
                    return False
        except Exception as e:
            #print(e)
            return False