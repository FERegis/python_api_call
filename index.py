








import requests
import json
from pprint import pprint

# WLAN Profile #1
#   SSID: Enterprise
#   Band: 5GHz
#   Authentication Type: psk
#   PSK: ilovewifi2020

url = "https://api.mist.com/api/v1/sites/24398c6b-aa78-44ca-8e10-dda21fb44cf4/wlans"
TOKEN = "eH0gJYne3nzReT8IgmxVVgJaG2nBTwMEw3CoR2JCScxqvOupgcKqV0CbWl6Indhwi0aroHb1Rmbl7hBlDUtEmOn3YUxivQfh"
headers = {"Content-Type": "application/json", "Authorization": f"Token {TOKEN}"}

wlan1 = {
    "ssid" : "Enterprise",
    "band" : "5",
    "enabled" : True,
    "auth" : {
        "type": "psk",
        "psk" : "ilovewifi2020"
    }
}

body = json.dumps(wlan1)

response = requests.post(url, data = body, headers = headers)

wlanresponse = json.loads(response.content)

pprint(wlanresponse)

# WLAN Profile #2
#   SSID: Guest
#   Band: both
#   Authentication Type: open

wlan2 = {
    "ssid" : "Guest",
    "band" : "both",
    "enabled" : True,
    "auth" : {
        "type": "open"
    }
}

body = json.dumps(wlan2)

response = requests.post(url, data = body, headers = headers)

wlanresponse = json.loads(response.content)

pprint(wlanresponse)

#body = json.dump(wlan2)

# Create the SSID on our Mist site
# API Call to make
# Section Site, sub-section WLAN

