from OP.Employee import Employee

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


#DisplayInfo
    def DisplayName(self):
        print("Имя тренера:" + self.getName())


    def DisplayAge(self):
        print("Возраст тренера:" + str(self.getAge()))

    def DisplaySpecialisation(self):
        print("Специализация тренера:" + self.__specialisation)

    def DisplayAll(self):
        print("Имя тренера:" + self.getName())
        print("Возраст тренера:" + str(self.getAge()))
        print("Стаж тренера:" + str(self.getExpirienceAge()))
        print("Специализация тренера:" + self.__specialisation)

    def DisplayInfo(self):
        iter=0
        while (iter==0):
            answer = str(input("Нужно ли указывать специализацию?")).replace (' ', '')
            if (answer=="Да"):
                self.DisplayAll()
                iter=1
            elif (answer=="Нет"):
                super().DisplayAll()
                iter=1
            else:
                print("Вы ввели что-то не то!")

#Operator Overloading
    def __eq__(self, other):
        return ((self.getName()==other.getName() and self.getAge()==other.getAge()
                and self.getExpirienceAge() == other.getExpirienceAge())
                and self.getSpecialisation() == other.getSpecialisation())

    def __hash__(self):
        return hash((self.getName(), self.getAge(), self.getExpirienceAge(), self.getSpecialisation()))