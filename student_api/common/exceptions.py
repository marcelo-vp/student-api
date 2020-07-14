class Error(Exception):
    pass


class PreConditionFailed(Error):

    def __init__(self):
        self.message = 'Precondition failed: student already exists.'
        self.status_code = 412
