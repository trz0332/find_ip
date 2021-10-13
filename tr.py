from scapy.all import *
import argparse
dev={}


def arp_monitor_callback(pkt):
    global dev
    #if ARP in pkt :
    #print(pkt.show() )
    if ARP in pkt and pkt[ARP].op in (1,2):
        #print(pkt.show())
        hwsrc=pkt.src
        psrc=pkt[ARP].psrc
        if hwsrc not in dev.keys():
            dev[hwsrc] =psrc
            print("找到新设备MAC：{}\n找到新设备IP:{}".format(hwsrc,psrc))
        else :
            if dev[hwsrc]!=psrc:
                dev[hwsrc] =psrc
                print("找到新设备MAC：{}\n找到新设备IP:{}".format(hwsrc,psrc))
                

    elif DHCP in pkt:
        hwsrc=pkt.src
        if hwsrc not in dev.keys():
            dev[hwsrc] =''
            print('该设备为自动获取IP,MAC地址为{}，请接入路由器来获取IP'.format(hwsrc))
        else :
            if dev[hwsrc]!='':
                dev[hwsrc] =''
                print('该设备为自动获取IP,MAC地址为{}，请接入路由器来获取IP'.format(hwsrc))

def manage(pkt):
    print(pkt.show())
    if pkt.haslayer(DHCP):
        req_type = [x[1] for x in pkt[DHCP].options if x[0] == 'message-type'][0]
        print('dhcp')
     
if __name__ == '__main__':
    z=IFACES.data
    dev_name=[]
    dev_ip=[]
    dev_mac=[]
    print('输入数字选择网卡')
    print('输入《0》，程序直接退出')
    x=1
    for i in z:
        #print(z[i].ip,z[i].mac)
        dev_name.append(z[i].name)
        dev_ip.append(z[i].ip)
        dev_mac.append(z[i].mac)
        print("输入《{}》，监听网卡<{}>的数据包".format(x,z[i].name))
        x+=1
    unz=100
    while unz not in list(range(len(dev_name)+1)):
        unz=input("请选择：")
        try :
            unz=int(unz)
        except:
            print('请输入数字')
        else :
            if unz ==0:
                exit()
            elif unz in list(range(1,len(dev_name)+1)):
                print('已经选择网卡<{}>，IP地址为{},MAC地址为{}，准备抓包'.format(dev_name[unz-1],dev_ip[unz-1],dev_mac[unz-1]))
                sniff(prn=arp_monitor_callback,iface=dev_name[unz-1], store=0)
            else:
                print('请重新输入')
