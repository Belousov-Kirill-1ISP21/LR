class ClientTrainerList:
    __List = {}

#Getters
    @staticmethod
    def getList():
        return ClientTrainerList.__List

    @staticmethod
    def getTrainerByName(trainerName):
        for i in ClientTrainerList.__List:
            if (ClientTrainerList.__List[i].getName() == trainerName):
                return ClientTrainerList.__List[i]

        print("Тренера с таким именем нет в списке.")
        return None

#ChangeList
    @staticmethod
    def addPair(client, trainer):
        ClientTrainerList.__List.update({client:trainer})

    @staticmethod
    def deletePair(client):
        ClientTrainerList.__List.pop(client)

    @staticmethod
    def changePair(client, trainer):
        ClientTrainerList.__List[client]=trainer

#DisplayInfo
    @staticmethod
    def DisplayPairs():
        for i in ClientTrainerList.__List:
            print(i.getName() + " : " + ClientTrainerList.__List[i].getName())

    @staticmethod
    def DisplayTrainers():
        print("Тренера:")
        for i in ClientTrainerList.__List:
            print(ClientTrainerList.__List[i].getName())



