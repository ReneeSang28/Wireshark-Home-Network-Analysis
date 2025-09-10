'''to analyse the incoming packets'''
import pyshark

# Load the Wireshark capture file
cap = pyshark.FileCapture("home_network.pcapng")

print("First 10 packets in your capture:\n")
for i, packet in enumerate(cap):
    if i == 10:  # stop after 10 packets
        break
    print(f"Packet {i+1}:")
    print(packet)
    print("="*60)
