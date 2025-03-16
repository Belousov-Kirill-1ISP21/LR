from Customer import Customer
from GUI import GUI
from loggingConfig import loggingConfig
from Trainer import Trainer
from Training import Training
from ClientTrainerList import ClientTrainerList

loggingConfig.setupLogging()
''
client1 = Customer("Ivan", 35, 12)
trainer1 = Trainer("Wasili", 40, 15, "Power trainings")
ClientTrainerList.addPairDirectly(client1, trainer1)
training1 = Training(0,"14:10", trainer1, client1, 90)

client2 = Customer("Sasha", 30, 10)
trainer2 = Trainer("Vanya", 44, 18, "Speed trainings")
ClientTrainerList.addPairDirectly(client2, trainer2)
training2 = Training(1,"15:20", trainer2, client2, 120)
''
GUI.start()






