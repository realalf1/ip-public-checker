import requests
from time import sleep

class IPServicer():
    
    def __init__(self, ip_public=requests.get("https://suip.biz/ip")):
        self.name = "IP Services for getting information about Internet Protocol."
        self.ip_public = ip_public.text
        
    def checking_ip_public(self):
        try:
            while True:
                print(f"IP Public: {self.ip_public}")
                sleep(5)
				
        except KeyboardInterrupt:
            print("Program interrupted by user")

    def get_location(self):
        r = requests.get(f"https://api.ipfind.com?ip={self.ip_public}") # limited to 100 requests / day or using API Key
        # r = requests.get(f"https://ipapi.co/{self.ip_public}/json") => limited if programmed
        
        return r.text

    def run(self):
        print (f"IP Public: {self.ip_public}")
        print (f"Location : \n{self.get_location()}")

if __name__ == "__main__":
    ip = IPServicer()
    ip.run()
