import requests
import json

url = "https://developer-api.govee.com/v1/devices/control"

payload = json.dumps({
    "device": "5F:EB:A4:C1:38:00:92:D2",
    "model": "H6159",
    "cmd": {
        "name": "turn",
        "value": "on"
    }
})
headers = {
    'Govee-API-Key': '095cfe5a-3e8d-430d-95a3-c23336a822cc',
    'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

# {
#     "device": "34:20:03:15:82:ae",
#     "model": "H6089",
#     "cmd": {
#         "name": "color",
#         "value": {
#             "r": 255,
#             "g": 255,
#             "b": 255
#         }
#     }
# }
