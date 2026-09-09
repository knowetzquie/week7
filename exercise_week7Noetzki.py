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

#==============================================================
#Exercise 1: Convert Python Dict + JSON
#==============================================================
#HINT: converts a python dict to a JSON string

print("=== EXERCISE 1: Convert to JSON ===")
#FILL IN THE BLANKS
#json_output = json._____(router_config, indent = 2)
json_output = json.dumps(router_config, indent = 2)

print(json_output)
print()

#==============================================================
#Exercise 2: Convert Python Dict + YAML
#==============================================================
#HINT: converts a python dict to a YAML string
print("=== EXERCISE 2: Convert to YAML ===")
#FILL IN THE BLANK
yaml_output = yaml.dump(router_config, default_flow_style= False)
print(yaml_output)
print()

#=============================================================
#Exercise 3: READ JSON from file
#==============================================================
print("=== EXERCISE 3: Read JSON from file === ")
#First, let's  save our config as a JSON file
with open("router_config.json", "w") as f:
    json.dump(router_config, f, indent = 2)

#Now read it back
#FILL IN THE BLANK
with open("router_config.json","r") as f:
    loaded_config = json.load(f)

print(f"Loaded hostname: {loaded_config['hostname']}")
print(f"Number of interfaces: {len(loaded_config['interfaces'])}")
print()
