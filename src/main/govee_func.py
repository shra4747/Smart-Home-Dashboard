import json
import requests


def toggle(state, mac, model):
    try:
        url = "https://developer-api.govee.com/v1/devices/control"

        payload = json.dumps({
            "device": mac,
            "model": model,
            "cmd": {
                "name": "turn",
                "value": state
            }
        })
        headers = {
            'Govee-API-Key': '095cfe5a-3e8d-430d-95a3-c23336a822cc',
            'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)
        return f"{response.status_code}"
    except:
        return "503"


def color(r, g, b, mac, model):
    print(r, g, b, mac, model)
    try:
        url = "https://developer-api.govee.com/v1/devices/control"

        payload = json.dumps({
            "device": mac,
            "model": model,
            "cmd": {
                "name": "color",
                "value": {
                    "r": int(r),
                    "g": int(g),
                    "b": int(b)
                }
            }
        })

        headers = {
            'Govee-API-Key': '095cfe5a-3e8d-430d-95a3-c23336a822cc',
            'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)
        return f"{response.status_code}"
    except:
        return "503"
