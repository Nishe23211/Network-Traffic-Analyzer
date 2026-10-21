
from scapy.all import sniff, IP, TCP, UDP
import pandas as pd
from datetime import datetime

packets_data = []

def analyze_packet(packet):
    if IP in packet:

        protocol = "OTHER"

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"

        packet_info = {
            "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Source IP": packet[IP].src,
            "Destination IP": packet[IP].dst,
            "Protocol": protocol,
            "Packet Size": len(packet)
        }

        packets_data.append(packet_info)

        print(packet_info)

print("Starting Network Traffic Analyzer...")

sniff(prn=analyze_packet, count=100, store=False)

df = pd.DataFrame(packets_data)

df.to_csv("traffic.csv", index=False)

print("Network traffic saved to traffic.csv")
