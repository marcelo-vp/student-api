from datetime import datetime
import logging

from student_api.students.models import StudentModel


logger = logging.getLogger(__name__)


class StudentView:

    model = StudentModel

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
        except Exception as e:
            logger.error(
                f'Server error while creating a student: {e}'
            )
            status_code = 500

        return content, status_code

    @classmethod
    def _list(cls):
        pass

    @classmethod
    def patch(cls):
        pass

    @classmethod
    def delete(cls):
        pass
