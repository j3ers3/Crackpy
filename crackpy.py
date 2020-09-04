#!/usr/bin/env python3
# encoding:utf8
import argparse
import asyncio
import time
from util.color import *
from rich.progress import track
from modules.mysql_check import MYSQL
from modules.redis_check import REDIS
from modules.ssh_check import SSH
from modules.mongo_check import MONGO
from modules.tomcat_check import TOMCAT
from modules.ftp_check import FTP

##########################################################

__version__ = "0.1"
__prog__ = "Crackpy"
__author__ = "whois"
__create_date__ = "2020 08 25"
__update_date__ = "2020 08 25"

##########################################################



banner = blue + """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

 ██████╗██████╗  █████╗  ██████╗██╗  ██╗██████╗ ██╗   ██╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔══██╗╚██╗ ██╔╝
██║     ██████╔╝███████║██║     █████╔╝ ██████╔╝ ╚████╔╝ 
██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔═══╝   ╚██╔╝  
╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗██║        ██║   
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝        ╚═╝   
                                                        \n""" + purple2 + """

                                    Crackpy Ver. {0}
                                    Update {1}
                                    Coded by {2}\n""".format(__version__, __update_date__, __author__) + blue + """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n""" + end


def url_list(urlfile):
    with open(urlfile, 'r') as f:
        f = [line.rstrip() for line in f.readlines()]
    return f


def main():
    print(banner)
    parser = argparse.ArgumentParser(
        usage='Crackpy -m mysql -f ip.txt',
        description="Password Check",
    )


    mod = parser.add_argument_group('MODULES')

    mod.add_argument("-m", dest="module",
                      help="Speciy module [mysql|redis|mongo|ftp|ssh|telnet]")

    misc = parser.add_argument_group('MISC')
    misc.add_argument("-f", dest="ipfile",
                      help="Speciy host file [1.1.1.1:3306]")
    misc.add_argument("-x", dest="host",
                      help="Specify single host [1.1.1.1:3306]")

    #misc.add_argument("-t", dest="threads", type=int, default=20,help="Set thread (default 20)")

    args = parser.parse_args()

    if args.ipfile is None and args.host is None:
        print("[x] Crackpy -h")
        exit(0)

    if args.module == 'mysql':
        if args.host:
            # 判断格式，可以是1.1.1.1:3306，也可以是默认端口
            m = MYSQL(args.host.split(':')[0], int(args.host.split(':')[1])) if ':' in args.host else MYSQL(args.host.split(':')[0])
            res = m.check()
            print(res)
        
        elif args.ipfile:
            for host in url_list(args.ipfile):
                m = MYSQL(host.split(':')[0], int(host.split(':')[1])) if ':' in host else MYSQL(host.split(':')[0])
                res = m.check()
                print(res)
                    

    elif args.module == 'redis':
        if args.host:
            m = REDIS(args.host.split(':')[0], int(args.host.split(':')[1])) if ':' in args.host else REDIS(args.host.split(':')[0])
            res = m.check()
            print(res)

        elif args.ipfile:
            for host in track(url_list(args.ipfile)):
                m = REDIS(host.split(':')[0], int(host.split(':')[1])) if ':' in host else REDIS(host.split(':')[0])
                res = m.check()
                print(res)


    elif args.module == 'ssh':
        if args.host:
            m = SSH(args.host.split(':')[0], int(args.host.split(':')[1])) if ':' in args.host else SSH(args.host.split(':')[0])
            res = m.check()
            print(res)

        elif args.ipfile:
            for host in url_list(args.ipfile):
                m = SSH(host.split(':')[0], int(host.split(':')[1])) if ':' in host else SSH(host.split(':')[0])
                res = m.check()
                print(res)

    elif args.module == 'mongo':
        if args.host:
            m = MONGO(args.host.split(':')[0], int(args.host.split(':')[1])) if ':' in args.host else MONGO(args.host.split(':')[0])
            res = m.check()
            print(res)

        elif args.ipfile:
            for host in track(url_list(args.ipfile)):
                m = MONGO(host.split(':')[0], int(host.split(':')[1])) if ':' in host else MONGO(host.split(':')[0])
                res = m.check()
                print(res)

    elif args.module == 'ftp':
        if args.host:
            m = FTP(args.host.split(':')[0], int(args.host.split(':')[1])) if ':' in args.host else FTP(args.host.split(':')[0])
            res = m.check()
            print(res)

        elif args.ipfile:
            for host in track(url_list(args.ipfile)):
                m = FTP(host.split(':')[0], int(host.split(':')[1])) if ':' in host else FTP(host.split(':')[0])
                res = m.check()
                print(res)

    elif args.module == 'tomcat':
        if args.host:
            m = TOMCAT(args.host.split(':')[0], int(args.host.split(':')[1])) if ':' in args.host else TOMCAT(args.host.split(':')[0])
            res = m.check()
            print(res)

        elif args.ipfile:
            for host in track(url_list(args.ipfile)):
                m = TOMCAT(host.split(':')[0], int(host.split(':')[1])) if ':' in host else TOMCAT(host.split(':')[0])
                res = m.check()
                print(res)

    else:
        print("[x] Modules dont exist !!!")


if __name__ == '__main__':
    main()
            


