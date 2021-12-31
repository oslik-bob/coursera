import socket
# =============================================================================
# без контекстного менеджера
#
# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.bind(('127.0.0.1',10001))
# sock.listen(socket.SOMAXCONN) #длинна очереди
# 
# conn, addr = sock.accept() # 
# 
# while True:
#     data=conn.recv(1024)
#     if not data:
#         break
#     print(data.decode('utf8'))
# conn.close()
# sock.close()
# 
# =============================================================================

#C контекстным менеджером



with socket.socket() as sock:
    sock.bind(("127.0.0.1",10001))
    sock.listen()
    
    while True:
        conn, addr = sock.accept()
        conn.settimeout(5) #timeout=None|0|gt 0
        with conn:
            try:
                data = conn.recv(1024)
            except socket.timeout:
                print("close connecton bu timeout")
                break
            if not data:
                break
            print(data.decode('utf8'))
