#!/usr/bin/env python
import scapy.all as scapy


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)  # create arp packet object (class)
    broadcast_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # create ether net frame
    broadcast_arp_request = broadcast_request / arp_request
    answered_list = scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]  # srp for custom packet

    return answered_list[0][1].hwsrc    # target's mac address


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)  # don't store in memory
    # throw into the prn function every time


def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        try:
            real_mac = get_mac(packet[scapy.ARP].psrc)
            response_mac = packet[scapy.ARP].hwsrc
            if response_mac != real_mac:
                print("[+] YOU ARE UNDER ATTACK !!!")
        except IndexError:
            pass


sniff("eth0")
# print(packet.show())  # to find the field

