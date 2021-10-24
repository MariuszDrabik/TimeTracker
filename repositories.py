from datetime import datetime
import sqlite3
from sqlite3 import Error
from time import sleep

'''Zmiana bazy danych
podział na dwie tabele'''
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
            cursor.execute("INSERT INTO Projects (`name`, `project_time`) VALUES(?, ?)",
                           (name, time))


    def creat_table(self):
        with self.conn as connection:
            cursor = connection.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Projects ('
                           'id integer PRIMARY KEY AUTOINCREMENT, '
                           'name text NOT NULL, '
                           'begin_date text, '
                           'end_date text, '
                           'project_time time)')
            connection.commit()

        print('Utworzono tabelę')

if __name__ == '__main__':

    tabela = ProjectRepository().select_all()
    #
    print(tabela)
    # # ProjectRepository().creat_table()
    # inital_time = datetime.now()
    # sleep(10)
    # end_time = datetime.now() - inital_time
    # print(end_time)
    #
    # ProjectRepository().save_time('projekt pierwszy', str(end_time))
