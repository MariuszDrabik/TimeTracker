from datetime import datetime, timedelta, time
import sqlite3

from sqlite3 import Error
from time import sleep

'''Wymaga modyfikacji'''
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    # create_connection("database/time.db")

    start_time = datetime.now()
    sleep(1)

    end_time = datetime.now()

    end = end_time - start_time
    a, b, c = str(end).split(".")[0].split(":")
    print(a, b, c)


    print(end)

