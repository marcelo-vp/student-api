from sqlalchemy import (
    create_engine,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    JSON,
    String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from student_api.common.connector import Connector
from student_api.constants import DB_NAME, DB_URL


Base = declarative_base()


class Student(Base):
    __tablename__  = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    responsible_adult = Column(String(100), nullable=False)
    school_grade = Column(String(100))
    discipline_grades = Column(JSON)
    last_registration = Column(DateTime)
    late_payments = Column(Integer, default=0)
    zip_code = Column(String(8), nullable=False)
    street_name = Column(String(200), nullable=False)
    street_number = Column(Integer, nullable=False)
    complement = Column(String(200))


engine = create_engine(f'{DB_URL}/{DB_NAME}')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
db_session = Session()
