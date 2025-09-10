'''To count the protocol usage'''
from collections import Counter
import pyshark

cap = pyshark.FileCapture("home_network.pcapng")
protocols = Counter()

for packet in cap:
    protocols[packet.highest_layer] += 1

print("\nProtocol Counts:")
for proto, count in protocols.most_common(10):
    print(f"{proto}: {count}")
