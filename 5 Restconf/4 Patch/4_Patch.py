import json
import requests

requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.56.101/restconf/data/Cisco-IOS-XE-native:native"

headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }

basicauth = ("cisco", "cisco123!")

severit = "{\n\"native\": {\n\"logging\": {\n\"monitor\": {\n\"severity\": \"informational\"\n}\n}\n}\n}\n"

severit1 = "{\n       \"severity\": \"warnings\"\n}\n"

#resp = requests.patch(api_url, data=severit, auth=basicauth, headers=headers, verify=False)

resp = requests.patch(api_url, data=severit, auth=basicauth, headers=headers, verify=False)


print(resp)