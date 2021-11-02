import os
import sqlite3
from sqlite3 import Error


def read_ini_sql():
    query_string = ''
    with open('migrations/ini.sql', 'r') as file:
        for i in file:
            query_string += i.strip()
    return query_string.split(';')


def database_dir_create(database_dir):
    if not os.path.exists(database_dir):
        os.mkdir(database_dir)
        print('Created dir: ', database_dir)
        return 0
    print('Already exist dir: ', database_dir)
    return 0


def create_connection(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        return conn


if __name__ == '__main__':
    db_file = 'time.db'
    dir_path = './database'

    database_dir_create(dir_path)

    for i in read_ini_sql():
        print(i)
        with create_connection(f'{dir_path}/{db_file}') as conn:
            cursor = conn.cursor()
            cursor.execute(i)
            conn.commit()
