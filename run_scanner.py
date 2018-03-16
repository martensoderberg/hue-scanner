#!/usr/bin/python3

from subprocess import call

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
        call(["./scan.sh", mac_address])


devices = read_mac_addresses()
scan_for_devices(devices)


