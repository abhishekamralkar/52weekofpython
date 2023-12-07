from functools import partial
from pprint import pprint


device1_str = "  r3-L-n7, cisco, catalyst 2968, ios "


# SPLITn
print("STRING STRIP, SPLIT, REPLACE")
device1 = device1_str.split(',')
print("device1 using split: ")
print("   ", device1)


# STRIP
device1 = device1_str.replace(" ", "").split(",")
print("device1 replaced blanks using split:   ", device1)


# REMOVE BLANKS
device1 = device1_str.replace("  ", "").split(',')
print("device1 replaced blanks using split:\n    ", device1)

# REMOVE BLANKS, CHANGE COMMA TO COLON
device1_str_colon = device1_str.replace(" ", "").replace(",", ":")
print("device1 replaced blank, commas to colon")
print("   ", device1_str_colon)

# LOOP WITH STRIP AND SPLIT
device1 = []
for item in device1_str.split(","):
    device1.append(item.strip())
print("device1 using loop and strip for each other:")
print("   ", device1)


# STRIP AND SPLIT, SINGLE LINE USING LIST COMPREHENSION
device1 = [item.strip() for item in device1_str.split()]
print("device1 using list comprehension")
print("    ", device1)

# IGNORING CASE
print("\n\nIGNORING CASE")
model = "CSR1000V"
if model == "csrv1000v":
    print(f"matched: {model}")
else:
    print(f"didn't match: {model}")

model = "CSR1000V"
if model.lower() == "csrv1000v":
    print(f"matched using lower(): {model}")
else:
    print(f"didn't match: {model}")

# FINDING SUBSTRING
print("\n\nFINDING SUBSTRING")
version = "Virtual XE Software (X86_64_LINUX_IOSO-UNIVERSALK9-M), Version 16.11.1a, RELEASE SOFTWARE (fc1)"
expected_version = "Version 16.11.1a"
index = version.find(expected_version)
if index > 0:
    print(f"found version: {expected_version} at location {index} ")
else:
    print(f"not found {expected_version}")

# SEPARATING STRING COMPONENTS
print("\n\nSEPARATING VERSIONS STRING COMPONENTS")
version_info = version.split(",")
for version_info_part in version_info:
    print(f"version part: {version_info_part.strip()}")

