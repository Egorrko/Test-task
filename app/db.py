<<<<<<< HEAD
import pymysql
from os import environ
=======
import sys
import pymysql
from os import environ
from loguru import logger

logger.add(sys.stderr, format="{time} {level} {message}")
>>>>>>> ac700b3c6e9bdde52447ddeb4dbeead904a4dbb5


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
<<<<<<< HEAD
            cursor.execute(sql)
            return cursor.fetchall()
    except Exception as e:
        print(e)
=======
            logger.info(sql)
            cursor.execute(sql)
            return cursor.fetchall()
    except Exception as e:
        logger.error(e)
>>>>>>> ac700b3c6e9bdde52447ddeb4dbeead904a4dbb5


def add_number(serial_number: str, device_id: int):
    try:
        connection = connect()
        with connection.cursor() as cursor:
            device = f'({device_id},"{serial_number}")'
            sql = f'INSERT INTO Devices (Type, SerialNumber) VALUES {device};'
<<<<<<< HEAD
=======
            logger.info(sql)
>>>>>>> ac700b3c6e9bdde52447ddeb4dbeead904a4dbb5
            cursor.execute(sql)
        connection.commit()
        return True
    except pymysql.err.IntegrityError as e:
<<<<<<< HEAD
        return False
    except Exception as e:
        return False
=======
        logger.warning(e)
        return False
    except Exception as e:
        logger.error(e)
        return False

>>>>>>> ac700b3c6e9bdde52447ddeb4dbeead904a4dbb5
