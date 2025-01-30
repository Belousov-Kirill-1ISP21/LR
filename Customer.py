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
