class MyException(Exception):
    def __init__(self):
        print('Create MyCustomerror')
    def __str__(self):
        print('MyCustomError has been raised')