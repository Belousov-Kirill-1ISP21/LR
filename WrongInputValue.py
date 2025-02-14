from OP.MyException import MyException


class WrongInputValue(MyException):
    def __init__(self):
        super().__init__()
        print('Create WrongInputValue')
    def __str__(self):
        super().__str__()
        print('WrongInputValue has been raised')