from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StudentView = QtWidgets.QPushButton(self.centralwidget)
        self.StudentView.setGeometry(QtCore.QRect(30, 30, 200, 40))
        self.StudentView.setObjectName("StudentView")
        self.EmployeeView = QtWidgets.QPushButton(self.centralwidget)
        self.EmployeeView.setGeometry(QtCore.QRect(270, 30, 200, 40))
        self.EmployeeView.setObjectName("EmployeeView")
        self.StudentPlus = QtWidgets.QPushButton(self.centralwidget)
        self.StudentPlus.setGeometry(QtCore.QRect(30, 110, 200, 40))
        self.StudentPlus.setObjectName("StudentPlus")
        self.EmployeePlus = QtWidgets.QPushButton(self.centralwidget)
        self.EmployeePlus.setGeometry(QtCore.QRect(270, 110, 200, 40))
        self.EmployeePlus.setObjectName("EmployeePlus")
        self.Updel = QtWidgets.QPushButton(self.centralwidget)
        self.Updel.setGeometry(QtCore.QRect(30, 190, 440, 40))
        self.Updel.setObjectName("Updel")
        self.School = QtWidgets.QPushButton(self.centralwidget)
        self.School.setGeometry(QtCore.QRect(30, 270, 440, 40))
        self.School.setObjectName("School")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(30, 350, 440, 40))
        self.Exit.setObjectName("Exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список учеников и работников учебного заведения"))
        self.StudentView.setText(_translate("MainWindow", "Просмотр списка учеников"))
        self.EmployeeView.setText(_translate("MainWindow", "Просмотр списка рабоников"))
        self.StudentPlus.setText(_translate("MainWindow", "Добавление ученика"))
        self.EmployeePlus.setText(_translate("MainWindow", "Добавление работника"))
        self.Updel.setText(_translate("MainWindow", "Изменение или удаление данных о ученике или работнике"))
        self.School.setText(_translate("MainWindow", "Сведения об учебной организации"))
        self.Exit.setText(_translate("MainWindow", "Выход"))


class StudentView(object):
    def setupUi(self, StudentView):
        StudentView.setObjectName("StudentView")
        StudentView.resize(1000, 500)
        self.centralwidget = QtWidgets.QWidget(StudentView)
        self.centralwidget.setObjectName("centralwidget")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(30, 410, 940, 40))
        self.Back.setObjectName("Back")
        self.Tablitsa = QtWidgets.QTableWidget(self.centralwidget)
        self.Tablitsa.setGeometry(QtCore.QRect(30, 30, 940, 340))
        self.Tablitsa.setObjectName("Tablitsa")
        self.Tablitsa.setColumnCount(0)
        self.Tablitsa.setRowCount(0)
        StudentView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StudentView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        StudentView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StudentView)
        self.statusbar.setObjectName("statusbar")
        StudentView.setStatusBar(self.statusbar)

        self.retranslateUi(StudentView)
        QtCore.QMetaObject.connectSlotsByName(StudentView)

    def retranslateUi(self, StudentView):
        _translate = QtCore.QCoreApplication.translate
        StudentView.setWindowTitle(_translate("StudentView", "Просмотр списка учеников"))
        self.Back.setText(_translate("StudentView", "Назад"))


class EmployeeView(object):
    def setupUi(self, EmployeeView):
        EmployeeView.setObjectName("StudentView")
        EmployeeView.resize(1000, 500)
        self.centralwidget = QtWidgets.QWidget(EmployeeView)
        self.centralwidget.setObjectName("centralwidget")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(30, 410, 940, 40))
        self.Back.setObjectName("Back")
        self.Tablitsa = QtWidgets.QTableWidget(self.centralwidget)
        self.Tablitsa.setGeometry(QtCore.QRect(30, 30, 940, 340))
        self.Tablitsa.setObjectName("Tablitsa")
        self.Tablitsa.setColumnCount(0)
        self.Tablitsa.setRowCount(0)
        EmployeeView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EmployeeView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        EmployeeView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EmployeeView)
        self.statusbar.setObjectName("statusbar")
        EmployeeView.setStatusBar(self.statusbar)

        self.retranslateUi(EmployeeView)
        QtCore.QMetaObject.connectSlotsByName(EmployeeView)

    def retranslateUi(self, EmployeeView):
        _translate = QtCore.QCoreApplication.translate
        EmployeeView.setWindowTitle(_translate("StudentView", "Просмотр списка учеников"))
        self.Back.setText(_translate("StudentView", "Назад"))


class StudentPlus(object):
    def setupUi(self, StudentPlus):
        StudentPlus.setObjectName("StudentPlus")
        StudentPlus.resize(500, 550)
        self.centralwidget = QtWidgets.QWidget(StudentPlus)
        self.centralwidget.setObjectName("centralwidget")
        self.Update = QtWidgets.QPushButton(self.centralwidget)
        self.Update.setGeometry(QtCore.QRect(30, 390, 440, 40))
        self.Update.setObjectName("Update")
        self.SClasses = QtWidgets.QComboBox(self.centralwidget)
        self.SClasses.setGeometry(QtCore.QRect(30, 250, 440, 40))
        self.SClasses.setObjectName("SCLasses")
        self.TName = QtWidgets.QLineEdit(self.centralwidget)
        self.TName.setGeometry(QtCore.QRect(30, 50, 440, 40))
        self.TName.setObjectName("TName")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(30, 30, 440, 20))
        self.Name.setObjectName("Name")
        self.Year = QtWidgets.QLabel(self.centralwidget)
        self.Year.setGeometry(QtCore.QRect(30, 130, 440, 20))
        self.Year.setObjectName("Year")
        self.Classes = QtWidgets.QLabel(self.centralwidget)
        self.Classes.setGeometry(QtCore.QRect(30, 230, 440, 20))
        self.Classes.setObjectName("Classes")
        self.TYear = QtWidgets.QLineEdit(self.centralwidget)
        self.TYear.setGeometry(QtCore.QRect(30, 150, 440, 40))
        self.TYear.setObjectName("TYear")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(30, 450, 440, 40))
        self.Back.setObjectName("Back")
        StudentPlus.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StudentPlus)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        StudentPlus.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StudentPlus)
        self.statusbar.setObjectName("statusbar")
        StudentPlus.setStatusBar(self.statusbar)

        self.retranslateUi(StudentPlus)
        QtCore.QMetaObject.connectSlotsByName(StudentPlus)

    def retranslateUi(self, StudentPlus):
        _translate = QtCore.QCoreApplication.translate
        StudentPlus.setWindowTitle(_translate("StudentPlus", "Добавление учеников"))
        self.Update.setText(_translate("StudentPlus", "Внести нового ученика в таблицу"))
        self.Name.setText(_translate("StudentPlus", "ФИО:"))
        self.Year.setText(_translate("StudentPlus", "Год начала обучения:"))
        self.Classes.setText(_translate("StudentPlus", "Класс обучения:"))
        self.Back.setText(_translate("StudentPlus", "Назад"))


class EmployeePlus(object):
    def setupUi(self, EmployeePlus):
        EmployeePlus.setObjectName("StudentPlus")
        EmployeePlus.resize(500, 550)
        self.centralwidget = QtWidgets.QWidget(EmployeePlus)
        self.centralwidget.setObjectName("centralwidget")
        self.Update = QtWidgets.QPushButton(self.centralwidget)
        self.Update.setGeometry(QtCore.QRect(30, 390, 440, 40))
        self.Update.setObjectName("Update")
        self.SRoles = QtWidgets.QComboBox(self.centralwidget)
        self.SRoles.setGeometry(QtCore.QRect(30, 250, 440, 40))
        self.SRoles.setObjectName("SCLasses")
        self.TName = QtWidgets.QLineEdit(self.centralwidget)
        self.TName.setGeometry(QtCore.QRect(30, 50, 440, 40))
        self.TName.setObjectName("TName")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(30, 30, 440, 20))
        self.Name.setObjectName("Name")
        self.Year = QtWidgets.QLabel(self.centralwidget)
        self.Year.setGeometry(QtCore.QRect(30, 130, 440, 20))
        self.Year.setObjectName("Year")
        self.Classes = QtWidgets.QLabel(self.centralwidget)
        self.Classes.setGeometry(QtCore.QRect(30, 230, 440, 20))
        self.Classes.setObjectName("Classes")
        self.TYear = QtWidgets.QLineEdit(self.centralwidget)
        self.TYear.setGeometry(QtCore.QRect(30, 150, 440, 40))
        self.TYear.setObjectName("TYear")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(30, 450, 440, 40))
        self.Back.setObjectName("Back")
        EmployeePlus.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EmployeePlus)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        EmployeePlus.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EmployeePlus)
        self.statusbar.setObjectName("statusbar")
        EmployeePlus.setStatusBar(self.statusbar)

        self.retranslateUi(EmployeePlus)
        QtCore.QMetaObject.connectSlotsByName(EmployeePlus)

    def retranslateUi(self, EmployeePlus):
        _translate = QtCore.QCoreApplication.translate
        EmployeePlus.setWindowTitle(_translate("StudentPlus", "Добавление работника"))
        self.Update.setText(_translate("StudentPlus", "Внести нового работника в таблицу"))
        self.Name.setText(_translate("StudentPlus", "ФИО:"))
        self.Year.setText(_translate("StudentPlus", "Год поступления на работу:"))
        self.Classes.setText(_translate("StudentPlus", "Профессия"))
        self.Back.setText(_translate("StudentPlus", "Назад"))


class UpDel(object):
    def setupUi(self, UpDel):
        UpDel.setObjectName("UpDel")
        UpDel.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(UpDel)
        self.centralwidget.setObjectName("centralwidget")
        self.SSet = QtWidgets.QComboBox(self.centralwidget)
        self.SSet.setGeometry(QtCore.QRect(270, 50, 200, 40))
        self.SSet.setObjectName("SSet")
        self.TSet = QtWidgets.QLineEdit(self.centralwidget)
        self.TSet.setGeometry(QtCore.QRect(30, 50, 200, 40))
        self.TSet.setObjectName("TSet")
        self.Set = QtWidgets.QLabel(self.centralwidget)
        self.Set.setGeometry(QtCore.QRect(30, 30, 440, 20))
        self.Set.setObjectName("Set")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(30, 110, 200, 20))
        self.Name.setObjectName("Name")
        self.Role = QtWidgets.QLabel(self.centralwidget)
        self.Role.setGeometry(QtCore.QRect(30, 270, 200, 20))
        self.Role.setObjectName("Role")
        self.Year = QtWidgets.QLabel(self.centralwidget)
        self.Year.setGeometry(QtCore.QRect(30, 190, 200, 20))
        self.Year.setObjectName("Year")
        self.TName = QtWidgets.QLineEdit(self.centralwidget)
        self.TName.setGeometry(QtCore.QRect(30, 130, 200, 40))
        self.TName.setObjectName("TName")
        self.TYear = QtWidgets.QLineEdit(self.centralwidget)
        self.TYear.setGeometry(QtCore.QRect(30, 210, 200, 40))
        self.TYear.setObjectName("TYear")
        self.SRole = QtWidgets.QComboBox(self.centralwidget)
        self.SRole.setGeometry(QtCore.QRect(30, 290, 200, 40))
        self.SRole.setObjectName("SRole")
        self.SClass = QtWidgets.QComboBox(self.centralwidget)
        self.SClass.setGeometry(QtCore.QRect(30, 370, 200, 40))
        self.SClass.setObjectName("SClass")
        self.Class = QtWidgets.QLabel(self.centralwidget)
        self.Class.setGeometry(QtCore.QRect(30, 350, 200, 20))
        self.Class.setObjectName("Class")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(270, 370, 200, 40))
        self.Back.setObjectName("Back")
        self.Update = QtWidgets.QPushButton(self.centralwidget)
        self.Update.setGeometry(QtCore.QRect(270, 130, 200, 70))
        self.Update.setObjectName("Update")
        self.Delete = QtWidgets.QPushButton(self.centralwidget)
        self.Delete.setGeometry(QtCore.QRect(270, 240, 200, 70))
        self.Delete.setObjectName("Delete")
        UpDel.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UpDel)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        UpDel.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UpDel)
        self.statusbar.setObjectName("statusbar")
        UpDel.setStatusBar(self.statusbar)

        self.retranslateUi(UpDel)
        QtCore.QMetaObject.connectSlotsByName(UpDel)

    def retranslateUi(self, UpDel):
        _translate = QtCore.QCoreApplication.translate
        UpDel.setWindowTitle(_translate("UpDel", "Изменение или удаление данных"))
        self.Set.setText(_translate("UpDel", "Выбор ученика или работника учебного заведения"))
        self.Name.setText(_translate("UpDel", "Поменять имя:"))
        self.Role.setText(_translate("UpDel", "Поменять роль:"))
        self.Year.setText(_translate("UpDel", "Поменять год:"))
        self.Class.setText(_translate("UpDel", "Поменять класс:"))
        self.Back.setText(_translate("UpDel", "Назад"))
        self.Update.setText(_translate("UpDel", "Изменить"))
        self.Delete.setText(_translate("UpDel", "Удалить"))


class School(object):
    def setupUi(self, School):
        School.setObjectName("School")
        School.resize(500, 391)
        self.centralwidget = QtWidgets.QWidget(School)
        self.centralwidget.setObjectName("centralwidget")
        self.TextRofl = QtWidgets.QLabel(self.centralwidget)
        self.TextRofl.setGeometry(QtCore.QRect(30, 30, 440, 250))
        self.TextRofl.setObjectName("TextRofl")
        self.Back = QtWidgets.QPushButton(self.centralwidget)
        self.Back.setGeometry(QtCore.QRect(30, 300, 440, 40))
        self.Back.setObjectName("Back")
        School.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(School)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        School.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(School)
        self.statusbar.setObjectName("statusbar")
        School.setStatusBar(self.statusbar)

        self.retranslateUi(School)
        QtCore.QMetaObject.connectSlotsByName(School)

    def retranslateUi(self, School):
        _translate = QtCore.QCoreApplication.translate
        School.setWindowTitle(_translate("School", "Об образовательной организации"))
        self.TextRofl.setText(_translate("School",
                                         "<html><head/><body><p>Так как я не являюсь никакой школой, то просто буду писать здесь</p><p>интересные вещи. Я люблю спать и кушать, это мое основное </p><p>времяпровождение.</p><p>Так как с 28 октября начался локдаун, то я буду спать и </p><p>кушать в два раза больше.</p><p>Спать и кушать - невероятно интересно.</p><p><span style=\" font-weight:600;\">Жаль, что нельзя спать и кушать одновременно</span></p></body></html>"))
        self.Back.setText(_translate("School", "Назад"))
