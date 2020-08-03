from student_api.common.exceptions import Conflict, NotFound

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class DatabaseMixin:

    @classmethod
    def _to_dict(cls, instance):
        instance_dict = instance.__dict__.copy()
        del instance_dict['_sa_instance_state']
        return instance_dict

    @classmethod
    def _has_existing_record(cls, model, **kwargs):
        existing_record = cls.session.query(model).filter_by(**kwargs).first()
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

    @classmethod
    def _find_student(cls, student_id):
        try:
            return cls.session.query(Student).filter_by(id=student_id).one()
        except Exception:
            raise NotFound('Student does not exist.')

    @classmethod
    def add(cls, data):
        new_student = cls(**data)

        if cls._has_existing_record(
            Student,
            first_name=new_student.first_name,
            last_name=new_student.last_name
        ):
            raise Conflict('Student already exists.')

        student_dict = cls._to_dict(new_student)
        cls.session.add(new_student)
        cls.session.commit()
        student_dict['id'] = new_student.id
        return student_dict

    @classmethod
    def list_(cls, params):
        students = [
            cls._to_dict(student_instance)
            for student_instance in cls.session.query(Student).filter_by(**params)
        ]
        return students

    @classmethod
    def patch(cls, student_id, data):
        student = cls._find_student(student_id)

        for key, value in data.items():
            setattr(student, key, value)

        student_dict = cls._to_dict(student)
        cls.session.commit()
        return student_dict

    @classmethod
    def delete(cls, student_id):
        student = cls._find_student(student_id)
        student_dict = cls._to_dict(student)
        cls.session.delete(student)
        cls.session.commit()
        return student_dict

metadata = Base.metadata
