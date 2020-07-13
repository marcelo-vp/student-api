from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class DatabaseMixin:

    @property
    def db_session(self):
        return self.session


class StudentModel(Base, DatabaseMixin):
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
        user_dict = self.__dict__.copy()
        del user_dict['_sa_instance_state']
        return user_dict

    def _check_existing_user(self):
        pass

    def add(self):
        user = self._to_dict()
        self.db_session.add(self)
        self.db_session.commit()
        user['id'] = self.id
        return user

tables = Base.metadata
