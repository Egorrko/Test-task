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
