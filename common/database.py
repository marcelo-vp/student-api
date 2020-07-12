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


Base = declarative_base()


class Student(Base):
    __tablename__  = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    responsible_adult = Column(String(250), nullable=False)
    school_grade = Column(String(250))
    discipline_grades = Column(JSON)
    last_registration = Column(DateTime)
    late_payments = Column(Integer)


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    zip_code = Column(String(8))
    street_name = Column(String(250))
    street_number = Column(Integer)
    complement = Column(String(250))
    student = relationship(Student)
    student_id = Column(Integer, ForeignKey('student.id'))


engine = create_engine('mysql://root@127.0.0.1:3306/school')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
db_session = Session()
