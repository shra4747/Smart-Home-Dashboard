from tplink_smartplug import SmartPlug


def toggle(state, ip):
    try:
        plug = SmartPlug(ip)
        if state == "on":
            try:
                plug.turn_on()
                return "200"
            except:
                return "503"
        elif state == "off":
            try:
                plug.turn_off()
                return "200"
            except:
                return "503"
    except:
        return "503"
