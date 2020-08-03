from datetime import datetime
import logging

from sqlalchemy.exc import OperationalError

from student_api.common.exceptions import Conflict, NotFound
from student_api.students.models import Student


logger = logging.getLogger(__name__)


class StudentView:

    model = Student

    @classmethod
    def post(cls, data):
        content = {}

        try:
            content = cls.model.add(data)
            status_code = 201
        except OperationalError as e:
            logger.error(
                f'Bad request while creating a student. {e.orig.args[1]}'
            )
            status_code = 400
        except Conflict as e:
            logger.error(e.message)
            status_code = e.status_code
        except Exception as e:
            logger.error(
                f'Server error while creating a student: {e}'
            )
            status_code = 500

        return content, status_code

    @classmethod
    def list_(cls, query_params):
        try:
            students = cls.model.list_(query_params.to_dict())
            return {'students': students}, 200
        except Exception as e:
            logger.error(
                f'Server error while listing students: {e}'
            )
            return {}, 500

    @classmethod
    def patch(cls, student_id, data):
        content = {}

        try:
            content = cls.model.patch(student_id, data)
            status_code = 200
        except OperationalError as e:
            logger.error(
                f'Bad request while updating a student. {e.orig.args[1]}'
            )
            status_code = 400
        except NotFound as e:
            logger.error(e.message)
            status_code = e.status_code
        except Exception as e:
            logger.error(
                f'Server error while updating a student: {e}'
            )
            status_code = 500

        return content, status_code

    @classmethod
    def delete(cls, student_id):
        content = {}

        try:
            content = cls.model.delete(student_id)
            status_code = 200
        except NotFound as e:
            logger.error(e.message)
            status_code = e.status_code
        except Exception as e:
            logger.error(
                f'Server error while deleting a student: {e}'
            )
            status_code = 500

        return content, status_code
