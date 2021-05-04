

class ParametersNotProvidedException(Exception):
    def __init__(self, message):
        super(ParametersNotProvidedException, self).__init__(message)