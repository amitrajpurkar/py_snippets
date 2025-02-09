#ask user for ip address and decode it using an API

import os
import urllib.request as urllib2
import json


# sample ip address: 162.159.152.17 (poe.com)
# 142.250.217.206 (google.com)

def decode_ip_address():
    url = "http://freegeoip.net/json/"
    url = "http://ip-api.com/json/"
    ip = input("Enter IP address: ")
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)
    json_string = json.dumps(values, indent=2, sort_keys=True)

    print(json_string)


decode_ip_address()