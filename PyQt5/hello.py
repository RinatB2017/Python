import sys
from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("Hello World! " + sys.argv[1])
label.show()
app.exec_()
