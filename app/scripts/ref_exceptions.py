class ModelNotFound(Exception):
    def __init__(self, message):
        # Pass the message to the base Exception class
        super().__init__(message)
    pass

class IDNotNumber(Exception):
    pass

class CategoryNotValid(Exception):
    pass