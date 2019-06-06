#!/usr/bin/sh python


import scapy.all as scapy


# create ether net frame and append arp request later on
def scan(ip):
    # scapy.arping(ip)

    arp_request = scapy.ARP(pdst=ip)    # create arp packet object (class)
    broadcast_request = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")    # create ether net frame
    broadcast_arp_request = broadcast_request / arp_request
    answered = scapy.srp(broadcast_arp_request, timeout=1, verbose=0)[0]  # srp for custom packet


    client_list = []
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


result_scan = scan("10.0.2.1/24")
print_result(result_scan)