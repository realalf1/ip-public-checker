import requests
from time import sleep

def get_ip_public():
    resp1   = requests.get("https://suip.biz/ip").text # show ip directly
    # resp2 = requests.get("https://api.ipify.org?format=json").json() => using json if available

    return resp1
    # return resp2["ip"]

''' Checking IP Public every 5 seconds
intr = 5

try:
    while True:
        get_public_ip()
        print (f"My public ip : {get_public_ip()}")
        sleep(intr)

except KeyboardInterrupt:
    print("Program interrupted by user")
'''