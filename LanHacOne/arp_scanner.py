import multiprocessing as mp
import click
import scapy.all as sc
from scapy.config import conf

conf.verb = 0

@click.command()
@click.option('-ip', multiple=True)
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
    print(f'{ip} |{result}')
        
if __name__ == "__main__":
    scan_local_network()
