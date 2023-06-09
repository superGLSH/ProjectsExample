import sys, sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from Windows import MainWindow, StudentView, EmployeeView, StudentPlus, EmployeePlus, UpDel, School

app = QtWidgets.QApplication(sys.argv)
mw = QtWidgets.QMainWindow()
ui = MainWindow()
ui.setupUi(mw)
mw.show()


def move(a, b):
    a.close()
    b.show()


def gotosv():
    global sv, mw
    sv = QtWidgets.QMainWindow()
    ui = StudentView()
    ui.setupUi(sv)
    move(mw, sv)

    def select_data(a):
        res = a.cursor().execute("""SELECT Name, Class, Year FROM Persons WHERE Role='Ученик'""").fetchall()
        ui.Tablitsa.setColumnCount(3)
        ui.Tablitsa.setRowCount(0)
        for i, row in enumerate(res):
            ui.Tablitsa.setRowCount(
                ui.Tablitsa.rowCount() + 1)
            for j, elem in enumerate(row):
                ui.Tablitsa.setItem(
                    i, j, QtWidgets.QTableWidgetItem(str(elem)))

    connection = sqlite3.connect("School.db")
    select_data(connection)
    ui.Back.clicked.connect(lambda x: move(sv, mw))


def gotoev():
    global ev
    ev = QtWidgets.QMainWindow()
    ui = EmployeeView()
    ui.setupUi(ev)
    move(mw, ev)

    def select_data(a):
        res = a.cursor().execute("""SELECT Name, Role, Year FROM Persons WHERE Role!='Ученик'""").fetchall()
        ui.Tablitsa.setColumnCount(3)
        ui.Tablitsa.setRowCount(0)
        for i, row in enumerate(res):
            ui.Tablitsa.setRowCount(
                ui.Tablitsa.rowCount() + 1)
            for j, elem in enumerate(row):
                ui.Tablitsa.setItem(
                    i, j, QtWidgets.QTableWidgetItem(str(elem)))

    connection = sqlite3.connect("School.db")
    select_data(connection)
    ui.Back.clicked.connect(lambda x: move(ev, mw))


def gotosp():
    global sp, mw
    sp = QtWidgets.QMainWindow()
    ui = StudentPlus()
    ui.setupUi(sp)
    move(mw, sp)
    ui.SClasses.addItem('')

    def data(a):
        res = a.cursor().execute("""SELECT Class FROM Classes WHERE Class !='-'""").fetchall()
        for i in res:
            ui.SClasses.addItem(i[0])

    def new_data(a):
        if ui.TName.text() != '' and len(
                ui.TName.text().split()) == 3 and ui.TYear.text() != '' and ui.SClasses.currentText() != '':
            idtab = max(map(lambda x: x[0], a.cursor().execute("""SELECT id FROM Persons""").fetchall()))
            inf_student = (idtab + 1, ui.TName.text(), ui.TYear.text(), 'Ученик', ui.SClasses.currentText())
            a.cursor().execute("""INSERT INTO Persons VALUES (?, ?, ?, ?, ?)""", inf_student)
            a.commit()
            ui.TName.setText('')
            ui.TYear.setText('')
            ui.SClasses.setCurrentIndex(0)
        else:
            error = QtWidgets.QMessageBox()
            if ui.TName.text() == "":
                error.setWindowTitle("Ошибка в поле ФИО")
                error.setText("Заполните поле ФИО")
            elif len(ui.TName.text().split()) != 3:
                error.setWindowTitle("Ошибка в поле ФИО")
                error.setText("Заполните поле ФИО корректно: <ФАМИЛИЯ ИМЯ ОТЧЕСТВО>")
            elif ui.TYear.text() == '':
                error.setWindowTitle("ОШИБКА В ПОЛЕ ГОДА")
                error.setText("Заполните поле года поступления ученика в школу")
            elif ui.SClasses.currentText() == '':
                error.setWindowTitle("ОШИБКА В ПОЛЕ КЛАССА")
                error.setText("Выберете класс из представленных")
            error.exec()

    connection = sqlite3.connect("School.db")
    data(connection)
    ui.Update.clicked.connect(lambda x: new_data(connection))
    ui.Back.clicked.connect(lambda x: move(sp, mw))


def gotoep():
    global ep, mw
    ep = QtWidgets.QMainWindow()
    ui = EmployeePlus()
    ui.setupUi(ep)
    move(mw, ep)
    ui.SRoles.addItem('')

    def data(a):
        res = a.cursor().execute("""SELECT Role FROM Role WHERE Role !='Ученик'""").fetchall()
        for i in res:
            ui.SRoles.addItem(i[0])

    def new_data(a):
        if ui.TName.text() != '' and len(
                ui.TName.text().split()) == 3 and ui.TYear.text() != '' and ui.SRoles.currentText() != '':
            idtab = max(map(lambda x: x[0], a.cursor().execute("""SELECT id FROM Persons""").fetchall()))
            inf_student = (idtab + 1, ui.TName.text(), ui.TYear.text(), ui.SRoles.currentText(), '-')
            a.cursor().execute("""INSERT INTO Persons VALUES (?, ?, ?, ?, ?)""", inf_student)
            a.commit()
            ui.TName.setText('')
            ui.TYear.setText('')
            ui.SRoles.setCurrentIndex(0)
        else:
            error = QtWidgets.QMessageBox()
            if ui.TName.text() == "":
                error.setWindowTitle("Ошибка в поле ФИО")
                error.setText("Заполните поле ФИО")
            elif len(ui.TName.text().split()) != 3:
                error.setWindowTitle("Ошибка в поле ФИО")
                error.setText("Заполните поле ФИО корректно: <ФАМИЛИЯ ИМЯ ОТЧЕСТВО>")
            elif ui.TYear.text() == '':
                error.setWindowTitle("ОШИБКА В ПОЛЕ ГОДА")
                error.setText("Заполните поле года поступления служащего на работу")
            elif ui.SRoles.currentText() == '':
                error.setWindowTitle("ОШИБКА В ПОЛЕ ПРОФФЕСИИ")
                error.setText("Выберете проффесию из представленных")
            error.exec()

    connection = sqlite3.connect("School.db")
    data(connection)
    ui.Update.clicked.connect(lambda x: new_data(connection))
    ui.Back.clicked.connect(lambda x: move(ep, mw))


def gotoud():
    global ud, mw
    ud = QtWidgets.QMainWindow()
    ui = UpDel()
    ui.setupUi(ud)
    move(mw, ud)

    def data(a):
        ui.SSet.clear()
        ui.SSet.addItem('')
        res = a.cursor().execute("""SELECT Name FROM Persons WHERE Name LIKE ?""",
                                 (str(ui.TSet.text()) + '%',)).fetchall()
        for i in res:
            ui.SSet.addItem(i[0])
        a.cursor().close()

    def showdata(a):
        ui.SRole.clear()
        ui.SClass.clear()
        if ui.SSet.currentText() != '':
            res = a.cursor().execute("""SELECT * FROM Persons WHERE Name = ?""", (ui.SSet.currentText(),)).fetchall()
            ui.TName.setText(str(res[0][1]))
            ui.TYear.setText(str(res[0][2]))
            res2 = a.cursor().execute("""SELECT Class FROM Classes""").fetchall()
            res3 = a.cursor().execute("""SELECT Role FROM Role""").fetchall()
            for i in res2:
                ui.SClass.addItem(i[0])
            for j in res3:
                ui.SRole.addItem(j[0])
            ui.SRole.setCurrentText(str(res[0][3]))
            ui.SClass.setCurrentText(str(res[0][4]))
        else:
            ui.TName.setText('')
            ui.TYear.setText('')

    def provirka():
        if ui.SRole.currentText() != "Ученик" and ui.SClass.currentText() != "-":
            return False
        elif ui.SRole.currentText() == "Ученик" and ui.SClass.currentText() == "-":
            return False
        else:
            return True

    def update(a):
        if ui.SSet.currentText() != "" and ui.TName.text() != "" and ui.TYear.text() != "" and len(
                ui.TName.text().split()) == 3 and provirka():
            x1 = ui.TName.text()
            x2 = ui.TYear.text()
            x3 = ui.SClass.currentText()
            x4 = ui.SRole.currentText()
            x5 = ui.SSet.currentText()
            a.cursor().execute("""UPDATE Persons SET Name = ?, Year = ?, Class = ?, Role = ? WHERE Name = ?""",
                               (x1, x2, x3, x4, x5))
            a.commit()
            ui.TSet.text()
            ui.TName.text()
            ui.TYear.text()
            ui.SClass.currentText()
            ui.SRole.currentText()
            data(a)
            ui.SSet.setCurrentIndex(0)
        else:
            error = QtWidgets.QMessageBox()
            if ui.SSet.currentText() == "":
                error.setWindowTitle("Ошибка в поле выбора")
                error.setText("Выберите человека, чьи данные вы хотите изменить")
            elif ui.TName.text() == "":
                error.setWindowTitle("Ошибка в поле ФИО")
                error.setText("Заполните поле ФИО")
            elif len(ui.TName.text().split()) != 3:
                error.setWindowTitle("Ошибка в поле ФИО")
                error.setText("Заполните поле ФИО корректно: <ФАМИЛИЯ ИМЯ ОТЧЕСТВО>")
            elif ui.TYear.text() == '':
                error.setWindowTitle("ОШИБКА В ПОЛЕ ГОДА")
                error.setText("Заполните поле года поступления {служащего на работу/ученика в школу}")
            elif not provirka():
                error.setWindowTitle("ОШИБКА В ЗАПОЛНЕНИИ ТАБЛИЦЫ")
                error.setText(
                    "Только для роли <Ученик> доступен выбор класса, для других ролей выбирайте вариант '-', "
                    "для <Ученик> же недоступен выбор варианта '-'")
            error.exec()

    def delete(a):
        if ui.SSet.currentText() != "":
            a.cursor().execute("""DELETE FROM Persons WHERE Name = ?""", (ui.SSet.currentText(),))
            a.commit()
            ui.TSet.text()
            ui.TName.text()
            ui.TYear.text()
            ui.SClass.currentText()
            ui.SRole.currentText()
            data(a)
            ui.SSet.setCurrentIndex(0)
        else:
            error = QtWidgets.QMessageBox()
            error.setWindowTitle("Ошибка в поле выбора")
            error.setText("Выберите человека, чьи данные вы хотите удалить")
            error.exec()

    connection = sqlite3.connect("School.db")
    data(connection)
    ui.TSet.textChanged.connect(lambda x: data(connection))
    ui.SSet.currentIndexChanged.connect(lambda x: showdata(connection))
    ui.Update.clicked.connect(lambda x: update(connection))
    ui.Delete.clicked.connect(lambda x: delete(connection))
    ui.Back.clicked.connect(lambda x: move(ud, mw))


def gotosch():
    global sch
    sch = QtWidgets.QMainWindow()
    ui = School()
    ui.setupUi(sch)
    move(mw, sch)
    ui.Back.clicked.connect(lambda x: move(sch, mw))


def ExitProg():
    sys.exit(app.exec_())


ui.StudentView.clicked.connect(gotosv)
ui.EmployeeView.clicked.connect(gotoev)
ui.StudentPlus.clicked.connect(gotosp)
ui.EmployeePlus.clicked.connect(gotoep)
ui.Updel.clicked.connect(gotoud)
ui.School.clicked.connect(gotosch)
ui.Exit.clicked.connect(ExitProg)
sys.exit(app.exec_())
