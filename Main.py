from Customer import Customer
from Trainer import Trainer
from Training import Training
from ClientTrainerList import ClientTrainerList

def findMaxAge(mas):
    maxage = 0
    for i in mas:
        for j in i:
            if (j.getAge()>maxage):
                maxage=j.getAge()
    return maxage

client1 = Customer("Ivan", 35, 12)
trainer1 = Trainer("Wasili", 40, 15, "Power trainings")
training1 = Training("14:10", trainer1, client1, 90)

client2 = Customer("Sasha", 30, 10)
trainer2 = Trainer("Vanya", 44, 18, "Speed trainings")
training2 = Training("15:20", trainer2, client2, 120)

client1.setAge(36)
client1.DisplayAge()

client1Str=client1.__repr__()
client1Mas=client1Str.split(',')
client3=Customer(client1Mas[0],int(client1Mas[1]),int(client1Mas[2]))
print(client1==client3)

listOfPairs = [[client1, trainer1], [client2, trainer2]]
print(findMaxAge(listOfPairs))

ClientTrainerList.addPair(client1, trainer1)
ClientTrainerList.addPair(client2, trainer2)

# print(trainer1.__specialisation) Выдаёт ошибку, так как атрибут защищённый
trainer1.DisplayInfo()
training3 = Training.createTraining()
training3.DisplayAll()

