#!/usr/bin/python3

from subprocess import call, check_output

devices = []
class Device:
    def __init__(self, mac_address, description):
        self.mac_address = mac_address
        self.description = description
        self.status = "Unknown!"

    def update_presence_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return self.description + " -- " + self.status

def read_mac_addresses():
    with open('mac_addresses') as f:
        content = f.readlines()
        content = map(lambda s: s.strip(), content)
        for line in content:
            if line:
                fields = line.split(',')
                mac_address = fields[0]
                description = fields[1]
                device = Device(mac_address, description)
                devices.append(device)

def scan_for_devices(devices):
    for device in devices:
        print("Scanning for " + device.description + "...")
        result = check_output(["./scan.sh", device.mac_address]).strip()
        if result == b'0':
            new_status = "Gone!"
        elif result == b'1':
            new_status = "Here!"
        else:
            new_status = "Whoops..."
        device.update_presence_status(new_status)

def turn_lights_off():
    call(["hue lights off"])

def turn_lights_on():
    call(["hue lights on"])

read_mac_addresses()
scan_for_devices(devices)
for d in devices:
    print(d)

