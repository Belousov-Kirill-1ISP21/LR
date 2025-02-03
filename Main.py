from Customer import Customer
from Trainer import Trainer
from Training import Training
from ClientTrainerList import ClientTrainerList

client1 = Customer("Ivan", 35, 12)
trainer1 = Trainer("Wasili", 40, 15, "Power trainings")
training1 = Training("14:10", trainer1, client1, 90)

client2 = Customer("Sasha", 30, 10)
trainer2 = Trainer("Vanya", 44, 18, "Speed trainings")
training2 = Training("15:20", trainer2, client2, 120)

ClientTrainerList.addPair(client1, trainer1)
ClientTrainerList.addPair(client2, trainer2)
ClientTrainerList.DisplayPairs()

ClientTrainerList.deletePair(client1)
ClientTrainerList.DisplayPairs()

ClientTrainerList.addPair(client1, trainer2)
ClientTrainerList.changePair(client2, trainer1)
ClientTrainerList.DisplayPairs()

training3 = Training.createTraining()
training3.DisplayAll()
