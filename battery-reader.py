#!/usr/bin/env python3

with open('/sys/class/power_supply/BAT0/capacity', 'r') as f:
    battery_level = int(f.read().strip())

print(f"Battery level: {battery_level}%")
