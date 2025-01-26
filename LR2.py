class Person:

#Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Getters

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

#Setters

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

#DisplayInfo
    def DisplayName(self):
        print("Имя человека:" + self.name)

    def DisplayAge(self):
        print("Возраст человека:" + self.age)

    def DisplayAll(self):
        print(self.name)
        print(self.age)
class Customer(Person):

# Constructor
    def __init__(self, name, age, visitTime):
        super().__init__(name, age)
        self.visitTime = visitTime

#Getters

    def getVisitTime(self):
        return self.visitTime

#Setters
    def setVisitTime(self, visitTime):
        self.visitTime = visitTime

#DisplayInfo

    def DisplayVisitTime(self):
        print("Время посещения клиентом зала:" + self.visitTime)

    def DisplayAll(self):
        print("Имя клиента:" + self.name)
        print("Возраст клиента:" + self.age)
        print("Время посещения клиентом зала:" +self.visitTime)

class Employee(Person):

# Constructor
    def __init__(self, name, age, expirienceAge):
        super().__init__(name, age)
        self.expirienceAge = expirienceAge

#Getters
    def getExpirienceAge(self):
        return self.expirienceAge

#Setters
    def setExpirienceAge(self, expirienceAge):
        self.expirienceAge = expirienceAge

#DisplayInfo
    def DisplayExpirienceAge(self):
        print("Стаж сотрудника:" + self.expirienceAge)

    def DisplayAll(self):
        print("Имя сотрудника:" + self.name)
        print("Возраст сотрудника:" + self.age)
        print("Стаж сотрудника:" + self.expirienceAge)

class Trainer(Employee):

# Constructor
    def __init__(self, name, age, expirienceAge, specialisation):
        super().__init__(name, age, expirienceAge)
        self.specialisation = specialisation

#Getters
    def getSpecialisation(self):
        return self.specialisation

#Setters
    def setSpecialisation(self, specialisation):
        self.specialisation = specialisation


# DisplayInfo
    def DisplaySpecialisation(self):
        print("Специализация тренера:" + self.specialisation)

    def DisplayAll(self):
        print("Имя тренера:" + self.name)
        print("Возраст тренера:" + self.age)
        print("Стаж тренера:" + self.expirienceAge)
        print("Специализация тренера:" + self.specialisation)

class Training:

# Constructor
    def __init__(self, time, trainer,customer,duration):
        self.time = time
        self.trainer = trainer
        self.customer = customer
        self.duration = duration

#Getters
    def getTime(self):
        return self.time

    def getTrainer(self):
        return self.trainer

    def getCustomer(self):
        return self.customer

    def getDuration(self):
        return self.duration

#Setters
    def setTrainer(self, trainer):
        self.trainer = trainer

    def setCustomer(self, customer):
        self.customer = customer

    def setDuration(self, duration):
        self.duration = duration

    def setTime(self, time):
        self.time = time

#DisplayInfo

    def DisplayTrainer(self):
        print("Тренер тренировки:" + self.trainer)

    def DisplayCustomer(self):
        print("Клиент тренировки:" + self.customer)

    def DisplayDuration(self):
        print("Продолжителньость тренировки:" + self.duration)

    def DisplayTime(self):
        print("Время начала тренировки:" + self.time)

    def DisplayAll(self):
        print("Тренер тренировки:" + self.trainer.getName())
        print("Клиент тренировки:" + self.customer.getName())
        print("Продолжителньость тренировки:" + str(self.duration))
        print("Время начала тренировки:" + str(self.time))


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


