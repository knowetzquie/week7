import json
import yaml
import os

try:
    import xmltodict
    HAS_XMLTODICT = True
except ImportError:
    HAS_XMLTODICT = False
    print("Note: xmltodict module is not installed. Run: pip install xmltodict")