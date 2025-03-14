import tkinter as tk
from Customer import Customer
from Trainer import Trainer
from Training import Training
from ClientTrainerList import ClientTrainerList


class GUI:
    @staticmethod
    def onButtonClick(button_name):
        if (button_name=="Создать клиента"):
            Customer.createCustomer()
        elif (button_name == "Создать тренера"):
            Trainer.createTrainer()
        elif (button_name == "Создать тренировку"):
            Training.createTraining()
        elif (button_name == "Добавить пару клиент-тренер"):
            ClientTrainerList.addPair()
        elif (button_name == "Изменить пару клиент-тренер"):
            ClientTrainerList.changePair()
        elif (button_name == "Посмотреть клиентов"):
            Customer.displayCustomers()
        elif (button_name == "Посмотреть тренеров"):
            Trainer.displayTrainers()
        elif (button_name == "Посмотреть тренировки"):
            Training.displayTrainings()
        elif (button_name == "Посмотреть пары клиент-тренер"):
            ClientTrainerList.DisplayPairs()
        elif (button_name == "Удалить клиента"):
            Customer.deleteCustomer()
        elif (button_name == "Удалить тренера"):
            Trainer.deleteTrainer()
        elif (button_name == "Удалить тренировку"):
            Training.deleteTraining()
        elif (button_name == "Удалить пару клиент-тренер"):
            ClientTrainerList.deletePair()

    @staticmethod
    def start():
        # Создание основного окна
        root = tk.Tk()
        root.title("Простой интерфейс с кнопками")
        root.geometry("666x666")

        # Создание кнопок
        button1 = tk.Button(root, text="Создать клиента", command=lambda: GUI.onButtonClick("Создать клиента"))
        button1.pack(pady=10)  # Отображение кнопки с отступом по вертикали

        button2 = tk.Button(root, text="Создать тренера", command=lambda: GUI.onButtonClick("Создать тренера"))
        button2.pack(pady=10)

        button3 = tk.Button(root, text="Создать тренировку", command=lambda: GUI.onButtonClick("Создать тренировку"))
        button3.pack(pady=10)

        button4 = tk.Button(root, text="Добавить пару клиент-тренер", command=lambda: GUI.onButtonClick("Добавить пару клиент-тренер"))
        button4.pack(pady=10)

        button5 = tk.Button(root, text="Изменить пару клиент-тренер", command=lambda: GUI.onButtonClick("Изменить пару клиент-тренер"))
        button5.pack(pady=10)

        button6 = tk.Button(root, text="Посмотреть клиентов", command=lambda: GUI.onButtonClick("Посмотреть клиентов"))
        button6.pack(pady=10)

        button7 = tk.Button(root, text="Посмотреть тренеров", command=lambda: GUI.onButtonClick("Посмотреть тренеров"))
        button7.pack(pady=10)

        button8 = tk.Button(root, text="Посмотреть тренировки", command=lambda: GUI.onButtonClick("Посмотреть тренировки"))
        button8.pack(pady=10)

        button9 = tk.Button(root, text="Посмотреть пары клиент-тренер", command=lambda: GUI.onButtonClick("Посмотреть пары клиент-тренер"))
        button9.pack(pady=10)

        button10 = tk.Button(root, text="Удалить клиента", command=lambda: GUI.onButtonClick("Удалить клиента"))
        button10.pack(pady=10)

        button11 = tk.Button(root, text="Удалить тренера", command=lambda: GUI.onButtonClick("Удалить тренера"))
        button11.pack(pady=10)  # Отображение кнопки с отступом по вертикали

        button12 = tk.Button(root, text="Удалить тренировку", command=lambda: GUI.onButtonClick("Удалить тренировку"))
        button12.pack(pady=10)

        button13 = tk.Button(root, text="Удалить пару клиент-тренер",command=lambda: GUI.onButtonClick("Удалить пару клиент-тренер"))
        button13.pack(pady=10)  # Отображение кнопки с отступом по вертикали

        # Запуск основного цикла приложения

        root.mainloop()
