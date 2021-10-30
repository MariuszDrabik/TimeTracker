from datetime import datetime
import sqlite3
from sqlite3 import Error
from time import sleep


class ConnectSQLite:

    @staticmethod
    def create_connection():
        db_file = 'database/time.db'
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            return conn

    def drop_table(self, table):
        with self.create_connection() as c:
            cursor = c.cursor()
            cursor.execute('DROP TABLE IF EXISTS ' + table + '')


class TrackRepository:

    def __init__(self):
        self.conn = ConnectSQLite().create_connection()

    def select_all(self):
        with self.conn as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT `id`,`name`, `project_time` FROM Projects')
            return cursor.fetchall()

    def save(self, project_id, start_time, end_time, project_time):
        with self.conn as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO Track ('
                           '`project_ID`, `start_time`, `end_time`, `project_time`);'
                           'VALUES(?, ?, ?, ?)',
                           (project_id, start_time, end_time, project_time))


class ProjectRepository:

    def __init__(self):
        self.conn = ConnectSQLite().create_connection()

    def select_all(self):
        with self.conn as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT `id`,`name` FROM Projects')
            return cursor.fetchall()

    def get_id(self, name):
        with self.conn as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT `id` FROM Projects WHERE name=?', name)
            return cursor.fetchone()

    def save(self, name):
        with self.conn as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Projects (`name`) VALUES(?)", (name,))
            connection.commit()



if __name__ == '__main__':


    project_name = 'Torun Dworce'

    ProjectRepository().save(project_name)
    print('ok')
