import sys
from PyQt5.QtWidgets import QApplication
from Customer import Customer
from GUI import GUI
from loggingConfig import loggingConfig
from Trainer import Trainer
from Training import Training
from ClientTrainerList import ClientTrainerList

loggingConfig.setupLogging()
''
client1 = Customer(0,"Иван", 35, 12)
trainer1 = Trainer(0,"Василий", 40, 15, "Силовые тренировки")
training1 = Training(0,"14:10", trainer1, client1, 90)

client2 = Customer(1, "Саша", 30, 10)
trainer2 = Trainer(1,"Ваня", 44, 18, "Тренировки на скорость")
training2 = Training(1,"15:20", trainer2, client2, 120)

client3 = Customer(2, "Гена", 40, 15)
training3 = Training(2,"11:20", trainer2, client3, 90)
training4 = Training(3,"9:20", trainer1, client3, 110)

''

# Запуск приложения
app = QApplication(sys.argv)
window = GUI()
window.resize(800, 600)  # Установка размера окна
window.show()
sys.exit(app.exec_())






