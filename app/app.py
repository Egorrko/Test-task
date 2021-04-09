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
