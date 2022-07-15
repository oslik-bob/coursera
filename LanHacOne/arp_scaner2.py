import click
import scapy.all as sc
from scapy.config import conf
from multiprocessing.dummy import Pool as mp

class AsinTest():
    def __init__(self, ip_adress,time_out=0.5) -> None:
        self.ip_adress=ip_adress
        self.ether_layer = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
        self.arp_layer = sc.ARP(pdst=ip_adress)
        self.arp_request = self.ether_layer / self.arp_layer
        self.time_out=time_out
        self.answered = sc.srp(self.arp_request, timeout=self.time_out)

    def get_laer(self,):
        if self.answered[0]:
            return f'{self.ip_adress}| {sc.getmacbyip(self.ip_adress)}'


conf.verb = 0

all=[]

@click.command()
@click.option('-s', multiple=False)
@click.option('-e', multiple=False)
def scan_local_network(**kwargs):
    if kwargs:
        ip_strt, ip_end=[kwargs[i] for i in kwargs]
    if not ip_end:
        a=AsinTest(ip_strt).get_laer()
        print(a)
        return AsinTest(ip_strt).get_laer()

    ip_end = ip_end.split('.')[-1]
    ip_strt = [i for i in ip_strt.split('.')]

    if ip_end == ip_strt[-1]:
        return AsinTest(ip_strt).get_laer()
    elif ip_end>ip_strt[-1]:
        func_lmbda = lambda x: AsinTest(x).get_laer()
        tuple_scan_addr =[f'{".".join(ip_strt[0:3])}.{i}'
            for i in range(int(ip_strt[-1]),int(ip_end)+1)]
        pool=mp(len(tuple_scan_addr))
        procs = pool.map(func_lmbda, tuple_scan_addr)
        pool.close()
        pool.join()
        all.extend([i for i in procs if i])
        
        print(all)
    else:
        print('ниправельный порядок')
        exit()
    

if __name__=="__main__":
    scan_local_network()

