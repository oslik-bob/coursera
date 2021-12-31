#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:06:59 2021

@author: kali
"""
import socket
import time
# =============================================================================
# sock=socket.socket()
# sock.connect(('127.0.0.1', 10001))
# sock.sendall("ping".encode('utf8'))
# sock.close()
# =============================================================================

with socket.create_connection(('127.0.0.1', 10001),5) as sock:
    sock.settimeout(2)
    i=1000
    try:
        while True:
            i-=i
            sock.sendall(f"ping {i}".encode("utf8"))
            time.sleep(1)
    except socket.timeout:
        print("send data timeout")
    except socket.error as ex:
        print ("send data error:",ex)
