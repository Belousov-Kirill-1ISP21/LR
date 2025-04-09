from Employee import Employee
import logging
from tkinter import simpledialog, messagebox

class Trainer(Employee):
    __List = []

# Constructor
    def __init__(self, id, name, age, expirience, specialisation):
        self.__id = id
        super().__init__(name, age, expirience)
        self.__specialisation = specialisation
        Trainer.addTrainer(self)
        logging.info('Был создан тренер ' + name + '.')

#Getters
    def getId(self):
        return self.__id

    def getSpecialisation(self):
        return self.__specialisation

    @staticmethod
    def getList():
        return Trainer.__List

    @staticmethod
    def getTrainerByName(clientName):
        for i in Trainer.__List:
            if (i.getName() == clientName):
                return i
        return None

    @staticmethod
    def getTrainerById(ID):
        for i in Trainer.__List:
            if (i.getId() == ID):
                return i
        return None

#Setters
    def setId(self, id):
        self.__Id = id

    def setSpecialisation(self, specialisation):
        self.__specialisation = specialisation


#DisplayInfo
    def DisplayId(self):
        print("Id тренера:" + self.__id)

    def DisplayName(self):
        print("Имя тренера:" + self.getName())


    def DisplayAge(self):
        print("Возраст тренера:" + str(self.getAge()))

    def DisplaySpecialisation(self):
        print("Специализация тренера:" + self.__specialisation)

    def DisplayAll(self):
        print("Id тренера:" + self.__id)
        print("Имя тренера:" + self.getName())
        print("Возраст тренера:" + str(self.getAge()))
        print("Стаж тренера:" + str(self.getExpirience()))
        print("Специализация тренера:" + self.__specialisation)

    @staticmethod
    def displayTrainers():
        result = ""
        for i in Trainer.__List:
            result += str(i.getName()) + "\n" + "Возраст:" + str(i.getAge()) + "\n" + "Опыт работы:" + str(
                i.getExpirience()) + "\n" + "Специализация:" + str(i.getSpecialisation()) + "\n"
        messagebox.showinfo("Тренера", result)

#ChangeList

    @staticmethod
    def addTrainer(trainer):
        Trainer.__List.append(trainer)

    @staticmethod
    def deleteTrainerById(id):
        trainers = Trainer.getList()
        for trainer in trainers:
            if trainer.getId() == id:
                trainers.remove(trainer)
                break

#GetInfo
    @staticmethod
    def isTrainerNameInTheList(trainerName):
        for i in Trainer.__List:
            if (i.getName() == trainerName):
                return True
        return False

    @staticmethod
    def isTrainerIdInTheList(ID):
        for i in Trainer.__List:
            if (i.getId() == ID):
                return True
        return False

#Operator Overloading
    def __eq__(self, other):
        return self.getId()==other.getId()

    def __hash__(self):
        return hash((self.getName(), self.getAge(), self.getExpirience(), self.getSpecialisation()))