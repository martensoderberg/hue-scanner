#!/usr/bin/python3

from subprocess import call, check_output

def read_mac_addresses():
    devices = []
    with open('mac_addresses') as f:
        content = f.readlines()
        content = map(lambda s: s.strip(), content)
        for line in content:
            if line:
                fields = line.split(',')
                mac_address = fields[0]
                description = fields[1]
                devices.append((mac_address, description))
    return devices

def scan_for_devices(devices):
    for mac_address, description in devices:
        print("Scanning for " + description + "...")
        result = check_output(["./scan.sh", mac_address]).strip()
        if result == b'1':
            print("Present and accounted for!")
        else:
            print("Gone with the wind!")


devices = read_mac_addresses()
scan_for_devices(devices)


