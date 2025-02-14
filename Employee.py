from Person import Person

class Employee(Person):

# Constructor
    def __init__(self, name, age, expirienceAge):
        super().__init__(name, age)
        self.__expirienceAge = expirienceAge

#Getters
    def getExpirienceAge(self):
        return self.__expirienceAge

#Setters
    def setExpirienceAge(self, expirienceAge):
        self.__expirienceAge = expirienceAge

#DisplayInfo
    def DisplayName(self):
        print("Имя сотрудника:" + self.getName())

    def DisplayAge(self):
        print("Возраст сотрудника:" + str(self.getAge()))

    def DisplayExpirienceAge(self):
        print("Стаж сотрудника:" + self.__expirienceAge)

    def DisplayAll(self):
        print("Имя сотрудника:" + self.getName())
        print("Возраст сотрудника:" + str(self.getAge()))
        print("Стаж сотрудника:" + str(self.__expirienceAge))

