'''To Print the Packet Summary'''
import pyshark

cap = pyshark.FileCapture("home_network.pcapng")

print("First 10 packets summary:\n")
for i, packet in enumerate(cap):
    if i == 10:
        break
    try:
        print(f"Packet {i+1}: {packet.highest_layer} | {packet.ip.src} → {packet.ip.dst} | Protocol: {packet.transport_layer}")
    except AttributeError:
        # some packets don’t have IP/transport layers
        print(f"Packet {i+1}: {packet.highest_layer}")
