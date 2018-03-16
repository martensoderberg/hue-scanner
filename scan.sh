#!/bin/bash
arp-scan \
  --interface=wlan0 \
  --retry=2 \
  --timeout=150 \
  --bandwidth=1M \
  --backoff=1 \
  --quiet \
  --destaddr=$1 \
  192.168.1.180-192.168.1.199
