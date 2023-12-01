from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

devices = []  # Create Empty list for holding devices

# For loop to create large number of devices

for index in range(1, 10):

    # Create device dictionary
    device = {}

    # Random Device Name
    device["name"] = (
        choice(['r2', 'r3', 'r4', 'r6', 'r10'])
        + choice(['L', 'U'])
        + choice(string.ascii_letters)
    )

    device['vendor'] = choice(['cisco', 'juniper', 'arista'])
    if device['vendor'] == 'cisco':
        device['os'] = choice(['ios', 'iosxe', 'iosxr', 'nexus'])
        device['version'] = choice(['12.1(T).04', '14.07X', '8.12(S).010'])
    elif device['vendor'] == 'juniper':
        device['os'] = 'junos'
        device['version'] = choice(['J6.23.1', '8.43.12', '6.45', '6.03'])
    elif device['vendor'] == 'arista':
        device['os'] = 'eos'
        device['version'] = choice(['2.45', '2.55', '2.92.145', '3.01'])
    device['ip'] = '10.0.0' + str(index)

    print()
    for key, value in device.items():
        print(f"{key:>16s} : {value}")
    devices.append(device)

print("\n----- Devices as LIST of Dicts-----")
pprint(devices)

# USE 'TABULATE' TO PRINT TABLE OF DEVICES
print("\n------- SORTED LIST IN TABULAR FORMAT-----")
print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers='keys'))
