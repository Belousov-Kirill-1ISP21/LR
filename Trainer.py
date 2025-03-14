from Employee import Employee
import logging
from tkinter import simpledialog, messagebox

class Trainer(Employee):
    __List = []

# Constructor
    def __init__(self, name, age, expirienceAge, specialisation):
        super().__init__(name, age, expirienceAge)
        self.__specialisation = specialisation
        Trainer.addTrainer(self)
        logging.info('Был создан тренер ' + name + '.')

#Getters
    def getSpecialisation(self):
        return self.__specialisation

    @staticmethod
    def getList():
        return Trainer.__List

#Setters
    def setSpecialisation(self, specialisation):
        self.__specialisation = specialisation


#DisplayInfo
    def DisplayName(self):
        print("Имя тренера:" + self.getName())


    def DisplayAge(self):
        print("Возраст тренера:" + str(self.getAge()))

    def DisplaySpecialisation(self):
        print("Специализация тренера:" + self.__specialisation)

    def DisplayAll(self):
        print("Имя тренера:" + self.getName())
        print("Возраст тренера:" + str(self.getAge()))
        print("Стаж тренера:" + str(self.getExpirienceAge()))
        print("Специализация тренера:" + self.__specialisation)

    def DisplayInfo(self):
        iter=0
        while (iter==0):
            answer = str(input("Нужно ли указывать специализацию?")).replace (' ', '')
            if (answer=="Да"):
                self.DisplayAll()
                iter=1
            elif (answer=="Нет"):
                super().DisplayAll()
                iter=1
            else:
                print("Вы ввели что-то не то!")

    @staticmethod
    def createTrainer():
        trainerName = str(simpledialog.askstring("Создание тренера", "Введите имя тренера:")).replace(' ', '')
        trainerAge = simpledialog.askinteger("Создание тренера", "Введите возраст тренера:")
        expirienceAge = simpledialog.askinteger("Создание тренера", "Введите опыт работы тренера:")
        specialisation = str(simpledialog.askstring("Создание тренера", "Введите специализацию тренера:")).replace(' ', '')
        if trainerName is not None and trainerAge is not None and expirienceAge is not None and specialisation is not None:
            try:
                Trainer(trainerName, trainerAge, expirienceAge,specialisation)
                messagebox.showinfo("Операция проведена успешно", "Тренер " + trainerName + " был успешно создан.")
            except ValueError:
                messagebox.showerror("Ошибка", "Пожалуйста, введите корректные данные.")

    @staticmethod
    def addTrainer(trainer):
        Trainer.__List.append(trainer)

    @staticmethod
    def deleteTrainer():
        user_input = simpledialog.askinteger("Удаление тренера", "Введите индекс:")
        if user_input is not None:
            try:
                index = user_input
                if not index < 0 and not index > len(Trainer.getList()):
                    name = Trainer.getList()[index].getName()
                    Trainer.__List.pop(index)
                    logging.info('Из списка был удалён тренер.')
                    messagebox.showinfo("Операция проведена успешно", "Тренер " + name + " был успешно удалён.")
                else:
                    messagebox.showerror("Ошибка", "Тренера по этому индексу нет.")
            except ValueError:
                messagebox.showerror("Ошибка", "Пожалуйста, введите корректное число.")
    @staticmethod
    def displayTrainers():
        result = ""
        for i in Trainer.__List:
            result += str(i.getName()) + "\n"
        messagebox.showinfo("Тренера", result)

    @staticmethod
    def getTrainerByName(clientName):
        for i in Trainer.__List:
            if (i.getName() == clientName):
                return i
        return None

    @staticmethod
    def isTrainerNameInTheList(trainerName):
        for i in Trainer.__List:
            if (i.getName() == trainerName):
                return True
        return False

#Operator Overloading
    def __eq__(self, other):
        return ((self.getName()==other.getName() and self.getAge()==other.getAge()
                and self.getExpirienceAge() == other.getExpirienceAge())
                and self.getSpecialisation() == other.getSpecialisation())

    def __hash__(self):
        return hash((self.getName(), self.getAge(), self.getExpirienceAge(), self.getSpecialisation()))