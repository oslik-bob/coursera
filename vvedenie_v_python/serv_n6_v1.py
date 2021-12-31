import asyncio
import re


def run_server(host, port):
    #запуск сервера
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port)

    server = loop.run_until_complete(coro)
    #server.

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class ClientServerProtocol(asyncio.Protocol):
    
<<<<<<< HEAD
    def __init__(self,metrix=dict()):
        self.metrix=metrix
    
=======
    def __init__(self, meta_rec=dict()):
        self.meta_rec=meta_rec
        
        
>>>>>>> 281a3def2e0e71b8c2d5b4df47caff5321d01293
    def connection_made(self, transport):
        self.transport = transport


    def data_received(self, data):
<<<<<<< HEAD
        resp = self.data_decode(data)
        

            #self.transport.write(resp)

    def data_decode(self, data):
        try:
            data=data.decode()
            comm,metrix,*value=data.split(' ')
            if comm =='put':
                if metrix in self.metrix:
                    self.metrix[metrix].append(value)
                    print (self.metrix)
                else:
                    self.metrix[metrix]=[value]
                    print (self.metrix)
            elif comm == 'get':
                
                print(comm)
            else: raise ValueError
        except ValueError:
            print('ValueError')
        else:
            print("else try")
        return data    
    
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
=======
        print(data.decode('utf8'))
        resp = self.process_data(data.decode())
        
        self.transport.write(resp.encode())
        
    
    def add_val(self, meta, val):
        if meta in self.meta_rec:
            if val in self.meta_rec[meta]:
                return True

            for i in self.meta_rec[meta]:
                if val[1] in i:
                    self.meta_rec[meta][self.meta_rec[meta].index(i)]=val
                    return True
            
            #elif not all([False for i in self.meta_rec[meta] if val[1] in i]):
            #    return
            self.meta_rec[meta].append(val)
            return True
        else:
            self.meta_rec[meta]=[val]
            return True
        
            
    def _get_all(self):
        result=''
        for k in self.meta_rec.keys():
            result+=self._get_one(k)
        return result
    
    
    def _get_one(self,meta):
        result=''
        if not meta in self.meta_rec.keys():
            return ''

        for i in self.meta_rec[meta]:
            result+=f'{meta} {i[0]} {i[1]}\n'
        return result
        
    def check(self,chk):
        if chk.isdigit():
            return True
        else: return bool(re.findall("\d+\.\d+", chk))

    def process_data(self, data):
        """Принимает строку <<комм ключ данные временная_метка>> 
        проверяет значения где комм == put или get (строка)
        ключ = ключ для поиска к данным словаря (строка)
        данные==дфанные метрики (дробное число)
        временная метка (число)"""
        try:

            if (data.split()[0]) not in ('put', 'get'):
                raise ValueError
            
            if data.split()[0] == 'put':
                _, meta,*val=data.split()
                if not all((
                    len(val)==2,
                    self.check(val[0]),
                    val[1].isdigit()
                    )):
                    raise ValueError
                else:
                    val[0]=float(val[0])
                    val[1]= int(val[1])
                    if not self.add_val(meta,val):
                       raise ValueError 
    
            elif data.split()[0] == 'get':
                _, meta=data.split()
                met=meta.strip('\n\r ')
>>>>>>> 281a3def2e0e71b8c2d5b4df47caff5321d01293

                if str(met).strip("\r \n")=='*':
                    return 'ok\n'+self._get_all()+'\n'
                elif len(met)>1:
                    return 'ok\n'+self._get_one(met.split("\\")[0])+'\n'
                else: raise ValueError
                    
            else:
                raise ValueError
        except:
            return'error\nwrong command\n\n'
        else:
            return "ok\n\n"
            

if __name__ == '__main__':
    
    run_server("127.0.0.1",8081)