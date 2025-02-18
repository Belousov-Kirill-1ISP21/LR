from WrongInputValue import WrongInputValue


class WrongIntInputValue(WrongInputValue):
    def __init__(self,message):
        super().__init__()
        print('Create WrongIntInputValue')
        print(message)
    def __str__(self):
        super().__str__()
        print('WrongIntInputValue has been raised')