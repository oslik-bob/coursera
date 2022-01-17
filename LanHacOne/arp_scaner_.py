"""import click
import scapy.all as sc
from scapy.config import conf
import asyncio

conf.verb = 0


@click.command()
@click.option('--ip', '-m', multiple=True)
def scan_local_network(ip):
    #запуск сервера
    loop = asyncio.get_event_loop()
    for _ in ip:
        coro = loop.create_task(scan(ip))

        server = loop.run_until_complete(coro)
    #server.

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


def scan(ip):

    ether_layer = sc.Ether(dst="ff:ff:ff:ff:ff:ff")

    for _ in ip:
        try:
            arp_layer = sc.ARP(pdst=_)
            arp_request = ether_layer / arp_layer
            answered = sc.srp(arp_request, timeout=10)[0]
            result = 'available' if answered else 'not available'
        except:
            print('bag')
            result = 'not available'
        finally:
            print(f'{_.ljust(15)}| {result}')
        
if __name__ == "__main__":
    scan_local_network()



"""
import multiprocessing as mp
import click
import scapy.all as sc
from scapy.config import conf

conf.verb = 0

@click.command()
@click.option('--ip', multiple=True)
def scan_local_network(ip):
        
    procs = [mp.Process(target=scan, args=(i,)) for i in ip] # создаем столько процессов, сколько имеем функций
    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()

def scan(ip):

    ether_layer = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_layer = sc.ARP(pdst=ip)
    arp_request = ether_layer / arp_layer
    answered = sc.srp(arp_request, timeout=10)[0]
    result = 'available' if answered else 'not available'
    print(f'{ip}| {result}')
        
if __name__ == "__main__":
    scan_local_network()
