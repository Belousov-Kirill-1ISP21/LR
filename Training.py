from ClientTrainerList import ClientTrainerList
from Trainer import Trainer
from Customer import Customer
import logging
from tkinter import simpledialog, messagebox


class Training:
    __List = []

# Constructor
    def __init__(self,id, time, trainer,customer,duration):
        self.__id = id
        self.__time = time
        self.__trainer = trainer
        self.__customer = customer
        self.__duration = duration
        Training.addTraining(self)
        ClientTrainerList.addPairDirectly(customer, trainer)
        logging.info('Был создана новая тренировка')

#Getters

    def getId(self):
        return self.__id
    def getTime(self):
        return self.__time

    def getTrainer(self):
        return self.__trainer

    def getCustomer(self):
        return self.__customer

    def getDuration(self):
        return self.__duration

    @staticmethod
    def getList():
        return Training.__List

    @staticmethod
    def getTrainingById(ID):
        for i in Training.__List:
            if (i.getId() == ID):
                return i
        return None

#Setters
    def setId(self, id):
        self.__Id = id

    def setTrainer(self, trainer):
        self.__trainer = trainer

    def setCustomer(self, customer):
        self.__customer = customer

    def setDuration(self, duration):
        self.__duration = duration

    def setTime(self, time):
        self.__time = time


#DisplayInfo

    def DisplayId(self):
        print("Id тренировки:" + self.__id)

    def DisplayTrainer(self):
        print("Тренер тренировки:" + self.__trainer)

    def DisplayCustomer(self):
        print("Клиент тренировки:" + self.__customer)

    def DisplayDuration(self):
        print("Продолжителньость тренировки:" + self.__duration)

    def DisplayTime(self):
        print("Время начала тренировки:" + self.__time)

    def DisplayAll(self):
        print("Id тренировки:" + self.__id)
        print("Тренер тренировки:" + self.__trainer.getName())
        print("Клиент тренировки:" + self.__customer.getName())
        print("Продолжителньость тренировки:" + str(self.__duration))
        print("Время начала тренировки:" + str(self.__time))

    @staticmethod
    def displayTrainings():
        result = ""
        for i in range(len(Training.__List)):
            result += ("Тренировка " + str(Training.__List[i].__id) + ":\n" +
                       "Тренер тренировки:" + Training.__List[i].__trainer.getName() + "\n" +
                       "Клиент тренировки:" + Training.__List[i].__customer.getName() + "\n" +
                       "Продолжителньость тренировки:" + str(Training.__List[i].__duration) + "\n" +
                       "Время начала тренировки:" + str(Training.__List[i].__time)) + "\n"
        messagebox.showinfo("Тренировки", result)

#ChangeList

    @staticmethod
    def addTraining(training):
        Training.__List.append(training)

    @staticmethod
    def deleteTrainingById(id):
        trainings = Training.getList()
        for training in trainings:
            if training.getId() == id:
                trainings.remove(training)
                break


#GetInfo
    @staticmethod
    def isTrainingIdInTheList(ID):
        for i in Training.__List:
            if (i.getId() == ID):
                return True
        return False

#Operator Overloading
    def __eq__(self, other):
        return self.getId()==other.getId()

    def __hash__(self):
        return hash((self.getTrainer(), self.getCustomer(), self.getTime(), self.getDuration()))