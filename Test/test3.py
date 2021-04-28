import sys
from PyQt5.QtWidgets import * # компоненты интерфейса
from PyQt5.QtCore import *

def btnClicked(self):
    QMessageBox.information(self, "Info", "OK")

def main():
    # Каждое приложение должно создать объект QApplication
    # sys.argv - список аргументов командной строки
    application = QApplication(sys.argv)

    # QWidget - базовый класс для всех объектов интерфейса
    # пользователя; если использовать для виджета конструктор
    # без родителя, такой виджет станет окном
    widget = QWidget()

    vbox = QVBoxLayout()

    label = QLabel()
    label.setText("HELLO")
    label.setAlignment(Qt.AlignHCenter)

    btn = QPushButton()
    btn.setText("OK")

    # btn.clicked.connect(btnClicked)
    # connect(btn, SIGNAL("Clicked()"), btnClicked)
    btn.clicked.connect(btnClicked)

    vbox.addWidget(label)
    vbox.addWidget(btn)
    vbox.addStretch()

    widget.setLayout(vbox)

    widget.resize(320, 240) # изменить размеры виджета
    widget.setWindowTitle("Hello, World!") # установить заголовок
    widget.show() # отобразить окно на экране

    sys.exit(application.exec_()) # запуск основного цикла

main()
