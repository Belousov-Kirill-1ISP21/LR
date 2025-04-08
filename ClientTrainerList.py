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
    def addPairDirectly(client,trainer):
        ClientTrainerList.__List.update({client: trainer})
        logging.info('В список была добавлена новая пара клиент-тренер.')

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



