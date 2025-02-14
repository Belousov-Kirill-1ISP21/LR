from OP.WrongInputValue import WrongInputValue


class WrongStrInputValue(WrongInputValue):
    def __init__(self):
        super().__init__()
        print('Create WrongStrInputValue')
    def __str__(self):
        super().__str__()
        print('WrongStrInputValue has been raised')