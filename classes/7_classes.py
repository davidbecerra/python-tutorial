class CustomException(Exception):
    def __init__(self, message):
        self.msg = message


def isEven(n):
    if n % 2 is 0:
        return True
    else:
        raise CustomException('I got an odd number!')


isEven(13)