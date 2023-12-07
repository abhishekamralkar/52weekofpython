from l_03_functions import create_devices
from operator import itemgetter
from tabulate import tabulate
from datetime import datetime
from random import choice
import nmap
from pprint import pprint
from time import sleep

devices = create_devices(25)

print("\n\nUSING PRINT")
print(devices)

print("\n\nUSING PPRINT")
pprint(devices)

print("\n\nUSING LOOP")
for device in devices:
    sleep(0.1)
    device["last_heard"] = str(datetime.now())
    print(device)

print("\n\nUSING TABULATE")
print(
    tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys")
)
print("\n\nUSING LOOP AND F-STRING")
print("   NAME      VENDOR : OS  IP ADDRESS LAST_HEARD    ")
print("  -------------- -------------- ----------- ---------------")
for device in devices:
    print(
        f'{device["name"]:>7}  {device["vendor"]:>10} {device["os"]:>6}   {device["ip"]:>10} {device["last_heard"]}'
    )

print("\nSame thing, but sorted descending by last_jeard")
for device in sorted(devices, key=itemgetter("last_heard"), reverse=True):
    print(
        f'{device["name"]:>7}  {device["vendor"]:>10} {device["os"]:>6}   {device["ip"]:>10} {device["last_heard"]}'
    )

print("\n\nMULTIPLE PRINT STATEMENT, SAME LINE")
print("Testing Devices:")
for device in devices:
    print(f"---testing devices {device['name']} ...",end="")
    sleep(choice([0.1,0.2,0.3,0.4]))
    print("done")
print("Testing completed")

nm = nmap.PortScanner()
while True:

    ip = input("\nInput IP address to scan:")
    if not ip:
        break

    print(f"\n---beginning {ip} scan")
    output = nm.scan(ip, '22-1024')
    print(f"--- --- command: {nm.command_line()}")

    print("---------nmap scan output------")
    pprint(output)
