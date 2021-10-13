# 主要用于运维过程中一些老设备找不到IP地址，可以用此工具，找到该设备IP或者是否处于DHCP状态  
准备工作，电脑网口直连设备网口
1、打开软件  
2、选择网卡  
3、软件抓包，如果该设备已经设置IP地址，可以通过ARP包中的who is来找到该IP地址  
4、如果该设备设置的DHCP。可以通过抓包过程中的dhcp广播判断是否在请求IP  
![Image text](https://github.com/trz0332/find_ip/blob/main/%E6%8D%95%E8%8E%B7.PNG)  
