import db
from re import match

devices = {}


class Device:
    def __init__(self, name, mask):
        self.name = name
        self.mask = translate(mask)


def translate(mask):
    translator = {
        'N': r'\d',
        'A': r'[A-Z]',
        'a': r'[a-z]',
        'X': r'[A-Z0-9]',
        'Z': r'[-_@]'
    }
    return r''.join([translator[i] for i in mask])


def get_devices():
    if len(devices) != 0:
        return devices
    raw_devices = db.get_devices()
    for i in raw_devices:
        devices[str(i[0])] = Device(i[1], i[2])
    return devices


def accept_numbers(serial_numbers: str, device_id: int):
    """return [(num, True/False/None)]
    True = accepted, False = repeated, None = rejected"""
    result = []
    for num in serial_numbers.split():
        if match(devices[device_id].mask, num):
            result.append((num, db.add_number(num, device_id)))
        else:
            result.append((num, None))
    return result
