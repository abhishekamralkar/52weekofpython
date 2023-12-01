from random import choice
from tabulate import tabulate

def create_devices(num_devices=1, num_subnets=1):

    created_devices = []

    if num_devices > 254 or num_subnets > 254:
        print("Error: Too many devices and/or subnets requsted")
        return create_devices

    for subnet_index in range(1, num_subnets+1):

        for devices_index in range(1, num_devices+1):
            device = {}

            device["name"] = (
                choice(["r2", "r3", "r4", "r6", "r10"])
            )

            device["vendor"] = (
                choice(["junper", "csco", "arsta"])
            )

            if device["vendor"] == "junper":
                device["os"] = "jnuos"
                device["versiion"] = choice(["12.3R12-S15", "15.1R7-S6", "18.4R2-S3", "15.1X53-D591"])

            elif device["vendor"] == "arsta":
                device["os"] = "eos"
                device["version"] = choice(["4.24.1F", "4.23.2F", "4.22.1F", "4.21.3F"])
            elif device["vendor"] == "csco":
                device['os'] = choice(['ios', 'iosxe', 'iosxr', 'nexus'])
                device['version'] = choice(['12.1(T).04', '14.07X', '8.12(S).010'])

            device["ip"] = "10.0." + str(subnet_index) + "." + str(devices_index)

            created_devices.append(device)

        return created_devices

if __name__ == '__main__':
    devices = create_devices(num_devices=20, num_subnets=4)
    print("\n", tabulate(devices, headers="keys"))
