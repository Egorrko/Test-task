<<<<<<< HEAD
import cherrypy
from jinja2 import Environment, FileSystemLoader
from logic import get_devices, accept_numbers

env = Environment(loader=FileSystemLoader('templates'))


class DeviceManager(object):
    @cherrypy.expose()
    def index(self, serial_numbers=None, device=None):
        if serial_numbers is None:
            return env.get_template('index.html').render(devices=get_devices(),
                                                         result=None)
        return env.get_template('index.html').render(devices=get_devices(),
                                                     result=accept_numbers(serial_numbers,device))


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 5000})
    cherrypy.quickstart(DeviceManager())
=======
from flask import Flask, render_template, request
from logic import get_devices, accept_numbers

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        serial_numbers = (request.form['serial_numbers'])
        device_id = (request.form['device'])
        return render_template('index.html',
                               devices=get_devices(),
                               result=accept_numbers(serial_numbers, device_id))
    return render_template('index.html',
                           devices=get_devices(),
                           result=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
>>>>>>> ac700b3c6e9bdde52447ddeb4dbeead904a4dbb5
