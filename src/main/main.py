from flask import Flask
import govee_func
import kasa_func


app = Flask(__name__)


@app.route('/govee/toggle/<state>/<mac>&<model>')
def toggle(state, mac, model):
    return govee_func.toggle(state, mac, model)


@app.route('/govee/color/<r>&<g>&<b>/<mac>&<model>')
def color(r, g, b, mac, model):
    return govee_func.color(r, g, b, mac, model)


@app.route('/kasa/toggle/<state>/<ip>')
def kasa_toggle(state, ip):
    return kasa_func.toggle(state, ip)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='80')
