#!/usr/bin/sh python


import scapy.all as scapy
import argparse


def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP address to scan")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a interface. Use --help for more information.")

    # parser.parse_args() is tuple
    return options


# create ether net frame and append arp request later on
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)    # create arp packet object (class)
    broadcast_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")    # create ether net frame
    broadcast_arp_request = broadcast_request / arp_request
    answered = scapy.srp(broadcast_arp_request, timeout=1, verbose=0)[0]  # srp for custom packet

    client_list = []
    # element(request, answer)
    for element in answered:
        client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
        client_list.append(client_dict)
        # print(element[1].psrc + "\t\t" + element[1].hwsrc)

    return client_list


def print_result(client_list):
    print("IP\t\t\tMAC\n---------------------------------------------------------------------")
    for client in client_list:
        print(client["ip"]+"\t\t"+client["mac"])


    # print(answered[0])
    # print(answered.summary())
    # print(unanswered.summary())

    # arp_request.show()
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP)     # ls scapy.arp options

    # in network pass by mac not ip
    # broadcast_request.show()
    # print(broadcast_request.summary())
    # scapy.ls(scapy.Ether())

    # broadcast mac will always be 6 ff
    # broadcast_arp_request.show()

options = get_argument()
result_scan = scan(options.target)
print_result(result_scan)
