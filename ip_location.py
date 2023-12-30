import ip_public as ip

def get_location(apikey):
    ip_addr = ip.get_ip_public()
    resp1 = ip.requests.get(f"https://api.ipfind.com?ip={ip_addr}&auth={apikey}").json()
    # resp2 = ip/requests.get(f"https://ipapi.co/{ip_addr}/json").json() => limited if programmed

    ''' Return specific datum from (resp2)
    loc_data = {
        "ip "   : ip_addr,
        "city"  : resp.get("city")
    }
    '''

    # return all data
    return resp1