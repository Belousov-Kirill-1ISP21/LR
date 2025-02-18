from WrongInputValue import WrongInputValue


class WrongStrInputValue(WrongInputValue):
    def __init__(self, message):
        super().__init__()
        print('Create WrongStrInputValue')
        print(message)
    def __str__(self):
        super().__str__()
        print('WrongStrInputValue has been raised')