#!/usr/bin/python3

devices = []
def read_mac_addresses:
with open('mac_addresses') as f:
    content = f.readlines()
    content = map(lambda s: s.strip(), content)
    for line in content:
        if line:
            fields = line.split(',')
            mac_address = fields[0]
            description = fields[1]
            devices.append((mac_address, description))


