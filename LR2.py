class Person:

#Constructor
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

#Getters

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

#Setters

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

#DisplayInfo
    def DisplayName(self):
        print("Имя человека:" + self.__name)

    def DisplayAge(self):
        print("Возраст человека:" + str(self.__age))

    def DisplayAll(self):
        print(self.__name)
        print(self.__age)
class Customer(Person):

# Constructor
    def __init__(self, name, age, visitTime):
        super().__init__(name, age)
        self.__visitTime = visitTime

#Getters

    def getVisitTime(self):
        return self.__visitTime

#Setters
    def setVisitTime(self, visitTime):
        self.__visitTime = visitTime

#DisplayInfo

    def DisplayVisitTime(self):
        print("Время посещения клиентом зала:" + self.__visitTime)

    def DisplayAll(self):
        print("Имя клиента:" + self.getName())
        print("Возраст клиента:" + str(self.getAge()))
        print("Время посещения клиентом зала:" + str(self.__visitTime))

class Employee(Person):

# Constructor
    def __init__(self, name, age, expirienceAge):
        super().__init__(name, age)
        self.__expirienceAge = expirienceAge

#Getters
    def getExpirienceAge(self):
        return self.__expirienceAge

#Setters
    def setExpirienceAge(self, expirienceAge):
        self.__expirienceAge = expirienceAge

#DisplayInfo
    def DisplayExpirienceAge(self):
        print("Стаж сотрудника:" + self.__expirienceAge)

    def DisplayAll(self):
        print("Имя сотрудника:" + self.getName())
        print("Возраст сотрудника:" + str(self.getAge()))
        print("Стаж сотрудника:" + str(self.__expirienceAge))

class Trainer(Employee):

# Constructor
    def __init__(self, name, age, expirienceAge, specialisation):
        super().__init__(name, age, expirienceAge)
        self.__specialisation = specialisation

#Getters
    def getSpecialisation(self):
        return self.__specialisation

#Setters
    def setSpecialisation(self, specialisation):
        self.__specialisation = specialisation


# DisplayInfo
    def DisplaySpecialisation(self):
        print("Специализация тренера:" + self.__specialisation)

    def DisplayAll(self):
        print("Имя тренера:" + self.getName())
        print("Возраст тренера:" + str(self.getAge()))
        print("Стаж тренера:" + str(self.getExpirienceAge()))
        print("Специализация тренера:" + self.__specialisation)

class Training:

# Constructor
    def __init__(self, time, trainer,customer,duration):
        self.__time = time
        self.__trainer = trainer
        self.__customer = customer
        self.__duration = duration

#Getters
    def getTime(self):
        return self.__time

    def getTrainer(self):
        return self.__trainer

    def getCustomer(self):
        return self.__customer

    def getDuration(self):
        return self.__duration

#Setters
    def setTrainer(self, trainer):
        self.__trainer = trainer

    def setCustomer(self, customer):
        self.__customer = customer

    def setDuration(self, duration):
        self.__duration = duration

    def setTime(self, time):
        self.__time = time

#DisplayInfo

    def DisplayTrainer(self):
        print("Тренер тренировки:" + self.__trainer)

    def DisplayCustomer(self):
        print("Клиент тренировки:" + self.__customer)

    def DisplayDuration(self):
        print("Продолжителньость тренировки:" + self.__duration)

    def DisplayTime(self):
        print("Время начала тренировки:" + self.__time)

    def DisplayAll(self):
        print("Тренер тренировки:" + self.__trainer.getName())
        print("Клиент тренировки:" + self.__customer.getName())
        print("Продолжителньость тренировки:" + str(self.__duration))
        print("Время начала тренировки:" + str(self.__time))


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


