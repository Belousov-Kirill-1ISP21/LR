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
    def createTraining():
        if len(Training.__List)!=0:
            id = Training.__List[-1].getId() + 1
        else:
            id=0

        clientName = str(simpledialog.askstring("Создание тренировки", "Введите имя клиента:")).replace(' ', '')
        trainerName = str(simpledialog.askstring("Создание тренировки", "Введите имя тренера:")).replace(' ', '')

        customer = Customer.getCustomerByName(clientName)
        trainer = Trainer.getTrainerByName(trainerName)

        time = str(simpledialog.askstring("Создание тренировки", "Введите время начала тренировки:")).replace(' ', '')
        duration = simpledialog.askinteger("Создание тренировки", "Введите продолжительность тренировки:")
        if customer is not None and trainer is not None and time is not None and duration is not None:
            try:
                Training(id, time, trainer, customer, duration)
                ClientTrainerList.addPairDirectly(customer, trainer)
                messagebox.showinfo("Операция проведена успешно", "Тренировка " + str(id) + " была успешно создана.")
            except ValueError:
                messagebox.showerror("Ошибка", "Пожалуйста, введите корректные данные.")


    @staticmethod
    def addTraining(training):
        Training.__List.append(training)

    @staticmethod
    def deleteTraining():
        user_input = simpledialog.askinteger("Удаление тренировки", "Введите индекс:")
        if user_input is not None:
            try:
                index = user_input
                if not index < 0 and not index > len(Training.getList()):
                    Training.__List.pop(index)
                    logging.info('Из списка была удалена тренировка.')
                    messagebox.showinfo("Операция проведена успешно", "Тренировка " + str(index) + " была успешно удалена.")
                else:
                    messagebox.showerror("Ошибка", "Тренировки по этому индексу нет.")
            except ValueError:
                messagebox.showerror("Ошибка", "Пожалуйста, введите корректное число.")

    @staticmethod
    def changeInfo():
        id = simpledialog.askinteger("Изменение информации о тренировке", "Введите ID тренировки:")
        try:
            if id is not None:
                training = Training.getTrainingById(id)
                if Training.isTrainingIdInTheList(id):
                    clientName = str(simpledialog.askstring("Создание тренировки", "Введите имя клиента:")).replace(' ','')
                    trainerName = str(simpledialog.askstring("Создание тренировки", "Введите имя тренера:")).replace(' ', '')

                    customer = Customer.getCustomerByName(clientName)
                    trainer = Trainer.getTrainerByName(trainerName)

                    time = str(simpledialog.askstring("Создание тренировки", "Введите время начала тренировки:")).replace(' ', '')
                    duration = simpledialog.askinteger("Создание тренировки", "Введите продолжительность тренировки:")

                    if customer is not None and trainer is not None and time is not None and duration is not None:
                        training.setTrainer(trainer)
                        training.setCustomer(customer)
                        ClientTrainerList.addPairDirectly(customer, trainer)
                        training.setDuration(duration)
                        training.setTime(time)
                        logging.info('Информация о тренировке была изменена.')
                        messagebox.showinfo("Операция проведена успешно", "Инфомрация о тренировке " + str(id) + " была успешно изменена.")
                    else:
                        messagebox.showerror("Ошибка", "Пожалуйста, введите корректную информацию о тренировке")
                else:
                    messagebox.showerror("Ошибка", "Нет тренировки с таким ID.")
        except:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректное ID тренировки.")

#GetInfo
    @staticmethod
    def isTrainingIdInTheList(ID):
        for i in Training.__List:
            if (i.getId() == ID):
                return True
        return False

#Operator Overloading
    def __eq__(self, other):
        return ((self.getTrainer()==other.getTrainer() and self.getCustomer()==other.getCustomer()
                and self.getTime() == other.getTime())
                and self.getDuration() == other.getDuration())

    def __hash__(self):
        return hash((self.getTrainer(), self.getCustomer(), self.getTime(), self.getDuration()))