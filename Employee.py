from Person import Person
import logging

class Employee(Person):

# Constructor
    def __init__(self, name, age, expirience):
        super().__init__(name, age)
        self.__expirience = expirience

#Getters
    def getExpirience(self):
        return self.__expirience

#Setters
    def setExpirience(self, expirience):
        self.__expirience = expirience

#DisplayInfo
    def DisplayName(self):
        print("Имя сотрудника:" + self.getName())

    def DisplayAge(self):
        print("Возраст сотрудника:" + str(self.getAge()))

    def DisplayExpirience(self):
        print("Стаж сотрудника:" + self.__expirience)

    def DisplayAll(self):
        print("Имя сотрудника:" + self.getName())
        print("Возраст сотрудника:" + str(self.getAge()))
        print("Стаж сотрудника:" + str(self.__expirience))

