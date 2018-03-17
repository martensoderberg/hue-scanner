I made this because I want my raspberry pi to turn the lights on when I come home, and off when I leave. The other solutions I've tried ([Philips Hue](https://play.google.com/store/apps/details?id=com.philips.lighting.hue2), [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm)) have been a bit slow to react, in my experience...

The project is entirely dependent on [hue cli](https://github.com/birkirb/hue-cli) to communicate with the lights, and [arp-scan](https://linux.die.net/man/1/arp-scan) to check the nextwork for device presence.

The idea is that the scanner script reads a file of mac addresses (called ```mac_addresses```), and checks the network for those addresses once every 5 seconds or so. If no device is present, it's probably safe to turn off the lights. If one (or more) is present but wasn't before, we should probably turn on the lights, assuming that it's not 3 in the morning and another device was already present, or something like that. I'll figure out the logic along the way.

```mac_addresses``` should have a file structure as so:
```
01:23:45:67:89:AB,Some ASCII description of this device
FE:DC:BA:98:76:54,Some ASCII description of another device
...
```
