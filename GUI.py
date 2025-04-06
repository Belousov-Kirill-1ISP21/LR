from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QFrame, QScrollArea, QCheckBox, \
    QGridLayout
from PyQt5.QtCore import Qt


class GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()

        self.__isClientWidgetVisible = False
        self.__isTrainerWidgetVisible = False
        self.__isTrainingWidgetVisible = False
        self.__isRelationsWidgetVisible = False

        self.clientWidget = QWidget()
        self.trainerWidget = QWidget()
        self.trainingWidget = QWidget()
        self.relationsWidget = QWidget()

        self.currentClientRow = None
        self.scrollClientlayout = QVBoxLayout()

        self.currentTrainerRow = None
        self.scrollTrainerlayout = QVBoxLayout()

        self.currentTrainingRow = None
        self.scrollTraininglayout = QVBoxLayout()

        self.column1 = QVBoxLayout()
        self.column2 = QVBoxLayout()
        self.column3 = QVBoxLayout()


        self.setFixedSize(1222, 777)


        self.сreateMainWindow()

        self.сreateClientWindow()
        self.сreateTrainerWindow()
        self.сreateTrainingWindow()
        self.сreateRelationsWindow()

        self.setLayout(self.main_layout)


    def сreateMainWindow(self):
        # Основной вертикальный layout

        self.main_layout.setAlignment(Qt.AlignTop)

        # Установка отступов для основного layout
        self.main_layout.setContentsMargins(10, 10, 10, 10)  # Отступы: левый, верхний, правый, нижний

        self.main_layout.addSpacing(24)

        # Заголовок по центру
        title_label = QLabel('Программа для администрирования спортзала')
        title_label.setAlignment(Qt.AlignCenter)  # Выравнивание по центру
        title_label.setStyleSheet("font-size: 16px;")
        self.main_layout.addWidget(title_label)

        # Добавление вертикального отступа между заголовком и кнопками
        self.main_layout.addSpacing(24)  # Добавляет пространство (10 пикселей) между заголовком и кнопками

        # Горизонтальный layout для кнопок
        button_layout = QHBoxLayout()

        # Создание 4 кнопок (QPushButton) с жирными стрелками
        clientButton = QPushButton("Управление клиентами ↓")
        trainerButton = QPushButton("Управление тренерами ↓")
        trainingButton = QPushButton("Управление тренировками ↓")
        relationsButton = QPushButton("Посмотреть связи ↓")

        # Подключение кнопок к функции отображения/скрытия прямоугольника
        clientButton.clicked.connect(lambda: self.showHideClient())
        trainerButton.clicked.connect(lambda: self.showHideTrainer())
        trainingButton.clicked.connect(lambda: self.showHideTraining())
        relationsButton.clicked.connect(lambda: self.showHideRelations())

        for button in [clientButton, trainerButton, trainingButton, relationsButton]:
            button.setStyleSheet("font-size: 16px; padding: 10px 20px;")  # Увеличиваем шрифт и внутренние отступы

        button_layout.addWidget(clientButton)
        button_layout.addWidget(trainerButton)
        button_layout.addWidget(trainingButton)
        button_layout.addWidget(relationsButton)

        # Добавление горизонтального layout с кнопками в основной layout
        self.main_layout.addLayout(button_layout)

        self.main_layout.addSpacing(24)

    def сreateClientWindow(self):
        self.clientWidget = QWidget()

        clientLayout = QVBoxLayout()

        rectangle_frame = QWidget()
        rectangle_frame.setStyleSheet("border: 2px solid black;")  # Стиль прямоугольника
        rectangle_frame.setFixedSize(1192, 444)  # Фиксированный размер

        # Создание layout для прямоугольника и добавление метки
        rectangle_layout = QVBoxLayout()

        rectangle_label = QLabel("Клиенты")
        rectangle_label.setAlignment(Qt.AlignTop)
        rectangle_label.setAlignment(Qt.AlignHCenter)
        rectangle_label.setStyleSheet("font-size: 18px; font-weight: bold; border: none;")

        scroll_area = QScrollArea()
        scroll_area.setStyleSheet("border: none;")
        scroll_area.setWidgetResizable(True)  # Виджет будет масштабироваться
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # Создаем контейнер (QFrame), который будет прокручиваться
        scroll_content = QFrame()
        self.scrollClientlayout = QVBoxLayout(scroll_content)

        scroll_area.setWidget(scroll_content)

        rectangle_layout.addSpacing(22)
        rectangle_layout.addWidget(rectangle_label)
        rectangle_layout.addWidget(scroll_area)

        self.scrollClientlayout.addSpacing(10)
        self.add_client_card(self.createClientCard())
        self.add_client_card(self.createClientCard())
        self.add_client_card(self.createClientCard())
        self.add_client_card(self.createClientCard())
        self.add_client_card(self.createClientCard())
        self.scrollClientlayout.addSpacing(44)

        # Установка layout в прямоугольник
        rectangle_frame.setLayout(rectangle_layout)

        # Добавление прямоугольника в основной layout
        clientLayout.addWidget(rectangle_frame)

        clientLayout.addSpacing(44)

        bottomButtonLayout = QHBoxLayout()
        firstBotButton = QPushButton("Добавить клиента")
        secondBotButton = QPushButton("Удалить клиента")
        firstBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        secondBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        bottomButtonLayout.addWidget(firstBotButton)
        bottomButtonLayout.addSpacing(444)
        bottomButtonLayout.addWidget(secondBotButton)

        clientLayout.addLayout(bottomButtonLayout)

        self.clientWidget.setLayout(clientLayout)
        self.clientWidget.hide()

        self.main_layout.addWidget(self.clientWidget)

    def сreateTrainerWindow(self):
        self.trainerWidget = QWidget()

        trainerLayout = QVBoxLayout()

        rectangle_frame = QFrame()
        rectangle_frame.setStyleSheet(
            "border: 2px solid black;")  # Стиль прямоугольника
        rectangle_frame.setFixedSize(1192, 444)  # Фиксированный размер

        # Создание layout для прямоугольника и добавление метки
        rectangle_layout = QVBoxLayout()

        rectangle_label = QLabel("Тренера")
        rectangle_label.setAlignment(Qt.AlignTop)
        rectangle_label.setAlignment(Qt.AlignHCenter)
        rectangle_label.setStyleSheet("font-size: 18px; font-weight: bold; border: none;")

        scroll_area = QScrollArea()
        scroll_area.setStyleSheet("border: none;")
        scroll_area.setWidgetResizable(True)  # Виджет будет масштабироваться
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # Создаем контейнер (QFrame), который будет прокручиваться
        scroll_content = QFrame()
        self.scrollTrainerlayout = QVBoxLayout(scroll_content)

        scroll_area.setWidget(scroll_content)

        rectangle_layout.addSpacing(22)
        rectangle_layout.addWidget(rectangle_label)
        rectangle_layout.addWidget(scroll_area)

        self.scrollTrainerlayout.addSpacing(10)
        self.add_trainer_card(self.createTrainerCard())
        self.add_trainer_card(self.createTrainerCard())
        self.add_trainer_card(self.createTrainerCard())
        self.scrollTrainerlayout.addSpacing(44)

        # Установка layout в прямоугольник
        rectangle_frame.setLayout(rectangle_layout)

        # Добавление прямоугольника в основной layout
        trainerLayout.addWidget(rectangle_frame)

        trainerLayout.addSpacing(44)

        bottomButtonLayout = QHBoxLayout()
        firstBotButton = QPushButton("Добавить тренера")
        secondBotButton = QPushButton("Удалить тренера")
        firstBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        secondBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        bottomButtonLayout.addWidget(firstBotButton)
        bottomButtonLayout.addSpacing(444)
        bottomButtonLayout.addWidget(secondBotButton)

        trainerLayout.addLayout(bottomButtonLayout)

        self.trainerWidget.setLayout(trainerLayout)
        self.trainerWidget.hide()

        self.main_layout.addWidget(self.trainerWidget)
    def сreateTrainingWindow(self):
        self.trainingWidget = QWidget()

        trainingLayout = QVBoxLayout()

        rectangle_frame = QFrame()
        rectangle_frame.setStyleSheet(
            "border: 2px solid black;")  # Стиль прямоугольника
        rectangle_frame.setFixedSize(1192, 444)  # Фиксированный размер

        # Создание layout для прямоугольника и добавление метки
        rectangle_layout = QVBoxLayout()

        rectangle_label = QLabel("Тренировки")
        rectangle_label.setAlignment(Qt.AlignTop)
        rectangle_label.setAlignment(Qt.AlignHCenter)
        rectangle_label.setStyleSheet("font-size: 18px; font-weight: bold; border: none;")

        scroll_area = QScrollArea()
        scroll_area.setStyleSheet("border: none;")
        scroll_area.setWidgetResizable(True)  # Виджет будет масштабироваться
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # Создаем контейнер (QFrame), который будет прокручиваться
        scroll_content = QFrame()
        self.scrollTraininglayout = QVBoxLayout(scroll_content)

        scroll_area.setWidget(scroll_content)

        rectangle_layout.addSpacing(22)
        rectangle_layout.addWidget(rectangle_label)
        rectangle_layout.addWidget(scroll_area)

        self.scrollTraininglayout.addSpacing(10)
        self.add_training_card(self.createTrainingCard())
        self.add_training_card(self.createTrainingCard())
        self.add_training_card(self.createTrainingCard())
        self.add_training_card(self.createTrainingCard())
        self.add_training_card(self.createTrainingCard())
        self.add_training_card(self.createTrainingCard())
        self.add_training_card(self.createTrainingCard())
        self.scrollTraininglayout.addSpacing(44)

        # Установка layout в прямоугольник
        rectangle_frame.setLayout(rectangle_layout)

        # Добавление прямоугольника в основной layout
        trainingLayout.addWidget(rectangle_frame)

        trainingLayout.addSpacing(44)

        bottomButtonLayout = QHBoxLayout()
        firstBotButton = QPushButton("Добавить тренировку")
        secondBotButton = QPushButton("Удалить тренировку")
        firstBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        secondBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        bottomButtonLayout.addWidget(firstBotButton)
        bottomButtonLayout.addSpacing(444)
        bottomButtonLayout.addWidget(secondBotButton)

        trainingLayout.addLayout(bottomButtonLayout)

        self.trainingWidget.setLayout(trainingLayout)
        self.trainingWidget.hide()

        self.main_layout.addWidget(self.trainingWidget)
    def сreateRelationsWindow(self):
        self.relationsWidget = QWidget()

        relationsLayout = QVBoxLayout()

        rectangle_frame = QFrame()
        rectangle_frame.setStyleSheet("border: 2px solid black;")  # Стиль прямоугольника
        rectangle_frame.setFixedSize(1192, 444)  # Фиксированный размер

        # Создание layout для прямоугольника и добавление метки
        rectangle_layout = QVBoxLayout()

        header_widget = QWidget()
        header_widget.setStyleSheet("border: none;")
        header_layout = QHBoxLayout(header_widget)
        header_layout.setContentsMargins(10, 22, 10, 10)  # Отступы: слева, сверху, справа, снизу
        header_layout.setSpacing(20)  # Расстояние между столбцами

        # 2. Создаем и настраиваем заголовки
        titles = ["Клиенты", "Тренировки", "Тренера"]
        for title in titles:
            header_label = QLabel(title)
            header_label.setAlignment(Qt.AlignCenter)
            header_label.setStyleSheet("font-size: 18px; font-weight: bold; border: none;")
            header_layout.addWidget(header_label)

        scroll_area = QScrollArea()
        scroll_area.setStyleSheet("border: none;")
        scroll_area.setWidgetResizable(True)  # Виджет будет масштабироваться
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # Создаем контейнер (QFrame), который будет прокручиваться
        scroll_content = QFrame()
        scroll_layout = QHBoxLayout(scroll_content)  # Основной горизонтальный layout

        # Создаем 3 вертикальных столбца
        self.column1 = QVBoxLayout()
        self.column2 = QVBoxLayout()
        self.column3 = QVBoxLayout()

        # Настраиваем отступы и расстояние между столбцами
        for column in [self.column1, self.column2, self.column3]:
            column.setSpacing(44)  # Расстояние между карточками в столбце
            column.setContentsMargins(5, 5, 44, 5)
            scroll_layout.addLayout(column)

        # Добавляем растягивающийся элемент для выравнивания
        self.column3.addStretch()

        scroll_area.setWidget(scroll_content)

        rectangle_layout.addWidget(header_widget)
        rectangle_layout.addWidget(scroll_area)

        self.add_relations_card(self.createClientCard(), 1)
        self.add_relations_card(self.createClientCard(), 1)
        self.add_relations_card(self.createTrainingCard(), 2)
        self.add_relations_card(self.createTrainingCard(), 2)
        self.add_relations_card(self.createTrainerCard(), 3)
        self.add_relations_card(self.createTrainerCard(), 3)
        scroll_layout.addSpacing(44)

        # Установка layout в прямоугольник
        rectangle_frame.setLayout(rectangle_layout)

        # Добавление прямоугольника в основной layout
        relationsLayout.addWidget(rectangle_frame)

        relationsLayout.addSpacing(44)

        bottomButtonLayout = QHBoxLayout()
        firstBotButton = QPushButton("Посмотреть связи клиента")
        secondBotButton = QPushButton("Посмотреть связи тренировки")
        thirdBotButton = QPushButton("Посмотреть связи тренера")
        firstBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        secondBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        thirdBotButton.setStyleSheet("font-size: 16px; padding: 10px 20px;")
        bottomButtonLayout.addWidget(firstBotButton)
        bottomButtonLayout.addSpacing(111)
        bottomButtonLayout.addWidget(secondBotButton)
        bottomButtonLayout.addSpacing(111)
        bottomButtonLayout.addWidget(thirdBotButton)

        relationsLayout.addLayout(bottomButtonLayout)

        self.relationsWidget.setLayout(relationsLayout)
        self.relationsWidget.hide()

        self.main_layout.addWidget(self.relationsWidget)


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
            self.clientWidget.hide()
            self.trainerWidget.hide()
            self.trainingWidget.hide()
            self.__isClientWidgetVisible = False
            self.__isTrainerWidgetVisible = False
            self.__isTrainingWidgetVisible = False

        self.__isRelationsWidgetVisible = not self.__isRelationsWidgetVisible



    def createClientCard(self):

        clientCardWidget = QWidget()
        clientCardWidget.setStyleSheet("border: 2px solid black;")
        clientCardWidget.setFixedSize(333, 333)

        # Создаем вертикальный layout
        layout = QVBoxLayout()

        # Создаем метки с информацией
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
        id_label = QLabel("id: 0")
        name_label = QLabel("Имя: Александр Владимирович")
        age_label = QLabel("Возраст: 30 лет")
        visit_label = QLabel("Время посещения: 2 месяца")

        # Устанавливаем выравнивание текста в метках
        for label in [id_label, name_label, age_label, visit_label]:
            label.setAlignment(Qt.AlignLeft)
            label.setStyleSheet("font-size: 14px; margin: 5px;")
            label.setAlignment(Qt.AlignVCenter)

        # Добавляем метки в layout
        layout.addWidget(checkBox)
        layout.addWidget(id_label)
        layout.addWidget(name_label)
        layout.addWidget(age_label)
        layout.addWidget(visit_label)

        # Устанавливаем отступы и spacing
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        # Устанавливаем layout для виджета
        clientCardWidget.setLayout(layout)

        return clientCardWidget

    def add_client_card(self, card):
        # Если нет текущей строки или в ней уже 3 карточки → создаем новую строку
        if self.currentClientRow is None or self.currentClientRow.count() >= 3:
            self.currentClientRow = QHBoxLayout()
            self.scrollClientlayout.addLayout(self.currentClientRow)
            self.scrollClientlayout.addSpacing(44)  # Отступ между строками

        # Добавляем карточку в текущую строку
        self.currentClientRow.addWidget(card)


    def createTrainerCard(self):

        clientCardWidget = QWidget()
        clientCardWidget.setStyleSheet("border: 2px solid black;")
        clientCardWidget.setFixedSize(333, 333)

        # Создаем вертикальный layout
        layout = QVBoxLayout()

        # Создаем метки с информацией
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
        id_label = QLabel("id: 0")
        name_label = QLabel("Имя: Александр Владимирович")
        age_label = QLabel("Возраст: 30 лет")
        specialization_label = QLabel("Специализация: силовые тренировки")
        experience_label = QLabel("Опыт работы: 1 год")

        # Устанавливаем выравнивание текста в метках
        for label in [id_label, name_label, age_label, specialization_label, experience_label]:
            label.setAlignment(Qt.AlignLeft)
            label.setStyleSheet("font-size: 14px; margin: 5px;")

        # Добавляем метки в layout
        layout.addWidget(checkBox)
        layout.addWidget(id_label)
        layout.addWidget(name_label)
        layout.addWidget(age_label)
        layout.addWidget(specialization_label)
        layout.addWidget(experience_label)

        # Устанавливаем отступы и spacing
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        # Устанавливаем layout для виджета
        clientCardWidget.setLayout(layout)

        return clientCardWidget

    def add_trainer_card(self, card):
        # Если нет текущей строки или в ней уже 3 карточки → создаем новую строку
        if self.currentTrainerRow is None or self.currentTrainerRow.count() >= 3:
            self.currentTrainerRow = QHBoxLayout()
            self.scrollTrainerlayout.addLayout(self.currentTrainerRow)
            self.scrollTrainerlayout.addSpacing(44)  # Отступ между строками

        # Добавляем карточку в текущую строку
        self.currentTrainerRow.addWidget(card)


    def createTrainingCard(self):

        clientCardWidget = QWidget()
        clientCardWidget.setStyleSheet("border: 2px solid black;")
        clientCardWidget.setFixedSize(333, 333)

        # Создаем вертикальный layout
        layout = QVBoxLayout()

        # Создаем метки с информацией
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
        id_label = QLabel("id: 0")
        client_label = QLabel("Клиент: Александр Владимирович")
        trainer_label = QLabel("Тренер: Александр Владимирович")
        time_label = QLabel("Время начала: 14:14")
        duration_label = QLabel("Продолжительность: 90 минут")

        # Устанавливаем выравнивание текста в метках
        for label in [id_label, client_label, trainer_label, time_label, duration_label]:
            label.setAlignment(Qt.AlignLeft)
            label.setStyleSheet("font-size: 14px; margin: 5px;")

        # Добавляем метки в layout
        layout.addWidget(checkBox)
        layout.addWidget(id_label)
        layout.addWidget(client_label)
        layout.addWidget(trainer_label)
        layout.addWidget(time_label)
        layout.addWidget(duration_label)

        # Устанавливаем отступы и spacing
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)

        # Устанавливаем layout для виджета
        clientCardWidget.setLayout(layout)

        return clientCardWidget

    def add_training_card(self, card):
        # Если нет текущей строки или в ней уже 3 карточки → создаем новую строку
        if self.currentTrainingRow is None or self.currentTrainingRow.count() >= 3:
            self.currentTrainingRow = QHBoxLayout()
            self.scrollTraininglayout.addLayout(self.currentTrainingRow)
            self.scrollTraininglayout.addSpacing(44)  # Отступ между строками

        # Добавляем карточку в текущую строку
        self.currentTrainingRow.addWidget(card)

    def add_relations_card(self, card, column_number):
        """Добавляет карточку в указанный столбец (1, 2 или 3)"""
        if column_number == 1:
            self.column1.addWidget(card)
        elif column_number == 2:
            self.column2.addWidget(card)
        elif column_number == 3:
            self.column3.insertWidget(self.column3.count() - 1, card)  # Добавляем перед stretch

