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
    def createTrainer():
        trainerName = str(simpledialog.askstring("Создание тренера", "Введите имя тренера:")).replace(' ', '')
        trainerAge = simpledialog.askinteger("Создание тренера", "Введите возраст тренера:")
        expirience = simpledialog.askinteger("Создание тренера", "Введите опыт работы тренера:")
        specialisation = str(simpledialog.askstring("Создание тренера", "Введите специализацию тренера:")).replace(' ', '')
        if trainerName is not None and trainerAge is not None and expirience is not None and specialisation is not None:
            try:
                Trainer(trainerName, trainerAge, expirience,specialisation)
                messagebox.showinfo("Операция проведена успешно", "Тренер " + trainerName + " был успешно создан.")
            except ValueError:
                messagebox.showerror("Ошибка", "Пожалуйста, введите корректные данные.")

    @staticmethod
    def addTrainer(trainer):
        Trainer.__List.append(trainer)

    @staticmethod
    def changeInfo():
        trainerName = str(simpledialog.askstring("Изменение информации о тренере", "Введите имя тренера:")).replace(
            ' ', '')
        try:
            if trainerName is not None:
                trainer = Trainer.getTrainerByName(trainerName)
                if Trainer.isTrainerNameInTheList(trainerName):
                    trainerAge = simpledialog.askinteger("Изменение информации о тренере","Введите возраст тренера:")
                    expirience = simpledialog.askinteger("Создание тренера", "Введите опыт работы тренера:")
                    specialisation = str(simpledialog.askstring("Создание тренера", "Введите специализацию тренера:")).replace(' ', '')
                    if trainerAge is not None and expirience is not None and specialisation is not None:
                        trainer.setAge(trainerAge)
                        trainer.setExpirienceAge(expirience)
                        trainer.setSpecialisation(specialisation)
                        logging.info('Информация о тренере была изменена.')
                        messagebox.showinfo("Операция проведена успешно","Инфомрация о тренере " + trainerName + " была успешно изменена.")
                    else:
                        messagebox.showerror("Ошибка", "Пожалуйста, введите корректную информацию о тренере")
                else:
                    messagebox.showerror("Ошибка", "Нет тренера с таким именем.")
        except:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректное имя тренера.")

    @staticmethod
    def deleteTrainerById(id):
        Trainer.getList().pop(id)

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