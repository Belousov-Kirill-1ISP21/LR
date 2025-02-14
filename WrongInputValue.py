from OP.MyException import MyCustomError


class WrongInputValue(MyCustomError):
    def __init__(self):
        super().__init__()
        print('Create WrongInputValue')
    def __str__(self):
        super().__str__()
        print('WrongInputValue has been raised')