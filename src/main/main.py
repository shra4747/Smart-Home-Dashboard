from flask import Flask
import govee_func
import kasa_func

app = Flask(__name__)

govee_func = govee_func.GoveeFunction(
    apiKey="095cfe5a-3e8d-430d-95a3-c23336a822cc")
govee_devices = {'room1': {'mac': '0F:21:A4:C1:38:16:C9:C2', 'model': 'H6110'},
                 'room2': {'mac': '5F:EB:A4:C1:38:00:92:D2', 'model': 'H6159'},
                 'desk': {'mac': 'AB:B7:A4:C1:38:BE:1C:6D', 'model': 'H6159'}}
kasa_devices = {'fan': '10.0.0.207', 'lamp': '10.0.0.27'}


@app.route('/')
def index():
    return '200'


@app.route('/govee/toggle/<state>/<mac>&<model>')
def toggle(state, mac, model):
    return govee_func.toggle(state, mac, model)


@app.route('/govee/color/<r>&<g>&<b>/<mac>&<model>')
def color(r, g, b, mac, model):
    return govee_func.color(r, g, b, mac, model)


@app.route('/kasa/toggle/<state>/<ip>')
def kasa_toggle(state, ip):
    return kasa_func.toggle(state, ip)


@app.route('/scenes/<scene>')
def scenes(scene):
    if scene == "all_on":
        govee_func.toggle(
            "on", govee_devices['room1']['mac'], govee_devices['room1']['model'])
        govee_func.toggle(
            "on", govee_devices['room2']['mac'], govee_devices['room2']['model'])
        govee_func.toggle(
            "on", govee_devices['desk']['mac'], govee_devices['desk']['model'])

        kasa_func.toggle('on', kasa_devices['lamp'])

        return '200'
    elif scene == "all_off":
        govee_func.toggle(
            "off", govee_devices['room1']['mac'], govee_devices['room1']['model'])
        govee_func.toggle(
            "off", govee_devices['room2']['mac'], govee_devices['room2']['model'])
        govee_func.toggle(
            "off", govee_devices['desk']['mac'], govee_devices['desk']['model'])

        kasa_func.toggle('off', kasa_devices['lamp'])

        return '200'
    elif scene == "sleep":
        govee_func.toggle(
            "off", govee_devices['room1']['mac'], govee_devices['room1']['model'])
        govee_func.toggle(
            "off", govee_devices['room2']['mac'], govee_devices['room2']['model'])

        kasa_func.toggle('off', kasa_devices['lamp'])

        return '200'
    elif scene == "tealpurple":
        govee_func.color(
            0, 255, 255, govee_devices['room1']['mac'], govee_devices['room1']['model'])
        govee_func.color(
            0, 255, 255, govee_devices['desk']['mac'], govee_devices['desk']['model'])
        govee_func.color(
            255, 0, 255, govee_devices['room2']['mac'], govee_devices['room2']['model'])

        return '200'
    elif scene == "blueyellow":
        govee_func.color(
            0, 0, 255, govee_devices['room1']['mac'], govee_devices['room1']['model'])
        govee_func.color(
            0, 0, 255, govee_devices['desk']['mac'], govee_devices['desk']['model'])
        govee_func.color(
            255, 190, 0, govee_devices['room2']['mac'], govee_devices['room2']['model'])

        return '200'
    elif scene == "white":
        govee_func.color(
            255, 255, 255, govee_devices['room1']['mac'], govee_devices['room1']['model'])
        govee_func.color(
            255, 255, 255, govee_devices['desk']['mac'], govee_devices['desk']['model'])
        govee_func.color(
            255, 255, 255, govee_devices['room2']['mac'], govee_devices['room2']['model'])

        return '200'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
