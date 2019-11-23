class BoardValidationException(Exception):
    pass


class BinaryDoesntExist(BoardValidationException):
    pass


class ProgrammerNotConnected(BoardValidationException):
    pass

