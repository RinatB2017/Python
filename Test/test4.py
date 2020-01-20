import sys
from PyQt5 import QtWidgets,  QtGui,  QtCore
from PyQt5.QtWidgets import QMessageBox
from mydesign import Ui_MainWindow
  
class mywindow(QtWidgets.QMainWindow):
 
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # подключение клик-сигнал к слоту btnClicked
        self.ui.pushButton.clicked.connect(self.btnClicked)
 
    def btnClicked(self):
        self.ui.label.setText("Вы нажали на кнопку!")
        # Если не использовать, то часть текста исчезнет.
        self.ui.label.adjustSize()
        QMessageBox.information(self, "Info",  "OK",  QMessageBox.Ok)
        
        
        self.ui.label.setFont(
            QtGui.QFont('SansSerif', 30)
        ) # Изменение шрифта и размера

        self.ui.label.setGeometry(
            QtCore.QRect(10, 10, 250, 200)
        ) # изменить геометрию ярлыка
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())
