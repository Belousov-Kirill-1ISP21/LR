import abc
import logging

class Person(abc.ABC):

#Constructor
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

#Getters

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

#Setters

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

#DisplayInfo
    def DisplayName(self):
        print("Имя человека:" + self.__name)

    def DisplayAge(self):
        print("Возраст человека:" + str(self.__age))

    def DisplayAll(self):
        print(self.__name)
        print(self.__age)