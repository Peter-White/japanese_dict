class ModelNotFound(Exception):
    def __init__(self, message, model):
        # Pass the message to the base Exception class
        super().__init__(message)
        self.model = model
    pass

class IDNotNumber(Exception):
    pass

class CategoryNotValid(Exception):
    pass