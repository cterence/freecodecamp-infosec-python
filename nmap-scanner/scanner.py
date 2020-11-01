#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple Nmap automation tool")
print("<--------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan : ")

print(f"You entered the IP address : {ip_addr}")

type(ip_addr)

resp = input(
    """
Please enter the type of scan you want to run
    1) SYN ACK Scan
    2) UDP Scan
    3) Comprehensive scan
"""
)

print(f"You have selected the option : {resp}\n")

if resp == "1":
    print(f"Nmap version : {scanner.nmap_version()}")
    scanner.scan(ip_addr, "1-1024", "--privileged -v -sS")
    print(scanner.scaninfo())
    print(f"IP status : {scanner[ip_addr].state()}")
    print(scanner[ip_addr].all_protocols())
    print(f"Open ports : {scanner[ip_addr]['tcp'].keys()}")

elif resp == "2":
    print(f"Nmap version : {scanner.nmap_version()}")
    scanner.scan(ip_addr, "1-1024", "--privileged -v -sU")
    print(scanner.scaninfo())
    print(f"IP status : {scanner[ip_addr].state()}")
    print(scanner[ip_addr].all_protocols())
    print(f"Open ports : {scanner[ip_addr]['udp'].keys()}")

elif resp == "3":
    print(f"Nmap version : {scanner.nmap_version()}")
    scanner.scan(ip_addr, "1-1024", "--privileged -v -sS -sV -sC -A -O")
    print(scanner.scaninfo())
    print(f"IP status : {scanner[ip_addr].state()}")
    print(scanner[ip_addr].all_protocols())
    print(f"Open ports : {scanner[ip_addr]['tcp'].keys()}")
elif resp >= "4":
    print("Please enter a valid option")