from datetime import datetime
import logging

from student_api.common.exceptions import PreConditionFailed
from student_api.students.models import Student


logger = logging.getLogger(__name__)


class StudentView:

    model = Student

    @classmethod
    def post(cls, data):
        content = {}

        try:
            user = cls.model(**data)
            content = user.add()
            status_code = 201
        except KeyError as e:
            logger.error(
                f'Bad request while creating a student: {e}'
            )
            status_code = 400
        except PreConditionFailed as e:
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
        students = cls.model().list_(query_params.to_dict())
        return {'students': students}, 200

    @classmethod
    def patch(cls, student_id, data):
        content = {}

        try:
            content = cls.model().patch(student_id, data)
            status_code = 200
        except PreConditionFailed as e:
            logger.error(e.message)
            status_code = e.status_code
        except Exception as e:
            logger.error(
                f'Server error while updating a student: {e}'
            )
            status_code = 500

        return content, status_code

    @classmethod
    def delete(cls):
        pass
