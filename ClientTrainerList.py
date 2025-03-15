import logging
from tkinter import simpledialog, messagebox
from Customer import Customer
from Trainer import Trainer


class ClientTrainerList:
    __List = {}

#Getters
    @staticmethod
    def getList():
        return ClientTrainerList.__List

    @staticmethod
    def getTrainerByName(trainerName):
        for i in ClientTrainerList.__List:
            if (ClientTrainerList.__List[i].getName() == trainerName):
                return ClientTrainerList.__List[i]
        return None

    @staticmethod
    def getCustomerByName(clientName):
        for i in ClientTrainerList.__List:
            if (i.getName() == clientName):
                return i
        return None


#ChangeList

    @staticmethod
    def addPair():
        clientName = str(simpledialog.askstring("Добавление пары клиент-тренер", "Введите имя клиента:")).replace(' ', '')
        trainerName = str(simpledialog.askstring("Добавление пары клиент-тренер", "Введите имя тренера:")).replace(' ', '')
        if clientName is not None and trainerName is not None:
            try:
                if Customer.isCustomerNameInTheList(clientName):
                    if Trainer.isTrainerNameInTheList(trainerName):
                        client = Customer.getCustomerByName(clientName)
                        trainer = Trainer.getTrainerByName(trainerName)
                        ClientTrainerList.__List.update({client: trainer})
                        logging.info('В список была добавлена новая пара клиент-тренер.')
                        messagebox.showinfo("Операция проведена успешно","Пара " + clientName + " : " + trainerName + " была успешно добавлена.")
                    else:
                        messagebox.showerror("Ошибка", "Нет тренера с таким именем.")
                else:
                    messagebox.showerror("Ошибка", "Нет клиента с таким именем.")
            except ValueError:
                messagebox.showerror("Ошибка", "Пожалуйста, введите корректные имена.")


    @staticmethod
    def addPairDirectly(client,trainer):
        ClientTrainerList.__List.update({client: trainer})
        logging.info('В список была добавлена новая пара клиент-тренер.')

    @staticmethod
    def deletePair():
        clientName = str(simpledialog.askstring("Удаление пары клиент-тренер", "Введите имя клиента:")).replace (' ', '')
        if clientName is not None:
            try:
                client = ClientTrainerList.getCustomerByName(clientName)
                if ClientTrainerList.isCustomerNameInTheList(clientName):
                    trainerName = ClientTrainerList.getList()[client].getName()
                    ClientTrainerList.__List.pop(client)
                    logging.info('Из списка была удалена пара клиент-тренер.')
                    messagebox.showinfo("Операция проведена успешно", "Пара " + clientName + " : " + trainerName + " была успешно удалена.")
                else:
                    messagebox.showerror("Ошибка", "Нет пары с таким клиентом.")
            except ValueError:
                messagebox.showerror("Ошибка", "Пожалуйста, введите корректное имя клиента.")

    @staticmethod
    def changePair():
        clientName = str(simpledialog.askstring("Изменение пары клиент-тренер", "Введите имя клиента:")).replace(' ','')
        trainerName = str(simpledialog.askstring("Изменение пары клиент-тренер", "Введите имя тренера:")).replace(' ','')
        if clientName is not None and trainerName is not None:
            try:
                if ClientTrainerList.isCustomerNameInTheList(clientName):
                    if Trainer.isTrainerNameInTheList(trainerName):
                        client = Customer.getCustomerByName(clientName)
                        trainer = Trainer.getTrainerByName(trainerName)
                        ClientTrainerList.__List[client] = trainer
                        logging.info('Пара клиент-тренер была изменена.')
                        messagebox.showinfo("Операция проведена успешно", "Пара была успешно изменена на " + clientName + " : " + trainerName + " .")
                    else:
                        messagebox.showerror("Ошибка", "Нет тренера с таким именем.")
                else:
                    messagebox.showerror("Ошибка", "Нет пары с клиентом с таким именем.")
            except ValueError:
                messagebox.showerror("Ошибка", "Пожалуйста, введите корректные имена.")

#GetInfo
    @staticmethod
    def isTrainerNameInTheList(trainerName):
        for i in ClientTrainerList.__List:
            if (ClientTrainerList.__List[i].getName() == trainerName):
                return True
        return False

    @staticmethod
    def isCustomerNameInTheList(customerName):
        for i in ClientTrainerList.__List:
            if (i.getName() == customerName):
                return True
        return False

#DisplayInfo
    @staticmethod
    def DisplayPairs():
        result = ""
        for i in ClientTrainerList.__List:
            result += i.getName() + " : " + ClientTrainerList.__List[i].getName() + "\n"
        messagebox.showinfo("Тренера", result)

    @staticmethod
    def DisplayTrainers():
        print("Тренера:")
        for i in ClientTrainerList.__List:
            print(ClientTrainerList.__List[i].getName())



