class Error(Exception):
    pass


class NotFound(Error):

    def __init__(self, message):
        self.message = message
        self.status_code = 404


class Conflict(Error):

    def __init__(self, message):
        self.message = message
        self.status_code = 409
