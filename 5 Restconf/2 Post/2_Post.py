import json
import requests

requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.56.101/restconf/data/Cisco-IOS-XE-native:native/logging/monitor"

headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }

basicauth = ("cisco", "cisco123!")

severit = { "severity": "alerts"
           }

severit1 = "{\n       \"severity\": \"alerts\"\n}\n"

#resp = requests.post(api_url, data=severit, auth=basicauth, headers=headers, verify=False)

resp = requests.post(api_url, data=json.dumps(severit), auth=basicauth, headers=headers, verify=False)


print(resp)

#print(resp.text)

print(type(severit))
#print(type(headers))
print(type(api_url))
print(type(basicauth))
print(json.dumps(severit))
print(json.loads(json.dumps(severit)))
print(type(severit1))




