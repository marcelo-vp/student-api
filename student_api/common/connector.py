import mysql.connector as connector

from student_api.constants import DB_NAME


class Connector:
    def __init__(self):
        self.connection = connector.connect(user='root')
        self.cursor = self.connection.cursor()

    def create_db(self, cursor):
        try:
            cursor.execute(
                f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'"
            )
        except connector.Error as e:
            print(f'Failed to create database with: {e}')
            exit(1)

    def connect(self):
        try:
            self.cursor.execute(f'USE {DB_NAME}')
        except connector.Error as e:
            print(f'Database {DB_NAME} does not exist')

            if e.errno == connector.errorcode.ER_BAD_DB_ERROR:
                self.create_db(self.cursor)
                print(f'Database {DB_NAME} created succesfully')
                self.connection.database = DB_NAME
            else:
                print(e)
                exit(1)
