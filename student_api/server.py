from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from student_api.constants import DB_NAME
from student_api.settings import DB_URL
from student_api.students.models import tables, DatabaseMixin


class Server(Flask):

    def run(self):
        self.__init_database()
        super().run()

    def __init_database(self):
        engine = create_engine(f'{DB_URL}/{DB_NAME}')
        tables.create_all(engine)

        Session = sessionmaker(bind=engine)
        DatabaseMixin.session = Session()


app = Server('student_api')
