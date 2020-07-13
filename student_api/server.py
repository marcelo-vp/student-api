from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from student_api.common.database import tables
from student_api.constants import DB_NAME, DB_URL


class Server(Flask):

    def run(self):
        self.__init_database()
        super().run()

    def __init_database(self):
        engine = create_engine(f'{DB_URL}/{DB_NAME}')
        tables.create_all(engine)

        Session = sessionmaker(bind=engine)
        Session()


app = Server('student_api')
