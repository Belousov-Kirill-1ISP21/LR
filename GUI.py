from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QFrame, QScrollArea, QCheckBox, \
    QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
from Customer import Customer
from Training import Training
from Trainer import Trainer


class GUI(QWidget):
    def __init__(self):
        super().__init__()

        #Настройка главного окна
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.setFixedSize(1222, 777)

        #Видимость основных вкладок
        self.__isClientWidgetVisible = False
        self.__isTrainerWidgetVisible = False
        self.__isTrainingWidgetVisible = False
        self.__isRelationsWidgetVisible = False

        #Основные вкладки
        self.clientWidget = QWidget()
        self.trainerWidget = QWidget()
        self.trainingWidget = QWidget()
        self.relationsWidget = QWidget()

        #Области прокруток основных вкладок
        self.currentClientRow = None
        self.scrollClientlayout = QVBoxLayout()

        self.currentTrainerRow = None
        self.scrollTrainerlayout = QVBoxLayout()

        self.currentTrainingRow = None
        self.scrollTraininglayout = QVBoxLayout()

        self.column1 = QVBoxLayout()
        self.column2 = QVBoxLayout()
        self.column3 = QVBoxLayout()

        #Создание главного окна
        self.сreateMainWindow()

        #Создание основных вкладок
        self.сreateClientWindow()
        self.сreateTrainerWindow()
        self.сreateTrainingWindow()
        self.сreateRelationsWindow()





    # Создание главного окна
    def сreateMainWindow(self):

        self.main_layout.setAlignment(Qt.AlignTop)

        self.main_layout.setContentsMargins(10, 10, 10, 10)

        self.main_layout.addSpacing(24)

        title_label = QLabel('Программа для администрирования спортзала')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 16px;")
        self.main_layout.addWidget(title_label)

        self.main_layout.addSpacing(24)

        button_layout = QHBoxLayout()

        clientButton = QPushButton("Управление клиентами ↓")
        trainerButton = QPushButton("Управление тренерами ↓")
        trainingButton = QPushButton("Управление тренировками ↓")
        relationsButton = QPushButton("Посмотреть связи ↓")

        clientButton.clicked.connect(lambda: self.showHideClient())
        trainerButton.clicked.connect(lambda: self.showHideTrainer())
        trainingButton.clicked.connect(lambda: self.showHideTraining())
        relationsButton.clicked.connect(lambda: self.showHideRelations())

        for button in [clientButton, trainerButton, trainingButton, relationsButton]:
            button.setStyleSheet("font-size: 16px; padding: 10px 20px;")

        button_layout.addWidget(clientButton)
        button_layout.addWidget(trainerButton)
        button_layout.addWidget(trainingButton)
        button_layout.addWidget(relationsButton)

        self.main_layout.addLayout(button_layout)

        self.main_layout.addSpacing(24)

#Создание основных вкладок
    def сreateClientWindow(self):
        self.clientWidget = QWidget()

        clientLayout = QVBoxLayout()

        rectangle_frame = QWidget()
        rectangle_frame.setStyleSheet("border: 2px solid black;")
        rectangle_frame.setFixedSize(1192, 444)

        rectangle_layout = QVBoxLayout()

        rectangle_label = QLabel("Клиенты")
        rectangle_label.setAlignment(Qt.AlignTop)
        rectangle_label.setAlignment(Qt.AlignHCenter)
        rectangle_label.setStyleSheet("font-size: 18px; font-weight: bold; border: none;")

        scroll_area = QScrollArea()
        scroll_area.setStyleSheet("border: none;")
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        scroll_content = QFrame()
        self.scrollClientlayout = QVBoxLayout(scroll_content)

        scroll_area.setWidget(scroll_content)

        rectangle_layout.addSpacing(22)
        rectangle_layout.addWidget(rectangle_label)
        rectangle_layout.addWidget(scroll_area)

        self.scrollClientlayout.addSpacing(10)
        self.renderClientCards()
        self.scrollClientlayout.addSpacing(44)

        rectangle_frame.setLayout(rectangle_layout)

        clientLayout.addWidget(rectangle_frame)

        clientLayout.addSpacing(44)

        bottomButtonLayout = QHBoxLayout()
        firstBotButton = QPushButton("Добавить клиента")
        secondBotButton = QPushButton("Внести изменения")
        thirdBotButton = QPushButton("Удалить клиента")
        firstBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        secondBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        thirdBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        firstBotButton.clicked.connect(lambda: self.addNewClient())
        secondBotButton.clicked.connect(lambda: self.changeClient())
        thirdBotButton.clicked.connect(lambda: self.deleteClient())
        bottomButtonLayout.addWidget(firstBotButton)
        bottomButtonLayout.addSpacing(111)
        bottomButtonLayout.addWidget(secondBotButton)
        bottomButtonLayout.addSpacing(111)
        bottomButtonLayout.addWidget(thirdBotButton)

        clientLayout.addLayout(bottomButtonLayout)

        self.clientWidget.setLayout(clientLayout)
        self.clientWidget.hide()

        self.main_layout.addWidget(self.clientWidget)

    def сreateTrainerWindow(self):
        self.trainerWidget = QWidget()

        trainerLayout = QVBoxLayout()

        rectangle_frame = QFrame()
        rectangle_frame.setStyleSheet(
            "border: 2px solid black;")
        rectangle_frame.setFixedSize(1192, 444)

        rectangle_layout = QVBoxLayout()

        rectangle_label = QLabel("Тренера")
        rectangle_label.setAlignment(Qt.AlignTop)
        rectangle_label.setAlignment(Qt.AlignHCenter)
        rectangle_label.setStyleSheet("font-size: 18px; font-weight: bold; border: none;")

        scroll_area = QScrollArea()
        scroll_area.setStyleSheet("border: none;")
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        scroll_content = QFrame()
        self.scrollTrainerlayout = QVBoxLayout(scroll_content)

        scroll_area.setWidget(scroll_content)

        rectangle_layout.addSpacing(22)
        rectangle_layout.addWidget(rectangle_label)
        rectangle_layout.addWidget(scroll_area)

        self.scrollTrainerlayout.addSpacing(10)
        self.renderTrainerCards()
        self.scrollTrainerlayout.addSpacing(44)

        rectangle_frame.setLayout(rectangle_layout)

        trainerLayout.addWidget(rectangle_frame)

        trainerLayout.addSpacing(44)

        bottomButtonLayout = QHBoxLayout()
        firstBotButton = QPushButton("Добавить тренера")
        secondBotButton = QPushButton("Внести изменения")
        thirdBotButton = QPushButton("Удалить тренера")
        firstBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        secondBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        thirdBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        firstBotButton.clicked.connect(lambda: self.addNewTrainer())
        secondBotButton.clicked.connect(lambda: self.changeTrainer())
        thirdBotButton.clicked.connect(lambda: self.deleteTrainer())

        bottomButtonLayout.addWidget(firstBotButton)
        bottomButtonLayout.addSpacing(111)
        bottomButtonLayout.addWidget(secondBotButton)
        bottomButtonLayout.addSpacing(111)
        bottomButtonLayout.addWidget(thirdBotButton)

        trainerLayout.addLayout(bottomButtonLayout)

        self.trainerWidget.setLayout(trainerLayout)
        self.trainerWidget.hide()

        self.main_layout.addWidget(self.trainerWidget)

    def сreateTrainingWindow(self):
        self.trainingWidget = QWidget()

        trainingLayout = QVBoxLayout()

        rectangle_frame = QFrame()
        rectangle_frame.setStyleSheet(
            "border: 2px solid black;")
        rectangle_frame.setFixedSize(1192, 444)

        rectangle_layout = QVBoxLayout()

        rectangle_label = QLabel("Тренировки")
        rectangle_label.setAlignment(Qt.AlignTop)
        rectangle_label.setAlignment(Qt.AlignHCenter)
        rectangle_label.setStyleSheet("font-size: 18px; font-weight: bold; border: none;")

        scroll_area = QScrollArea()
        scroll_area.setStyleSheet("border: none;")
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        scroll_content = QFrame()
        self.scrollTraininglayout = QVBoxLayout(scroll_content)

        scroll_area.setWidget(scroll_content)

        rectangle_layout.addSpacing(22)
        rectangle_layout.addWidget(rectangle_label)
        rectangle_layout.addWidget(scroll_area)

        self.scrollTraininglayout.addSpacing(10)
        self.renderTrainingCards()
        self.scrollTraininglayout.addSpacing(44)

        rectangle_frame.setLayout(rectangle_layout)

        trainingLayout.addWidget(rectangle_frame)

        trainingLayout.addSpacing(44)

        bottomButtonLayout = QHBoxLayout()
        firstBotButton = QPushButton("Добавить тренировку")
        secondBotButton = QPushButton("Внести изменения")
        thirdBotButton = QPushButton("Удалить тренировку")
        firstBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        secondBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        thirdBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        firstBotButton.clicked.connect(lambda: self.addNewTraining())
        secondBotButton.clicked.connect(lambda: self.changeTraining())
        thirdBotButton.clicked.connect(lambda: self.deleteTraining())

        bottomButtonLayout.addWidget(firstBotButton)
        bottomButtonLayout.addSpacing(111)
        bottomButtonLayout.addWidget(secondBotButton)
        bottomButtonLayout.addSpacing(111)
        bottomButtonLayout.addWidget(thirdBotButton)

        trainingLayout.addLayout(bottomButtonLayout)

        self.trainingWidget.setLayout(trainingLayout)
        self.trainingWidget.hide()

        self.main_layout.addWidget(self.trainingWidget)

    def сreateRelationsWindow(self):
        self.relationsWidget = QWidget()

        relationsLayout = QVBoxLayout()

        rectangle_frame = QFrame()
        rectangle_frame.setStyleSheet("border: 2px solid black;")
        rectangle_frame.setFixedSize(1192, 444)

        rectangle_layout = QVBoxLayout()

        header_widget = QWidget()
        header_widget.setStyleSheet("border: none;")
        header_layout = QHBoxLayout(header_widget)
        header_layout.setContentsMargins(10, 22, 10, 10)
        header_layout.setSpacing(20)

        titles = ["Клиенты", "Тренировки", "Тренера"]
        for title in titles:
            header_label = QLabel(title)
            header_label.setAlignment(Qt.AlignCenter)
            header_label.setStyleSheet("font-size: 18px; font-weight: bold; border: none;")
            header_layout.addWidget(header_label)

        scroll_area = QScrollArea()
        scroll_area.setStyleSheet("border: none;")
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        scroll_content = QFrame()
        scroll_layout = QHBoxLayout(scroll_content)

        self.column1 = QVBoxLayout()
        self.column2 = QVBoxLayout()
        self.column3 = QVBoxLayout()

        for column in [self.column1, self.column2, self.column3]:
            column.setSpacing(44)
            column.setContentsMargins(5, 5, 44, 5)
            scroll_layout.addLayout(column)

        scroll_area.setWidget(scroll_content)

        rectangle_layout.addWidget(header_widget)
        rectangle_layout.addWidget(scroll_area)

        self.renderRelationsCards()
        scroll_layout.addSpacing(44)

        rectangle_frame.setLayout(rectangle_layout)

        relationsLayout.addWidget(rectangle_frame)

        relationsLayout.addSpacing(44)

        bottomButtonLayout = QHBoxLayout()
        firstBotButton = QPushButton("Показать связи клиента")
        secondBotButton = QPushButton("Показать связи тренировки")
        thirdBotButton = QPushButton("Показать связи тренера")
        firstBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        secondBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        thirdBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        firstBotButton.clicked.connect(lambda: self.showClientRelations())
        secondBotButton.clicked.connect(lambda: self.showTrainingRelations())
        thirdBotButton.clicked.connect(lambda: self.showTrainerRelations())
        bottomButtonLayout.addWidget(firstBotButton)
        bottomButtonLayout.addSpacing(111)
        bottomButtonLayout.addWidget(secondBotButton)
        bottomButtonLayout.addSpacing(111)
        bottomButtonLayout.addWidget(thirdBotButton)

        relationsLayout.addLayout(bottomButtonLayout)

        self.relationsWidget.setLayout(relationsLayout)
        self.relationsWidget.hide()

        self.main_layout.addWidget(self.relationsWidget)

#Показ и скрывание вкладок
    def showHideClient(self):
        if (self.__isClientWidgetVisible == True):
            self.clientWidget.hide()
        else:
            self.clientWidget.show()
            self.trainerWidget.hide()
            self.trainingWidget.hide()
            self.relationsWidget.hide()
            self.__isTrainerWidgetVisible = False
            self.__isTrainingWidgetVisible = False
            self.__isRelationsWidgetVisible = False

        self.__isClientWidgetVisible = not self.__isClientWidgetVisible

    def showHideTrainer(self):
        if (self.__isTrainerWidgetVisible == True):
            self.trainerWidget.hide()
        else:
            self.trainerWidget.show()
            self.clientWidget.hide()
            self.trainingWidget.hide()
            self.relationsWidget.hide()
            self.__isClientWidgetVisible = False
            self.__isTrainingWidgetVisible = False
            self.__isRelationsWidgetVisible = False


        self.__isTrainerWidgetVisible = not self.__isTrainerWidgetVisible

    def showHideTraining(self):
        if (self.__isTrainingWidgetVisible == True):
            self.trainingWidget.hide()
        else:
            self.trainingWidget.show()
            self.clientWidget.hide()
            self.trainerWidget.hide()
            self.relationsWidget.hide()
            self.__isClientWidgetVisible = False
            self.__isTrainerWidgetVisible = False
            self.__isRelationsWidgetVisible = False

        self.__isTrainingWidgetVisible = not self.__isTrainingWidgetVisible

    def showHideRelations(self):
        if (self.__isRelationsWidgetVisible == True):
            self.relationsWidget.hide()
        else:
            self.relationsWidget.show()
            self.renderRelationsCards()
            self.clientWidget.hide()
            self.trainerWidget.hide()
            self.trainingWidget.hide()
            self.__isClientWidgetVisible = False
            self.__isTrainerWidgetVisible = False
            self.__isTrainingWidgetVisible = False

        self.__isRelationsWidgetVisible = not self.__isRelationsWidgetVisible


#Создание и добавления карточек объектов
    def createClientCard(self, customer):
        clientCardWidget = QWidget()
        clientCardWidget.clientId = customer.getId()
        clientCardWidget.setStyleSheet("border: 2px solid black;")
        clientCardWidget.setFixedSize(333, 333)

        layout = QVBoxLayout()

        checkBox = QCheckBox()
        checkBox.setStyleSheet("""
            QCheckBox {
                border:none;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
            }
        """)

        clientCardWidget.checkbox = checkBox

        id_edit, id_input = self.create_labeled_input("id: ", str(customer.getId()))
        name_edit, name_input = self.create_labeled_input("Имя:", customer.getName())
        age_edit, age_input = self.create_labeled_input("Возраст:", str(customer.getAge()))
        visit_edit, visit_input = self.create_labeled_input("Время посещения (Месяцы):", str(customer.getVisitTime()))

        clientCardWidget.id_input = id_input
        clientCardWidget.name_input = name_input
        clientCardWidget.age_input = age_input
        clientCardWidget.visit_input = visit_input

        layout.addWidget(checkBox)
        layout.addWidget(id_edit)
        layout.addWidget(name_edit)
        layout.addWidget(age_edit)
        layout.addWidget(visit_edit)

        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        clientCardWidget.setLayout(layout)

        return clientCardWidget

    def add_client_card(self, card):
        if self.currentClientRow is None or self.currentClientRow.count() >= 3:
            self.currentClientRow = QHBoxLayout()
            self.scrollClientlayout.addLayout(self.currentClientRow)
            self.scrollClientlayout.addSpacing(44)

        self.currentClientRow.addWidget(card)


    def createTrainerCard(self, trainer):

        trainerCardWidget = QWidget()
        trainerCardWidget.trainerId = trainer.getId()
        trainerCardWidget.setStyleSheet("border: 2px solid black;")
        trainerCardWidget.setFixedSize(333, 333)

        layout = QVBoxLayout()

        checkBox = QCheckBox()
        checkBox.setStyleSheet("""
            QCheckBox {
                border:none;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
            }
        """)
        trainerCardWidget.checkbox = checkBox

        id_edit, id_input = self.create_labeled_input("id: ", str(trainer.getId()))
        name_edit, name_input = self.create_labeled_input("Имя:", trainer.getName())
        age_edit, age_input = self.create_labeled_input("Возраст:", str(trainer.getAge()))
        specialization_edit, specialization_input = self.create_labeled_input("Специализация:", trainer.getSpecialisation())
        experience_edit, experience_input = self.create_labeled_input("Опыт работы (Месяцы):", str(trainer.getExpirience()))

        trainerCardWidget.id_input = id_input
        trainerCardWidget.name_input = name_input
        trainerCardWidget.age_input = age_input
        trainerCardWidget.specialization_input = specialization_input
        trainerCardWidget.experience_input = experience_input

        layout.addWidget(checkBox)
        layout.addWidget(id_edit)
        layout.addWidget(name_edit)
        layout.addWidget(age_edit)
        layout.addWidget(specialization_edit)
        layout.addWidget(experience_edit)

        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        trainerCardWidget.setLayout(layout)

        return trainerCardWidget

    def add_trainer_card(self, card):
        if self.currentTrainerRow is None or self.currentTrainerRow.count() >= 3:
            self.currentTrainerRow = QHBoxLayout()
            self.scrollTrainerlayout.addLayout(self.currentTrainerRow)
            self.scrollTrainerlayout.addSpacing(44)

        self.currentTrainerRow.addWidget(card)


    def createTrainingCard(self, training):

        trainingCardWidget = QWidget()
        trainingCardWidget.trainingId = training.getId()
        trainingCardWidget.setStyleSheet("border: 2px solid black;")
        trainingCardWidget.setFixedSize(333, 333)

        layout = QVBoxLayout()

        checkBox = QCheckBox()
        checkBox.setStyleSheet("""
            QCheckBox {
                border:none;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
            }
        """)
        trainingCardWidget.checkbox = checkBox

        id_edit, id_input = self.create_labeled_input("id: ", str(training.getId()))
        client_edit, client_input = self.create_labeled_input("Клиент (ID):", str(training.getCustomer().getId()))
        trainer_edit, trainer_input = self.create_labeled_input("Тренер (ID):", str(training.getTrainer().getId()))
        time_edit, time_input = self.create_labeled_input("Время начала:", str(training.getTime()))
        duration_edit, duration_input = self.create_labeled_input("Продолжительность (Минуты):", str(training.getDuration()))

        trainingCardWidget.id_input = id_input
        trainingCardWidget.client_id_input = client_input
        trainingCardWidget.trainer_id_input = trainer_input
        trainingCardWidget.time_input = time_input
        trainingCardWidget.duration_input = duration_input

        layout.addWidget(checkBox)
        layout.addWidget(id_edit)
        layout.addWidget(client_edit)
        layout.addWidget(trainer_edit)
        layout.addWidget(time_edit)
        layout.addWidget(duration_edit)

        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        trainingCardWidget.setLayout(layout)

        return trainingCardWidget

    def add_training_card(self, card):
        if self.currentTrainingRow is None or self.currentTrainingRow.count() >= 3:
            self.currentTrainingRow = QHBoxLayout()
            self.scrollTraininglayout.addLayout(self.currentTrainingRow)
            self.scrollTraininglayout.addSpacing(44)

        self.currentTrainingRow.addWidget(card)

    def add_relations_card(self, card, column_number):
        if column_number == 1:
            self.column1.addWidget(card)
        elif column_number == 2:
            self.column2.addWidget(card)
        elif column_number == 3:
            self.column3.addWidget(card)

#Создание поля для ввода с названием слева
    def create_labeled_input(self, label_text, default_value):
        container = QWidget()
        container.setFixedSize(313, 56)
        container.setStyleSheet("margin: 5px;")
        layout = QHBoxLayout(container)

        label = QLabel(label_text)
        label.setStyleSheet("font-size: 14px; margin: 5px; margin-right: 0px; border: none;")
        label.setAlignment(Qt.AlignLeft)
        label.setAlignment(Qt.AlignVCenter)

        line_edit = QLineEdit(default_value)
        line_edit.setStyleSheet("height: 28px;")

        layout.addWidget(label)
        layout.addWidget(line_edit)

        return container, line_edit

#Очистка карточек с вкладок
    def clear_layout(self, layout):

        while layout.count():
            item = layout.takeAt(0)

            if item.layout():
                while item.layout().count():
                    widget = item.layout().takeAt(0).widget()
                    if widget:
                        widget.deleteLater()
                item.layout().deleteLater()

        self.currentClientRow = None
        self.currentTrainerRow = None
        self.currentTrainingRow = None
        layout.update()

# Очистка карточек со вкладки связей
    def clearRelationslayout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

#Создать карточки
    def renderClientCards(self):
        self.clear_layout(self.scrollClientlayout)
        for i in Customer.getList():
            self.add_client_card(self.createClientCard(i))

    def renderTrainerCards(self):
        self.clear_layout(self.scrollTrainerlayout)
        for i in Trainer.getList():
            self.add_trainer_card(self.createTrainerCard(i))

    def renderTrainingCards(self):
        self.clear_layout(self.scrollTraininglayout)

        for i in Training.getList():
            self.add_training_card(self.createTrainingCard(i))

    def renderRelationsCards(self):
        self.clearRelationslayout(self.column1)
        self.clearRelationslayout(self.column2)
        self.clearRelationslayout(self.column3)

        clients = Customer.getList()
        trainings = Training.getList()
        trainers = Trainer.getList()

        max_count = max(len(clients), len(trainings), len(trainers))

        for i in range(max_count):
            if i < len(clients):
                self.column1.addWidget(self.createClientCard(clients[i]))
            else:
                self.column1.addWidget(self.create_empty_card())

            if i < len(trainings):
                self.column2.addWidget(self.createTrainingCard(trainings[i]))
            else:
                self.column2.addWidget(self.create_empty_card())

            if i < len(trainers):
                self.column3.addWidget(self.createTrainerCard(trainers[i]))
            else:
                self.column3.addWidget(self.create_empty_card())
    def renderAllCards(self):
        self.renderClientCards()
        self.renderTrainerCards()
        self.renderTrainingCards()
        self.renderRelationsCards()

#Создание пустой карточки для более красивого отображения в последней вкладке
    def create_empty_card(self):
        card = QWidget()
        card.setFixedHeight(333)
        return card

#Добавить новую карточку объекта
    def addNewClient(self):
        Customer(Customer.getList()[-1].getId() + 1, "", 0, 0)
        self.renderAllCards()

    def addNewTrainer(self):
        Trainer(Trainer.getList()[-1].getId() + 1, "", 0, 0, "")
        self.renderAllCards()

    def addNewTraining(self):
        Training(Training.getList()[-1].getId() + 1, "", Customer.getCustomerById(Customer.getList()[-1].getId()),
                 Trainer.getTrainerById(Trainer.getList()[-1].getId()), 0)
        self.renderAllCards()

# Удалить карточку объекта
    def deleteClient(self):
        clients_to_delete = []

        for i in range(self.scrollClientlayout.count()):
            item = self.scrollClientlayout.itemAt(i)
            if item and item.layout():
                row_layout = item.layout()
                for j in range(row_layout.count()):
                    widget = row_layout.itemAt(j).widget()
                    if (widget and hasattr(widget, 'checkbox')
                            and hasattr(widget, 'clientId')
                            and widget.checkbox.isChecked()):
                        clients_to_delete.append(widget.clientId)

        if clients_to_delete:
            for client_id in clients_to_delete:
                try:
                    Customer.deleteCustomerByID(client_id)
                except Exception as e:
                    print(f"Ошибка удаления клиента {client_id}: {str(e)}")
            self.renderAllCards()

    def deleteTrainer(self):
        trainers_to_delete = []

        for i in range(self.scrollTrainerlayout.count()):
            item = self.scrollTrainerlayout.itemAt(i)
            if item and item.layout():
                row_layout = item.layout()
                for j in range(row_layout.count()):
                    widget = row_layout.itemAt(j).widget()
                    if (widget and hasattr(widget, 'checkbox')
                            and hasattr(widget, 'trainerId')
                            and widget.checkbox.isChecked()):
                        trainers_to_delete.append(widget.trainerId)

        if trainers_to_delete:
            for trainer_id in trainers_to_delete:
                try:
                    Trainer.deleteTrainerById(trainer_id)
                except Exception as e:
                    print(f"Ошибка удаления тренера {trainer_id}: {str(e)}")
            self.renderAllCards()

    def deleteTraining(self):
        trainings_to_delete = []

        for i in range(self.scrollTraininglayout.count()):
            item = self.scrollTraininglayout.itemAt(i)
            if item and item.layout():
                row_layout = item.layout()
                for j in range(row_layout.count()):
                    widget = row_layout.itemAt(j).widget()
                    if (widget and hasattr(widget, 'checkbox')
                            and hasattr(widget, 'trainingId')
                            and widget.checkbox.isChecked()):
                        trainings_to_delete.append(widget.trainingId)

        if trainings_to_delete:
            for training_id in trainings_to_delete:
                try:
                    Training.deleteTrainingById(training_id)
                except Exception as e:
                    print(f"Ошибка удаления тренировки {training_id}: {str(e)}")
            self.renderAllCards()

# Создать только связанные карточки
    def renderCardsInRelationByClient(self, clientId):
        self.clearRelationslayout(self.column1)
        self.clearRelationslayout(self.column2)
        self.clearRelationslayout(self.column3)

        client = Customer.getCustomerById(clientId)
        trainers = []
        trainings = []
        for i in Training.getList():
            if i.getCustomer()==client:
                trainings.append(i)
                trainers.append(i.getTrainer())

        max_count = max(1, len(trainings), len(trainers))

        for i in range(max_count):
            if i < 1:
                self.column1.addWidget(self.createClientCard(client))
            else:
                self.column1.addWidget(self.create_empty_card())

            if i < len(trainings):
                self.column2.addWidget(self.createTrainingCard(trainings[i]))
            else:
                self.column2.addWidget(self.create_empty_card())

            if i < len(trainers):
                self.column3.addWidget(self.createTrainerCard(trainers[i]))
            else:
                self.column3.addWidget(self.create_empty_card())
    def renderCardsInRelationByTrainer(self, trainerId):
        self.clearRelationslayout(self.column1)
        self.clearRelationslayout(self.column2)
        self.clearRelationslayout(self.column3)

        clients = []
        trainer = Trainer.getTrainerById(trainerId)
        trainings = []

        for i in Training.getList():
            if i.getTrainer()==trainer:
                trainings.append(i)
                clients.append(i.getCustomer())

        max_count = max(len(clients), len(trainings), 2)

        for i in range(max_count):

            if i < len(clients):
                self.column1.addWidget(self.createClientCard(clients[i]))
            else:
                self.column1.addWidget(self.create_empty_card())


            if i < len(trainings):
                self.column2.addWidget(self.createTrainingCard(trainings[i]))
            else:
                self.column2.addWidget(self.create_empty_card())

            if i < 1:
                self.column3.addWidget(self.createTrainerCard(trainer))
            else:
                self.column3.addWidget(self.create_empty_card())

    def renderCardsInRelationByTraining(self, trainingId):
        self.clearRelationslayout(self.column1)
        self.clearRelationslayout(self.column2)
        self.clearRelationslayout(self.column3)

        training = Training.getTrainingById(trainingId)
        client = training.getCustomer()
        trainer = training.getTrainer()

        max_count = 1

        for i in range(max_count):
            if i < 1:
                self.column1.addWidget(self.createClientCard(client))
            else:
                self.column1.addWidget(self.create_empty_card())

            if i < 1:
                self.column2.addWidget(self.createTrainingCard(training))
            else:
                self.column2.addWidget(self.create_empty_card())

            if i < 1:
                self.column3.addWidget(self.createTrainerCard(trainer))
            else:
                self.column3.addWidget(self.create_empty_card())

# Показать связанные карточки
    def showClientRelations(self):
        selected_cards = []
        for i in range(self.column1.count()):
            item = self.column1.itemAt(i)
            if item and item.widget():
                card = item.widget()
                if hasattr(card, 'checkbox') and card.checkbox.isChecked():
                    selected_cards.append(card)

        if len(selected_cards) == 1:
            self.renderCardsInRelationByClient(selected_cards[0].clientId)
            return selected_cards[0]
        elif len(selected_cards) > 1:
            self.show_warning_message()
            return None
        else:
            return None


    def showTrainerRelations(self):
        selected_cards = []
        for i in range(self.column3.count()):
            item = self.column3.itemAt(i)
            if item and item.widget():
                card = item.widget()
                if hasattr(card, 'checkbox') and card.checkbox.isChecked():
                    selected_cards.append(card)

        if len(selected_cards) == 1:
            self.renderCardsInRelationByTrainer(selected_cards[0].trainerId)
            return selected_cards[0]
        elif len(selected_cards) > 1:
            self.show_warning_message()
            return None
        else:
            return None


    def showTrainingRelations(self):
        selected_cards = []
        for i in range(self.column2.count()):
            item = self.column2.itemAt(i)
            if item and item.widget():
                card = item.widget()
                if hasattr(card, 'checkbox') and card.checkbox.isChecked():
                    selected_cards.append(card)

        if len(selected_cards) == 1:
            self.renderCardsInRelationByTraining(selected_cards[0].trainingId)
            return selected_cards[0]
        elif len(selected_cards) > 1:
            self.show_warning_message()
            return None
        else:
            return None

# Вывод ошибки, если карточек для связей было выбрано больше 1
    def show_warning_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Пожалуйста, выберите только одну карточку")
        msg.exec_()

# Изменениеи информмации об объекте
    def changeClient(self):
        for i in range(self.scrollClientlayout.count()):
            item = self.scrollClientlayout.itemAt(i)
            if item and item.layout():
                row_layout = item.layout()
                for j in range(row_layout.count()):
                    widget = row_layout.itemAt(j).widget()
                    if (widget and hasattr(widget, 'checkbox')
                            and hasattr(widget, 'clientId')
                            and widget.checkbox.isChecked()):
                        client = Customer.getCustomerById(widget.clientId)
                        client.setId(int(widget.id_input.text()))
                        client.setName(widget.name_input.text())
                        client.setAge(int(widget.age_input.text()))
                        client.setVisitTime(int(widget.visit_input.text()))

        self.renderAllCards()

    def changeTrainer(self):
        for i in range(self.scrollTrainerlayout.count()):
            item = self.scrollTrainerlayout.itemAt(i)
            if item and item.layout():
                row_layout = item.layout()
                for j in range(row_layout.count()):
                    widget = row_layout.itemAt(j).widget()
                    if (widget and hasattr(widget, 'checkbox')
                            and hasattr(widget, 'trainerId')
                            and widget.checkbox.isChecked()):
                        trainer = Trainer.getTrainerById(widget.trainerId)
                        trainer.setId(int(widget.id_input.text()))
                        trainer.setName(widget.name_input.text())
                        trainer.setAge(int(widget.age_input.text()))
                        trainer.setSpecialisation(widget.specialization_input.text())
                        trainer.setExpirience(int(widget.experience_input.text()))
        self.renderAllCards()

    def changeTraining(self):
        for i in range(self.scrollTraininglayout.count()):
            item = self.scrollTraininglayout.itemAt(i)
            if item and item.layout():
                row_layout = item.layout()
                for j in range(row_layout.count()):
                    widget = row_layout.itemAt(j).widget()
                    if (widget and hasattr(widget, 'checkbox')
                            and hasattr(widget, 'trainingId')
                            and widget.checkbox.isChecked()):
                        training = Training.getTrainingById(widget.trainingId)
                        training.setId(int(widget.id_input.text()))
                        training.setCustomer(Customer.getCustomerById(int(widget.client_id_input.text())))
                        training.setTrainer(Trainer.getTrainerById(int(widget.trainer_id_input.text())))
                        training.setTime(widget.time_input.text())
                        training.setDuration(int(widget.duration_input.text()))

        self.renderAllCards()