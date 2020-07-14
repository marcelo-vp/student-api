from student_api.common.exceptions import PreConditionFailed

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class DatabaseMixin:

    @property
    def session(self):
        return self._session


class Student(Base, DatabaseMixin):
    __tablename__  = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    responsible_adult = Column(String(100), nullable=False)
    school_grade = Column(String(100))
    zip_code = Column(String(10), nullable=False)
    street_name = Column(String(200), nullable=False)
    street_number = Column(Integer, nullable=False)
    complement = Column(String(200))

    def _to_dict(self):
        student_dict = self.__dict__.copy()
        del student_dict['_sa_instance_state']
        return student_dict

    def _check_existing_student(self):
        existing_student = self.session.query(Student).filter_by(
            first_name=self.first_name,
            last_name=self.last_name
        ).first()

        if existing_student:
            raise PreConditionFailed

        return

    def add(self):
        self._check_existing_student()

        user = self._to_dict()
        self.session.add(self)
        self.session.commit()
        user['id'] = self.id

        return user

    def list_(self, params):
        students = [
            student_instance._to_dict()
            for student_instance in self.session.query(Student).filter_by(**params)
        ]
        return students

tables = Base.metadata
