#! /usr/bin/python

import signal
from getData import *
from checkConn import *

def handler(signum,frame):
    raise AssertionError

def Listen():
    try:
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(100)
        flag = checkConn();
        if flag == True:
            getData()
        signal.alarm(0)
    except AssertionError:
        exit(0)

if __name__ == "__main__":
    Listen()
