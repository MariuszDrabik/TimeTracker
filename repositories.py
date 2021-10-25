from datetime import datetime
import sqlite3
from sqlite3 import Error
from time import sleep


class ConnectSQLite:

    def create_connection(self):
        db_file = 'database/time.db'
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            return conn


class ProjectRepository:

    def __init__(self):
        self.conn = ConnectSQLite().create_connection()

    def select_all(self):
        with self.conn as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT `id`,`name`, `project_time` FROM Projects')
            return cursor.fetchall()

    def save_time(self, name, time):
        with self.conn as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Projects (`name`, `project_time`);'
                           'VALUES(?, ?)',
                           (name, time))

    def creat_table(self):
        with self.conn as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE Track ( '
                           'id integer PRIMARY KEY AUTOINCREMENT, '
                           'project_ID INTEGER, '
                           'start_time time, '
                           'end_time time, '
                           'project_time TEXT);')
            connection.commit()
        print('Utworzono tabelę')

    def creat_table_2(self):
        with self.conn as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE Project ('
                                    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                                    'name TEXT)')
            connection.commit()
        print('Utworzono tabelę')

    def drop_table(self, table):
        with self.conn as c:
            cursor = c.cursor()
            cursor.execute('DROP TABLE IF EXISTS '+table+'')


if __name__ == '__main__':
    # tabela = ProjectRepository().creat_table()
    # tabela_2 = ProjectRepository().creat_table_2()
    with open('migrations/ini.sql', 'r') as file:
        for i in file:
            print(i.strip())
    # # ProjectRepository().creat_table()
    # inital_time = datetime.now()
    # sleep(10)
    # end_time = datetime.now() - inital_time
    # print(end_time)
    #
    # ProjectRepository().save_time('projekt pierwszy', str(end_time))
