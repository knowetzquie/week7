#!/usr/bini/env python3
"""
Week 7: Data Serialization - Convert Network compare_configs
============================================================
Your task: Convert a network device config between JSON nd YAML

FILL IN THE BLANKS marked with _____
Run this script when done: python3 exercise_week7Noetzki.py
"""
import json
import yaml

#===============================================================
#This is a network device configuration in Python (dictionary)
#===============================================================

router_config = {
    "hostname": "Router-1",
    "vendor": "Cisco",
    "interfaces": [
        {"name": "GigabitEthernet1", "ip": "192.168.1.1", "status": "up"},
        {"name": "GigabitEthernet2", "ip": "10.0.0.1", "status": "up"},
        {"name": "GigabitEthernet3", "ip": "172.16.0.1", "status": "down"},
    ]
}