import mysql.connector as connector

from student_api.constants import DB_NAME


connection = connector.connect(user='root')
cursor = connection.cursor()

def _create_db(cursor):
    try:
        cursor.execute(
            f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'"
        )
    except connector.Error as e:
        print(f'Failed to create database with: {e}')
        exit(1)

def connect_to_db():
    try:
        cursor.execute(f'USE {DB_NAME}')
    except connector.Error as e:
        print(f'Database {DB_NAME} does not exist')

        if e.errno == connector.errorcode.ER_BAD_DB_ERROR:
            _create_db(cursor)
            print(f'Database {DB_NAME} created succesfully')
            connection.database = DB_NAME
        else:
            print(e)
            exit(1)

if __name__ == '__main__':
    connect_to_db()
