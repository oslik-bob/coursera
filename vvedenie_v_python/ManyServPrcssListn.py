#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 22:56:47 2021

@author: kali
"""
import socket
import multiprocess
import threading

    
def process_request(conn,addr):
    print("conneckted client", addr)
                                         # Поток для обработки соединения 
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf8"))
            
            
def worker(sock):
    while True:
                                     # accept распределится "равномерно" между процессами
        conn,addr=sock.accept()
        th=threading.Thread(target=process_request,args=(conn,addr))
        th.start()
                 

with socket.socket() as sock:
    
    sock.bind(('',10001))
    sock.listen()
                                     # создание нескольких процессов
    workers_count = 3
    workers_list = [multiprocess.Process(target=worker, args=(sock,)) 
                     for _ in range(workers_count)]
    for w in workers_list:
         w.start()
         
    for w in workers_list:
        w.join()


     