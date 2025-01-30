from Employee import Employee

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
