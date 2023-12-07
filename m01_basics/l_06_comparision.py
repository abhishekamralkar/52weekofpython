from util.create_utils import create_devices
from pprint import pprint
from random import randint, uniform
from datetime import datetime

devices = create_devices(num_subnets=2, num_devices=25)
print("\n    NAME    VENDOR   :   OS    IP ADDRESS     VERSION")
print("\n  ------    ------      ----- ------------   ---------")
for device in devices:
    print(
        f'{device["name"]:>7}    {device["vendor"]:>10}  :  {device["os"]:>6}   {device["ip"]:>10}'
    )

print("\n    NAME    VENDOR   :   OS    IP ADDRESS     VERSION")
print("\n  ------    ------      ----- ------------   ---------")
for device in devices:
    if device["vendor"] == "csco":
        print(
            f'{device["name"]:>7}  {device["vendor"]:>10}  :  {device["os"]:>6}   {device["ip"]:>10}'
        )

print("\n------ Starting comparision of device names -------------------")
for index, device_a in enumerate(devices):
    for device_b in devices[index+1:]:
        if device_a["name"] == device_b["name"]:
            print(f"Found match! {device_a['name']} for both {device_a['ip']}")
print("------- Comparision of device names completed------------")

print("\n-----------Create table arbitrary 'standard' versions for each vendor:os -------------")
standard_version = dict()
for device in devices:
    vendor_os = device["vendor"] + ":" + device["os"]
    if vendor_os not in standard_version:
        standard_version[vendor_os] = device["version"]
pprint(standard_version)

print("\n------ Create list of non-compliant device OS versions for each vendor:os -------")
non_compliant_devices = dict()
for vendor_os, _ in standard_version.items():
    non_compliant_devices[vendor_os] = []

for device in devices:
    vendor_os = device["vendor"] + ":" + device["os"]
    if device["version"] != standard_version[vendor_os]:
        non_compliant_devices[vendor_os].append(device["ip"] + " version: " + device["version"])

pprint(non_compliant_devices)

print("\n\n---- Assignment, copy, and deep copy------")
devices2 = devices
devices[0]["name"] = "this is a dumb device name"
if devices2 == devices:
    print("\n   Assignment and modification: device2 STILL equals devices")
    print("    ----> Moral: Assignment is NOT the same as copy!")
else:
    print("----huh?")

from copy import copy
from copy import deepcopy

devices2 = deepcopy(device)
devices2[0]["name"] = "this is also a dumb device name"
if devices2 == devices:
    print("----huh?")
else:
    print("\n      Shallow copy modification: devices2 STILL equals devices")
    print("        Moral: copy() only does a SHALLOW copy")
    print("        ----> I just screwed up the original version")
    
