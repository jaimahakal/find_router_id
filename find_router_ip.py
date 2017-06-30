#!/usr/bin/python
from scapy.all import *
import netaddr
network='192.168.43.1/27' #make changes here for your subnet;
addresses=netaddr.IPNetwork(network)

for maa in addresses:
  if (maa==addresses.network or maa==addresses.broadcast):
    continue;
  send(IP(dst=str(maa))/ICMP())
  send(IP(dst='192.168.43.225')/ICMP()) 
