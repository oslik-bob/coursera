#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 21:51:53 2021

@author: kali
"""
import socket
import threading

def process_request(conn,addr):
    print("conneckted client", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf8"))
            
with socket.socket() as sock:
    sock.bind(('',10001))
    sock.listen()
    while True:
        conn,addr=sock.accept()
        th=threading.Thread(target=process_request,args=(conn,addr))
        th.start()