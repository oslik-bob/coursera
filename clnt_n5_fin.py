''' 
запрос <команда> <данные запроса><\n>
Put -save on server 
get - get 
 <\n> - символ переноса строки.
 
ответ <статус ответа><\n><данные ответа><\n\n> 
ok» - команда успешно выполнена на сервере
«error» - выполнение команды завершилось ошибкой
 <\n\n> - два символа переноса строки.

 '''
from time import time
import socket
import bisect

class ClientError(Exception):
    pass

class Client:
    def __init__(self, host, port,timeout=None):
        self.host_ip = host
        self.port = port
        self.timeout = timeout
        try:
            self.connection=socket.create_connection((self.host_ip,self.port),timeout)
        except socket.error as error:
            raise ClientError ("ошибка соединения",error)
    
    def snd(self,val):
        try:
            self.connection.send(val)
        except socket.error as error:
            raise ClientError('error on send',error)
    
    def resive(self):
        res=b''
        while not res.endswith(b'\n\n'):
            try:
                res+= self.connection.recv(1024)
                return res
            except socket.error as error:
                raise ClientError ('error resive data from server')


    def get(self,val):
        message=f'get {val}\n'
        self.snd(message.encode())
        res=self.resive().decode()
        
        try:
            stat,*midl,_,_=res.split('\n')
            if stat != "ok":
                raise ClientError()
            if not midl:
                return {}
            ddict={}
            for i in midl:
                if len(i.split(' '))==3:
                    key,met,time=i.split(' ')
                    if key not in ddict:
                        ddict[key]=[]
                    bisect.insort(ddict[key], ((int(time), float(met))))                  
                else:
                    raise ClientError()
        except:
            raise ClientError
        else:
            return ddict
    
    
    def put(self, metrics,value,timestamp=None):
        timestamp=int(timestamp) if timestamp else int(time())
        messages=f'put {metrics} {value} {timestamp}\n'
        self.snd(messages.encode())
        res=self.resive().decode()
        if res not in 'ok\n\n':
            raise ClientError ('server not return ok')
