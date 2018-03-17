#!/bin/bash
# ip_range should be your routers DHCP range
ip_range="192.168.1.180-192.168.1.199"
arp-scan \
  --interface=wlan0 \
  --retry=2 \
  --timeout=150 \
  --bandwidth=1M \
  --backoff=1 \
  --quiet \
  --numeric \
  --destaddr=$1 \
  $ip_range \
| grep $1 | uniq | wc -l
