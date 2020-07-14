class Error(Exception):
    pass


class PreConditionFailed(Error):

    def __init__(self, message):
        self.message = message
        self.status_code = 412
