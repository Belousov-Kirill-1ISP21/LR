from Person import Person
class Customer(Person):

# Constructor
    def __init__(self, name, age, visitTime):
        super().__init__(name, age)
        self.__visitTime = visitTime

#Getters

    def getVisitTime(self):
        return self.__visitTime

#Setters
    def setVisitTime(self, visitTime):
        self.__visitTime = visitTime

#DisplayInfo

    def DisplayVisitTime(self):
        print("Время посещения клиентом зала:" + self.__visitTime)

    def DisplayAll(self):
        print("Имя клиента:" + self.getName())
        print("Возраст клиента:" + str(self.getAge()))
        print("Время посещения клиентом зала:" + str(self.__visitTime))

#UserInput
    @staticmethod
    def createCustomer():
        customerName = str(input("Введите имя клиента:")).replace (' ', '')
        customerAge = None
        while (type(customerAge)!=int):
            try:
                customerAge = int(input("Введите возраст клиента:"))
            except:
                print("Возраст введён неверно. Введите только число полных лет.")

        customer = Customer(customerName,customerAge,0)
        return customer

    #Operator Overloading
    def __eq__(self, other):
        return (self.getName()==other.getName() and self.getAge()==other.getAge()
                and self.getVisitTime() == other.getVisitTime())


    def __hash__(self):
        return hash((self.getName(), self.getAge(), self.getVisitTime()))