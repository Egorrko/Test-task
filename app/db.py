import pymysql
from os import environ


def connect():
    return pymysql.connect(
        host=environ['HOST'],
        port=int(environ['PORT']),
        user=environ['USER'],
        password=environ['PASSWORD'],
        database=environ['DB_NAME']
    )


def get_devices():
    try:
        connection = connect()
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM Types'
            cursor.execute(sql)
            return cursor.fetchall()
    except Exception as e:
        print(e)


def add_number(serial_number: str, device_id: int):
    try:
        connection = connect()
        with connection.cursor() as cursor:
            device = f'({device_id},"{serial_number}")'
            sql = f'INSERT INTO Devices (Type, SerialNumber) VALUES {device};'
        return True
    except pymysql.err.IntegrityError as e:
        return False
    except Exception as e:
        return False
