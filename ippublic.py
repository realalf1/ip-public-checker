import requests
from time import sleep

def get_public_ip():
    resp = requests.get("https://api.ipify.org").text
    return resp

intr = 5

try:
    while True:
        get_public_ip()
        print (f"My public ip : {get_public_ip()}")
        sleep(intr)

except KeyboardInterrupt:
    print("Program interrupted by user")