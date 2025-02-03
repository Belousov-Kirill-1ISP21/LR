from ClientTrainerList import ClientTrainerList
from Customer import Customer

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

#UserInput
    @staticmethod
    def createTraining():
        customer = Customer.createCustomer()
        trainerForClient = None
        duration = None
        time = None

        iter = False
        while (iter == False):
            print("Выберите тренера:")
            ClientTrainerList.DisplayTrainers()
            trainerForClientName = str(input()).replace(' ', '').replace(' ', '')
            if (ClientTrainerList.isTrainerNameInTheList(trainerForClientName)==True):
                trainerForClient = ClientTrainerList.getTrainerByName(trainerForClientName)
                iter = True
            else:
                print("Тренера с таким именем нет в списке.")


        iter = False
        while (iter == False):
            try:
                time = str(input("Введите время тренировки (часы:минуты):"))
                hoursAndMins = time.split(':')
                if (type(int(hoursAndMins[0])) == int and type(int(hoursAndMins[1])) == int):
                    iter = True
                else:
                    raise Exception
            except Exception:
                print("Время введено неверно. Формат времени: 14:13")

        while (type(duration)!=int):
            try:
                duration = int(input("Введите продолжительность тренировки в минутах:"))
            except:
                print("Число минут введено неверно. Введите только число.")

        training = Training(time, trainerForClient, customer, duration)
        return training

#Operator Overloading
    def __eq__(self, other):
        return ((self.getTrainer()==other.getTrainer() and self.getCustomer()==other.getCustomer()
                and self.getTime() == other.getTime())
                and self.getDuration() == other.getDuration())

    def __hash__(self):
        return hash((self.getTrainer(), self.getCustomer(), self.getTime(), self.getDuration()))