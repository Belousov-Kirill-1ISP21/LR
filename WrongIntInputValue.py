from OP.WrongInputValue import WrongInputValue


class WrongIntInputValue(WrongInputValue):
    def __init__(self):
        super().__init__()
        print('Create WrongIntInputValue')
    def __str__(self):
        super().__str__()
        print('WrongIntInputValue has been raised')