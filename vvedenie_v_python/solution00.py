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

class ClientError(Exception):
    pass

class Client:
    
    def __init__(self, host, port,timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        try:
            self.connection=socket.create_connection((self.host,self.port),timeout)
        except socket.error as error:
            raise ClientError ("ошибка соединения",error)
        
         
         
    def get():
        pass
    
    
    def put(self, metrics,value,timestamp=None):
        timestamp=timestamp if timestamp else int(time())
        
        
    
    