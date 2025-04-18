from Person import Person
import logging
from tkinter import simpledialog, messagebox

class Customer(Person):
    __List = []

# Constructor
    def __init__(self, id, name, age, visitTime):
        self.__id = id
        super().__init__(name, age)
        self.__visitTime = visitTime
        Customer.addCustomer(self)
        logging.info('Был создан клиент ' + name + '.')

#Getters
    def getId(self):
        return self.__id

    def getVisitTime(self):
        return self.__visitTime

    @staticmethod
    def getList():
        return Customer.__List

    @staticmethod
    def getCustomerByName(clientName):
        for i in Customer.__List:
            if (i.getName() == clientName):
                return i
        return None

    @staticmethod
    def getCustomerById(ID):
        for i in Customer.__List:
            if (i.getId() == ID):
                return i
        return None

#Setters
    def setId(self, id):
        self.__Id = id

    def setVisitTime(self, visitTime):
        self.__visitTime = visitTime

#DisplayInfo
    def DisplayId(self):
        print("Id клиента:" + self.__id)

    def DisplayName(self):
        print("Имя клиента:" + self.getName())

    def DisplayAge(self):
        print("Возраст клиента:" + str(self.getAge()))

    def DisplayVisitTime(self):
        print("Время посещения клиентом зала:" + self.__visitTime)

    def DisplayAll(self):
        print("Id клиента:" + self.__id)
        print("Имя клиента:" + self.getName())
        print("Возраст клиента:" + str(self.getAge()))
        print("Время посещения клиентом зала:" + str(self.__visitTime))


    @staticmethod
    def displayCustomers():
        result = ""
        for i in Customer.__List:
            result+= str(i.getName()) + "\n" + "Возраст:" + str(i.getAge()) + "\n" + "Время посещения:" + str(i.getVisitTime()) + "\n"
        messagebox.showinfo("Пользователи", result)

#ChangeList
    @staticmethod
    def addCustomer(client):
        Customer.__List.append(client)

    @staticmethod
    def deleteCustomerByID(id):
        customers = Customer.getList()
        for customer in customers:
            if customer.getId() == id:
                customers.remove(customer)
                break

#GetInfo
    @staticmethod
    def isCustomerNameInTheList(customerName):
        for i in Customer.__List:
            if (i.getName() == customerName):
                return True
        return False

    @staticmethod
    def isCustomererIdInTheList(ID):
        for i in Customer.__List:
            if (i.getId() == ID):
                return True
        return False

    def createCopy(self):
        clientMas = lambda client: client.__repr__().split(',')
        customerCopyByMas = lambda clientMas: Customer(clientMas[0], int(clientMas[1]), int(clientMas[2]))
        logging.info('Была создана копия клиента ' + self.getName() + '.')
        return customerCopyByMas(clientMas(self))

    #Operator Overloading
    def __eq__(self, other):
        return self.getId()==other.getId()


    def __hash__(self):
        return hash((self.getName(), self.getAge(), self.getVisitTime()))

    def __repr__(self):
        return (str(self.getName())+","+str(self.getAge())+","+str(self.getVisitTime()))