import ip_public as ip
import ip_location as loc

def run():
    ip_addr = ip.get_ip_public()
    ip_loc = loc.get_location("your-api-key")

    print (ip_addr)
    print (ip_loc)

if __name__ == "__main__":
    run()

