# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

# https://tproger.ru/translations/python-gui-pyqt/

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget

from mainwindow.mainwindow import Ui_MainWindow

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

    def test(self):
        QMessageBox.information(self, "Info",  "Тест",  QMessageBox.Ok)

    def xxx(self):
        print("XXX")

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
    app.exec_()                             # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()                  # то запускаем функцию main()
