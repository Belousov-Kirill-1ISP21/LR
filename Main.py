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

client4 = Customer("Sergey", 35, 12)
trainer4 = Trainer("Andrey", 40, 15, "Power trainings")
training4 = Training("14:10", trainer4, client4, 90)

client5 = Customer("Sasha", 30, 10)
trainer5 = Trainer("Vanya", 44, 18, "Speed trainings")
training5 = Training("15:20", trainer5, client5, 120)

print(client4 == client5)
print(client5 == client2)

print(trainer4 == trainer5)
print(trainer5 == trainer2)

print(training4 == training5)
print(training5 == training2)

training3 = Training.createTraining()
training3.DisplayAll()
