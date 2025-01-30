class ClientTrainerList:
    __List = {}

    @staticmethod
    def getList():
        return ClientTrainerList.__List

    @staticmethod
    def addPair(client, trainer):
        ClientTrainerList.__List.update({client:trainer})

    @staticmethod
    def deletePair(client):
        ClientTrainerList.__List.pop(client)

    @staticmethod
    def DisplayPairs():
        for i in ClientTrainerList.__List:
            print(i.getName() + " : " + ClientTrainerList.__List[i].getName())
