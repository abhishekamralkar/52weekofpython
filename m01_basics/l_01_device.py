from pprint import pprint

# DICTIONARY representing a device

device = {
    "name": "sbx-n9kv-ao",
    "vendor": "cisco",
    "model": "Nexus9000 C9300v Chassis",
    "os": "nxos",
    "version": "9.3(3)",
    "ip": "10.1.1.1",
}


# SIMPLE PRINT
print("\n______SIMPLPE PRINT___________")
print("device: ", device)
print("device name:", device["name"])

# PRETTY PRINT

print("\n______PRETTY PRINT___________")
pprint(device)

# FOR LOOP, NICELY FORMATTED PRINT
print("\n______FOR LOOP, USING F-STRING_________")
for key, value in device.items():
    print(f"{key:>16s} : {value}")

def name():
    print("Hello World")
