from student_api.common.exceptions import PreConditionFailed

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class DatabaseMixin:

    @property
    def session(self):
        return self._session

    def _to_dict(self):
        instance_dict = self.__dict__.copy()
        del instance_dict['_sa_instance_state']
        return instance_dict

    def _has_existing_record(self, model):
        existing_record = self.session.query(model).filter_by(
            first_name=self.first_name,
            last_name=self.last_name
        ).first()

        return True if existing_record else False


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

    def add(self):
        if self._has_existing_record(Student):
            raise PreConditionFailed('Student already exists.')

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

    def patch(self, student_id, data):
        try:
            student = self.session.query(Student).filter_by(id=student_id).one()
        except Exception:
            raise PreConditionFailed('Student does not exist.')

        for key, value in data.items():
            setattr(student, key, value)

        response = student._to_dict()
        self.session.commit()
        return response

tables = Base.metadata
