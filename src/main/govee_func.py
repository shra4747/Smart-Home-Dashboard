from pygovee import Govee


class GoveeFunction:

    client = None

    def __init__(self, apiKey):
        self.apiKey = apiKey

        global client
        client = Govee.GoveeClient(self.apiKey)

    def toggle(self, state, mac, model):
        if state == "on":
            client.device_on(mac, model)
        elif state == "off":
            client.device_off(mac, model)

    def color(self, r, g, b, mac, model):
        client.change_device_color(mac, model, r, g, b)

    def brightness(self, brightness_level, mac, model):
        client.change_device_brightness(mac, model, brightness_level)
