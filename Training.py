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
