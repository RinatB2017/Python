# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

# https://tproger.ru/translations/python-gui-pyqt/

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget, QDialog
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon

from mainwindow.mainwindow import Ui_MainWindow
from dialog.my_dialog import Ui_Dialog

# import test_classes.test_classes

from test_classes.class_0.class_0 import Class_0
from test_classes.class_1.class_1 import Class_1


import sys

#----------------------------------------------------------------------------------
#
# класс заменяет UI-класс, чтобы можно было его спокойно редактировать
#
class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.btn_test.clicked.connect(self.test_box)
        # self.btn_test.clicked.connect(self.test)
        # self.btn_test.clicked.connect(self.xxx)
        self.btn_0.clicked.connect(self.run_0)
        self.btn_1.clicked.connect(self.run_1)
        self.btn_run_dialog.clicked.connect(self.run_dialog)

    def run_dialog(self):
        dialog = QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.ui.sb_value.setValue(555)
        res = dialog.exec_()
        if res == QDialog.Accepted:
            self.te_log.append("value: " + str(dialog.ui.sb_value.value())) #QString в PyQt не работает

    def test(self):
        QMessageBox.information(self, "Info",  "Тест",  QMessageBox.Ok)

    def run_0(self):
        # c0 = Class_0()
        # self.te_log.append(c0.test())
        self.te_log.append(Class_0.test(self))

    def run_1(self):
        # c1 = Class_1()
        # self.te_log.append(c1.test())
        self.te_log.append(Class_1.test(self))

    def test_box(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        if retval == QMessageBox.Ok:
            self.te_log.append("OK")
            self.lbl_test.setText("OK")
        else:
            self.te_log.append("CANCEL")
            self.lbl_test.setText("CANCEL")
#----------------------------------------------------------------------------------

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()                   # Создаём объект класса ExampleApp
    window.show()                           # Показываем окно
    app.setApplicationName("Test_QMainWindow")
    app.setWindowIcon(QIcon("computer.ico"));
    app.exec_()                             # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()                  # то запускаем функцию main()
