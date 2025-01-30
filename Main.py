from Customer import Customer
from Trainer import Trainer
from Training import Training
from ClientTrainerList import ClientTrainerList

client1 = Customer("Ivan", 35, 12)
trainer1 = Trainer("Wasilii", 40, 15, "Power trainings")
training1 = Training("14:10", trainer1, client1, 90)

client2 = Customer("Vasya", 30, 10)
trainer2 = Trainer("Vanya", 44, 18, "Speed trainings")
training2 = Training("15:20", trainer2, client2, 120)

trainingList = [training1, training2]
clientList = [client1,client2]
clientsTrainerList = {}

for i in range(len(trainingList)):
    clientsTrainerList.update({trainingList[i].getCustomer():trainingList[i].getTrainer()})

for i in range(len(clientList)):
    print("Для клиента " + clientList[i].getName() + " тренером является " + clientsTrainerList.get(clientList[i]).getName() + ".")

ClientTrainerList.addPair(client1,trainer1)
ClientTrainerList.addPair(client2,trainer2)
ClientTrainerList.DisplayPairs()
ClientTrainerList.deletePair(client1)
ClientTrainerList.DisplayPairs()
