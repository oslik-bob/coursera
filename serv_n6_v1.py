# =============================================================================
# import asyncio
# host=input('host')
# port=input("port")
#  
# 
# 
# 
# def run_server(host,port):
#     
#     loop = asyncio.get_event_loop()
#     coro = loop.create_server(ClientServerProtocol,host, int(port))
#     
#     server = loop.run_until_complete(coro)
#     try:
#         loop.run_forever()
#     except KeyboardInterrupt:
#         server.close()
#     
#     server.close()
#     loop.run_until_complete(server.wait_closed())
#     loop.close()
#         
# 
# 
# class ClientServerProtocol(asyncio.Protocol):
#     def connection_made(self, transport):
#         self.transport = transport
# 
#     def data_received(self, data):
#         resp = process_data(data.decode())
#         self.transport.write(resp.encode())
# 
# if __name__=='__main__':
#     run_server(host,port)
# =============================================================================

import asyncio
import logging
import concurrent.futures


def run_server(host, port):
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
    
    def __init__(self,metrix=dict()):
        self.metrix=metrix
    
    def connection_made(self, transport):
        self.transport = transport


    def data_received(self, data):
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

    run_server("127.0.0.1",8081)
