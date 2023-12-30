import requests

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

def get_location(apikey):
    ip_addr = get_ip_public()
    resp1 = requests.get(f"https://api.ipfind.com?ip={ip_addr}&auth={apikey}").json()
    # resp2 = ip/requests.get(f"https://ipapi.co/{ip_addr}/json").json() => limited if programmed

    ''' Return specific datum from (resp2)
    loc_data = {
        "ip "   : ip_addr,
        "city"  : resp.get("city")
    }
    '''

    # return all data
    return resp1

def run():
    ip_address = get_ip_public()
    ip_location = get_location("your-api-key")

    print (f"IP Public: {ip_address}")
    print (ip_location)

if __name__ == "__main__":
    run()