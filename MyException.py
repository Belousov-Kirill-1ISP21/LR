class MyException(Exception):
    def __init__(self):
        print('Create MyCustomerror')
    def __str__(self):
        return('MyCustomError has been raised')