# -*- coding: utf-8 -*-

from pathlib import Path
import pandas as pd
import sys, os, io
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5.uic as uic
from mailmerge import MailMerge
from docx2pdf import convert
import shutil


excel = ["Solarmodule_Nummern.xlsx",
         "Wechselrichter_Nummern.xlsx",
         "Leistungsoptimierer_Nummern.xlsx",
         "Zähler_Nummern.xlsx",
         "Anlageüberwachung_Nummern.xlsx",
         "Leistungsregler_Nummern.xlsx",
         "Ladestation_Nummern.xlsx",
         "Batterie_Nummern.xlsx",
         "Unterkonstruktion_Nummern.xlsx",
         "Überspannungsschutz_Nummern.xlsx",
         "Anzeigetafeln_Monitoren_Nummern.xlsx",
         "Sensoren_Nummern.xlsx",]

ordnerstruktur = ['1.-3. Dokumentationsblätter', 
                  '4.01 Solarmodule', 
                  '4.02 Wechselrichter', 
                  '4.03 Leistungsoptimierer', 
                  '4.04 Zähler', 
                  '4.05 Anlageüberwachung', 
                  '4.06 Leistungsregler', 
                  '4.07 Ladestation', 
                  '4.08 Batterie', 
                  '4.09 Unterkonstruktion', 
                  '4.10 Überspannungsschutz', 
                  '4.11 Anzeigetafeln_Monitoren', 
                  '4.12 Sensoren']

monateDE = ['',
            'Januar',
            'Februar',
            'März',
            'April',
            'Mai',
            'Juni',
            'Juli',
            'August',
            'September',
            'Oktober',
            'November',
            'Dezember']

monateFR = ['',
            'janvier',
            'février',
            'mars',
            'avril',
            'mai',
            'juin',
            'juillet',
            'août',
            'septembre',
            'octobre',
            'novembre',
            'décembre']

monateEN = ['',
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'Dezember']

    
    ####wechselrichter marken ermitteln####

sol_marken = []
wr_marken = []
leist_o_marken = []
zeh_marken = []
anlage_marken = []
leist_r_marken = []
lade_marken = []
batt_marken = []
unterkon_marken = []
ueberspan_marken = []
anzeiget_marken = []
sens_marken = []

def hersteller(a, b):
    for i in Path(a).glob("*"):
        if i.suffix == ".xlsx":
            continue
        elif i.suffix == ".pdf":
            continue
        else:
            b.append(i.name)

hersteller(ordnerstruktur[1], sol_marken)
hersteller(ordnerstruktur[2], wr_marken)
hersteller(ordnerstruktur[3], leist_o_marken)
hersteller(ordnerstruktur[4], zeh_marken)
hersteller(ordnerstruktur[5], anlage_marken)
hersteller(ordnerstruktur[6], leist_r_marken)
hersteller(ordnerstruktur[7], lade_marken)
hersteller(ordnerstruktur[8], batt_marken)
hersteller(ordnerstruktur[9], unterkon_marken)
hersteller(ordnerstruktur[10], ueberspan_marken)
hersteller(ordnerstruktur[11], anzeiget_marken)
hersteller(ordnerstruktur[12], sens_marken)


####Excel auslesen####

#class first:
#Solarmodule
sol_typen1 = []
sol_typen2 = []
sol_typen3 = []
sol_typen4 = []
#sol_typen5 = []
#sol_typen6 = []
#sol_typen7 = []
#sol_typen8 = []
#sol_typen9 = []
#sol_typen10 = []

wr_typen1 = []
wr_typen2 = []
wr_typen3 = []
wr_typen4 = []
wr_typen5 = []

leist_o_typen1 = []
leist_o_typen2 = []

zeh_typen1 = []
zeh_typen2 = []
zeh_typen3 = []

anlage_typen1 = []
anlage_typen2 = []
anlage_typen3 = []
anlage_typen4 = []
anlage_typen5 = []

leist_typen1 = []
leist_typen2 = []
leist_typen3 = []

lade_typen1 = []
lade_typen2 = []
lade_typen3 = []
lade_typen4 = []

batt_typen1 = []
batt_typen2 = []
batt_typen3 = []
batt_typen4 = []
batt_typen5 = []
batt_typen6 = []
batt_typen7 = []

unterkon_typen1 = []

ueberspan_typen1 = []
ueberspan_typen2 = []
ueberspan_typen3 = []

anzeiget_typen1 = []

sens_typen1 = []
sens_typen2 = []


def excelRead(a, b, c, d):
    x = pd.read_excel(Path(a, b), 
                            header=0, 
                            sheet_name=c, 
                            usecols='A, B, D, F, H, J, L, N, P, R, T, V, X, Z')
    wr_doc_nr = x.values.tolist()


    y = pd.read_excel(Path(a, b), 
                            header=0, 
                            sheet_name=c, 
                            usecols='A')
    y = y.fillna('')
    z = list(y['Name'])
    for i in z:
        d.append(str(i))




excelRead(ordnerstruktur[1], excel[0], sol_marken[0], sol_typen1)
excelRead(ordnerstruktur[1], excel[0], sol_marken[1], sol_typen2)
excelRead(ordnerstruktur[1], excel[0], sol_marken[2], sol_typen3)
excelRead(ordnerstruktur[1], excel[0], sol_marken[3], sol_typen4)
#excelRead(ordnerstruktur[1], excel[0], sol_marken[4], sol_typen5)
#excelRead(ordnerstruktur[1], excel[0], sol_marken[5], sol_typen6)
#excelRead(ordnerstruktur[1], excel[0], sol_marken[6], sol_typen7)
#excelRead(ordnerstruktur[1], excel[0], sol_marken[7], sol_typen8)
#excelRead(ordnerstruktur[1], excel[0], sol_marken[8], sol_typen9)
#excelRead(ordnerstruktur[1], excel[0], sol_marken[9], sol_typen10)

excelRead(ordnerstruktur[2], excel[1], wr_marken[0], wr_typen1)
excelRead(ordnerstruktur[2], excel[1], wr_marken[1], wr_typen2)
excelRead(ordnerstruktur[2], excel[1], wr_marken[2], wr_typen3)
excelRead(ordnerstruktur[2], excel[1], wr_marken[3], wr_typen4)
excelRead(ordnerstruktur[2], excel[1], wr_marken[4], wr_typen5)

excelRead(ordnerstruktur[3], excel[2], leist_o_marken[0], leist_o_typen1)
excelRead(ordnerstruktur[3], excel[2], leist_o_marken[1], leist_o_typen2)

excelRead(ordnerstruktur[4], excel[3], zeh_marken[0], zeh_typen1)
excelRead(ordnerstruktur[4], excel[3], zeh_marken[1], zeh_typen2)
excelRead(ordnerstruktur[4], excel[3], zeh_marken[2], zeh_typen3)

excelRead(ordnerstruktur[5], excel[4], anlage_marken[0], anlage_typen1)
excelRead(ordnerstruktur[5], excel[4], anlage_marken[1], anlage_typen2)
excelRead(ordnerstruktur[5], excel[4], anlage_marken[2], anlage_typen3)
excelRead(ordnerstruktur[5], excel[4], anlage_marken[3], anlage_typen4)
excelRead(ordnerstruktur[5], excel[4], anlage_marken[4], anlage_typen5)

excelRead(ordnerstruktur[6], excel[5], leist_r_marken[0], leist_typen1)
excelRead(ordnerstruktur[6], excel[5], leist_r_marken[1], leist_typen2)
excelRead(ordnerstruktur[6], excel[5], leist_r_marken[2], leist_typen3)

excelRead(ordnerstruktur[7], excel[6], lade_marken[0], lade_typen1)
excelRead(ordnerstruktur[7], excel[6], lade_marken[1], lade_typen2)
excelRead(ordnerstruktur[7], excel[6], lade_marken[2], lade_typen3)
excelRead(ordnerstruktur[7], excel[6], lade_marken[3], lade_typen4)

excelRead(ordnerstruktur[8], excel[7], batt_marken[0], batt_typen1)
excelRead(ordnerstruktur[8], excel[7], batt_marken[1], batt_typen2)
excelRead(ordnerstruktur[8], excel[7], batt_marken[2], batt_typen3)
excelRead(ordnerstruktur[8], excel[7], batt_marken[3], batt_typen4)
excelRead(ordnerstruktur[8], excel[7], batt_marken[4], batt_typen5)
excelRead(ordnerstruktur[8], excel[7], batt_marken[5], batt_typen6)
excelRead(ordnerstruktur[8], excel[7], batt_marken[6], batt_typen7)

excelRead(ordnerstruktur[9], excel[8], unterkon_marken[0], unterkon_typen1)

excelRead(ordnerstruktur[10], excel[9], ueberspan_marken[0], ueberspan_typen1)
excelRead(ordnerstruktur[10], excel[9], ueberspan_marken[1], ueberspan_typen2)
excelRead(ordnerstruktur[10], excel[9], ueberspan_marken[2], ueberspan_typen3)

excelRead(ordnerstruktur[11], excel[10], anzeiget_marken[0], anzeiget_typen1)

excelRead(ordnerstruktur[12], excel[11], sens_marken[0], sens_typen1)
excelRead(ordnerstruktur[12], excel[11], sens_marken[1], sens_typen2)



        ####Qt Designer####
        

# Form implementation generated from reading ui file 'definitiv.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.




class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1800, 800)
        Form.setAcceptDrops(False)
        Form.setStyleSheet("background-color: rgb(76, 76, 76);\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_29 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setMaximumSize(QtCore.QSize(70, 45))
        self.label_29.setText("")
        self.label_29.setPixmap(QtGui.QPixmap("Zeichenfläche 1.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 0, 2, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setToolTipDuration(-1)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("/*background-color: rgb(76, 76, 76);*/\n"
"\n"
"font: 8pt \"Century Gothic\";")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setStyleSheet("background-color: rgb(225,225,225);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 553, 459))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.lineEdit_ortobjekt_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_ortobjekt_2.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.lineEdit_ortobjekt_2.setObjectName("lineEdit_ortobjekt_2")
        self.gridLayout_11.addWidget(self.lineEdit_ortobjekt_2, 18, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout_11.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_13.setObjectName("label_13")
        self.gridLayout_11.addWidget(self.label_13, 16, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout_11.addWidget(self.label_8, 5, 0, 1, 1)
        self.comboBox_sprache = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_sprache.setObjectName("comboBox_sprache")
        self.gridLayout_11.addWidget(self.comboBox_sprache, 0, 4, 1, 1)
        self.lineEdit_kwh = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_kwh.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_kwh.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.lineEdit_kwh.setObjectName("lineEdit_kwh")
        self.gridLayout_11.addWidget(self.lineEdit_kwh, 18, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout_11.addWidget(self.label_5, 8, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_16.setObjectName("label_16")
        self.gridLayout_11.addWidget(self.label_16, 22, 0, 1, 1)
        self.lineEdit_strasse = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_strasse.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.lineEdit_strasse.setObjectName("lineEdit_strasse")
        self.gridLayout_11.addWidget(self.lineEdit_strasse, 6, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 8pt \"Century Gothic\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.gridLayout_11.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_strasseobjekt = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_strasseobjekt.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.lineEdit_strasseobjekt.setObjectName("lineEdit_strasseobjekt")
        self.gridLayout_11.addWidget(self.lineEdit_strasseobjekt, 16, 0, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_14.setObjectName("label_14")
        self.gridLayout_11.addWidget(self.label_14, 22, 1, 1, 1)
        self.lineEdit_ort_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_ort_2.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.lineEdit_ort_2.setObjectName("lineEdit_ort_2")
        self.gridLayout_11.addWidget(self.lineEdit_ort_2, 9, 0, 1, 1)
        self.lineEdit_m2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_m2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_m2.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.lineEdit_m2.setObjectName("lineEdit_m2")
        self.gridLayout_11.addWidget(self.lineEdit_m2, 15, 2, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_30.setObjectName("label_30")
        self.gridLayout_11.addWidget(self.label_30, 0, 2, 1, 1)
        self.dateEdit_bis = QtWidgets.QDateEdit(self.scrollAreaWidgetContents_2, calendarPopup=True)
        self.dateEdit_bis.setMaximumSize(QtCore.QSize(110, 16777215))
        self.dateEdit_bis.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.dateEdit_bis.setObjectName("dateEdit_bis")
        self.gridLayout_11.addWidget(self.dateEdit_bis, 23, 2, 1, 3)
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_25.setObjectName("label_25")
        self.gridLayout_11.addWidget(self.label_25, 17, 4, 1, 1)
        self.lineEdit_kva = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_kva.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_kva.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.lineEdit_kva.setObjectName("lineEdit_kva")
        self.gridLayout_11.addWidget(self.lineEdit_kva, 17, 2, 1, 1)
        self.dateEdit_von = QtWidgets.QDateEdit(self.scrollAreaWidgetContents_2, calendarPopup=True)
        self.dateEdit_von.setMaximumSize(QtCore.QSize(110, 16777215))
        self.dateEdit_von.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.dateEdit_von.setObjectName("dateEdit_von")
        self.gridLayout_11.addWidget(self.dateEdit_von, 23, 1, 1, 1)
        self.groupBox_DragDrop = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_DragDrop.sizePolicy().hasHeightForWidth())
        self.groupBox_DragDrop.setSizePolicy(sizePolicy)
        self.groupBox_DragDrop.setMaximumSize(QtCore.QSize(220, 16777215))
        self.groupBox_DragDrop.setAcceptDrops(True)
        self.groupBox_DragDrop.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.groupBox_DragDrop.setObjectName("groupBox_DragDrop")
        self.label_10 = QtWidgets.QLabel(self.groupBox_DragDrop)
        self.label_10.setGeometry(QtCore.QRect(10, 90, 220, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMaximumSize(QtCore.QSize(220, 16777215))
        self.label_10.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_10.setObjectName("label_10")
        self.gridLayout_11.addWidget(self.groupBox_DragDrop, 2, 2, 10, 3)
        self.checkBox_objekt = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.checkBox_objekt.setFont(font)
        self.checkBox_objekt.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.checkBox_objekt.setObjectName("checkBox_objekt")
        self.gridLayout_11.addWidget(self.checkBox_objekt, 14, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_11.setObjectName("label_11")
        self.gridLayout_11.addWidget(self.label_11, 17, 0, 1, 1)
        self.lineEdit_plzobjekt = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_plzobjekt.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.lineEdit_plzobjekt.setObjectName("lineEdit_plzobjekt")
        self.gridLayout_11.addWidget(self.lineEdit_plzobjekt, 18, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_17.setObjectName("label_17")
        self.gridLayout_11.addWidget(self.label_17, 22, 2, 1, 1)
        self.dateEdit_inbetriebnahme = QtWidgets.QDateEdit(self.scrollAreaWidgetContents_2, calendarPopup=True)
        self.dateEdit_inbetriebnahme.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateEdit_inbetriebnahme.setFont(font)
        self.dateEdit_inbetriebnahme.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.dateEdit_inbetriebnahme.setObjectName("dateEdit_inbetriebnahme")
        self.gridLayout_11.addWidget(self.dateEdit_inbetriebnahme, 23, 0, 1, 1)
        self.lineEdit_nachname = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_nachname.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.lineEdit_nachname.setObjectName("lineEdit_nachname")
        self.gridLayout_11.addWidget(self.lineEdit_nachname, 4, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout_11.addWidget(self.label_7, 8, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_name.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout_11.addWidget(self.lineEdit_name, 2, 0, 1, 2)
        self.lineEdit_plz = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_plz.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.lineEdit_plz.setObjectName("lineEdit_plz")
        self.gridLayout_11.addWidget(self.lineEdit_plz, 9, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.gridLayout_11.addWidget(self.label_31, 12, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout_11.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_11.addWidget(self.label_2, 20, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_18.setObjectName("label_18")
        self.gridLayout_11.addWidget(self.label_18, 17, 1, 1, 1)
        self.lineEdit_kwp = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_kwp.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_kwp.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.lineEdit_kwp.setObjectName("lineEdit_kwp")
        self.gridLayout_11.addWidget(self.lineEdit_kwp, 16, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_12.setObjectName("label_12")
        self.gridLayout_11.addWidget(self.label_12, 15, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_15.setObjectName("label_15")
        self.gridLayout_11.addWidget(self.label_15, 18, 4, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_26.setObjectName("label_26")
        self.gridLayout_11.addWidget(self.label_26, 15, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem, 25, 2, 1, 1)
        self.pushButton_PDF = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_PDF.setStyleSheet("background-color: rgb(159, 159, 159);")
        self.pushButton_PDF.setObjectName("pushButton_PDF")
        self.gridLayout_11.addWidget(self.pushButton_PDF, 24, 1, 1, 4)
        self.pushButton_speichern = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_speichern.setStyleSheet("background-color: rgb(159, 159, 159);")
        self.pushButton_speichern.setObjectName("pushButton_speichern")
        self.gridLayout_11.addWidget(self.pushButton_speichern, 24, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab, "")
        self.Tab2 = QtWidgets.QWidget()
        self.Tab2.setObjectName("Tab2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Tab2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.Tab2)
        self.scrollArea_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 270, 595))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_70 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_70.setFont(font)
        self.label_70.setObjectName("label_70")
        self.gridLayout_7.addWidget(self.label_70, 20, 0, 1, 1)
        self.comboBox_zahler = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_zahler.sizePolicy().hasHeightForWidth())
        self.comboBox_zahler.setSizePolicy(sizePolicy)
        self.comboBox_zahler.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_zahler.setAcceptDrops(False)
        self.comboBox_zahler.setObjectName("comboBox_zahler")
        self.gridLayout_7.addWidget(self.comboBox_zahler, 8, 0, 1, 1)
        self.comboBox_leistungso = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_leistungso.sizePolicy().hasHeightForWidth())
        self.comboBox_leistungso.setSizePolicy(sizePolicy)
        self.comboBox_leistungso.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_leistungso.setAcceptDrops(False)
        self.comboBox_leistungso.setObjectName("comboBox_leistungso")
        self.gridLayout_7.addWidget(self.comboBox_leistungso, 5, 0, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.gridLayout_7.addWidget(self.label_44, 12, 0, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.gridLayout_7.addWidget(self.label_42, 12, 2, 1, 1)
        self.comboBox_modultyp = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_modultyp.sizePolicy().hasHeightForWidth())
        self.comboBox_modultyp.setSizePolicy(sizePolicy)
        self.comboBox_modultyp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_modultyp.setAcceptDrops(False)
        self.comboBox_modultyp.setObjectName("comboBox_modultyp")
        self.gridLayout_7.addWidget(self.comboBox_modultyp, 1, 2, 1, 1)
        self.comboBox_gaktyp = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_gaktyp.sizePolicy().hasHeightForWidth())
        self.comboBox_gaktyp.setSizePolicy(sizePolicy)
        self.comboBox_gaktyp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_gaktyp.setAcceptDrops(False)
        self.comboBox_gaktyp.setObjectName("comboBox_gaktyp")
        self.gridLayout_7.addWidget(self.comboBox_gaktyp, 26, 2, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.gridLayout_7.addWidget(self.label_69, 25, 0, 1, 1)
        self.comboBox_zahlertyp = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_zahlertyp.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_zahlertyp.sizePolicy().hasHeightForWidth())
        self.comboBox_zahlertyp.setSizePolicy(sizePolicy)
        self.comboBox_zahlertyp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_zahlertyp.setAcceptDrops(False)
        self.comboBox_zahlertyp.setObjectName("comboBox_zahlertyp")
        self.gridLayout_7.addWidget(self.comboBox_zahlertyp, 8, 2, 1, 1)
        self.comboBox_leistungsrtyp = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_leistungsrtyp.sizePolicy().hasHeightForWidth())
        self.comboBox_leistungsrtyp.setSizePolicy(sizePolicy)
        self.comboBox_leistungsrtyp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_leistungsrtyp.setAcceptDrops(False)
        self.comboBox_leistungsrtyp.setObjectName("comboBox_leistungsrtyp")
        self.gridLayout_7.addWidget(self.comboBox_leistungsrtyp, 13, 2, 1, 1)
        self.comboBox_lasttyp = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_lasttyp.sizePolicy().hasHeightForWidth())
        self.comboBox_lasttyp.setSizePolicy(sizePolicy)
        self.comboBox_lasttyp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_lasttyp.setAcceptDrops(False)
        self.comboBox_lasttyp.setObjectName("comboBox_lasttyp")
        self.gridLayout_7.addWidget(self.comboBox_lasttyp, 15, 2, 1, 1)
        self.label_65 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.gridLayout_7.addWidget(self.label_65, 14, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_33.setObjectName("label_33")
        self.gridLayout_7.addWidget(self.label_33, 0, 2, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.gridLayout_7.addWidget(self.label_72, 29, 0, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.gridLayout_7.addWidget(self.label_66, 20, 2, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_75.setFont(font)
        self.label_75.setObjectName("label_75")
        self.gridLayout_7.addWidget(self.label_75, 17, 0, 1, 1)
        self.comboBox_anzeigetaftyp = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_anzeigetaftyp.sizePolicy().hasHeightForWidth())
        self.comboBox_anzeigetaftyp.setSizePolicy(sizePolicy)
        self.comboBox_anzeigetaftyp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_anzeigetaftyp.setAcceptDrops(False)
        self.comboBox_anzeigetaftyp.setObjectName("comboBox_anzeigetaftyp")
        self.gridLayout_7.addWidget(self.comboBox_anzeigetaftyp, 28, 2, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.gridLayout_7.addWidget(self.label_40, 7, 2, 1, 1)
        self.comboBox_sensortyp = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_sensortyp.sizePolicy().hasHeightForWidth())
        self.comboBox_sensortyp.setSizePolicy(sizePolicy)
        self.comboBox_sensortyp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_sensortyp.setAcceptDrops(False)
        self.comboBox_sensortyp.setObjectName("comboBox_sensortyp")
        self.gridLayout_7.addWidget(self.comboBox_sensortyp, 30, 2, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.gridLayout_7.addWidget(self.label_36, 2, 0, 1, 1)
        self.comboBox_uberwachtyp = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_uberwachtyp.sizePolicy().hasHeightForWidth())
        self.comboBox_uberwachtyp.setSizePolicy(sizePolicy)
        self.comboBox_uberwachtyp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_uberwachtyp.setAcceptDrops(False)
        self.comboBox_uberwachtyp.setObjectName("comboBox_uberwachtyp")
        self.gridLayout_7.addWidget(self.comboBox_uberwachtyp, 11, 2, 1, 1)
        self.label_64 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.gridLayout_7.addWidget(self.label_64, 27, 0, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.gridLayout_7.addWidget(self.label_41, 10, 0, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.gridLayout_7.addWidget(self.label_39, 4, 0, 1, 1)
        self.comboBox_leistungsotyp = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_leistungsotyp.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_leistungsotyp.sizePolicy().hasHeightForWidth())
        self.comboBox_leistungsotyp.setSizePolicy(sizePolicy)
        self.comboBox_leistungsotyp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_leistungsotyp.setAcceptDrops(False)
        self.comboBox_leistungsotyp.setObjectName("comboBox_leistungsotyp")
        self.gridLayout_7.addWidget(self.comboBox_leistungsotyp, 5, 2, 1, 1)
        self.comboBox_batterie = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_batterie.sizePolicy().hasHeightForWidth())
        self.comboBox_batterie.setSizePolicy(sizePolicy)
        self.comboBox_batterie.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_batterie.setAcceptDrops(False)
        self.comboBox_batterie.setObjectName("comboBox_batterie")
        self.gridLayout_7.addWidget(self.comboBox_batterie, 18, 0, 1, 1)
        self.comboBox_batterietyp = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_batterietyp.sizePolicy().hasHeightForWidth())
        self.comboBox_batterietyp.setSizePolicy(sizePolicy)
        self.comboBox_batterietyp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_batterietyp.setAcceptDrops(False)
        self.comboBox_batterietyp.setObjectName("comboBox_batterietyp")
        self.gridLayout_7.addWidget(self.comboBox_batterietyp, 18, 2, 1, 1)
        self.comboBox_wr = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_wr.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_wr.sizePolicy().hasHeightForWidth())
        self.comboBox_wr.setSizePolicy(sizePolicy)
        self.comboBox_wr.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_wr.setAcceptDrops(False)
        self.comboBox_wr.setObjectName("comboBox_wr")
        self.gridLayout_7.addWidget(self.comboBox_wr, 3, 0, 1, 1)
        self.pushButton_unterkonberechnung = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_unterkonberechnung.setObjectName("pushButton_unterkonberechnung")
        self.gridLayout_7.addWidget(self.pushButton_unterkonberechnung, 23, 0, 1, 1)
        self.comboBox_uberwach = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_uberwach.sizePolicy().hasHeightForWidth())
        self.comboBox_uberwach.setSizePolicy(sizePolicy)
        self.comboBox_uberwach.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_uberwach.setAcceptDrops(False)
        self.comboBox_uberwach.setObjectName("comboBox_uberwach")
        self.gridLayout_7.addWidget(self.comboBox_uberwach, 11, 0, 1, 1)
        self.comboBox_anzeigeta = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_anzeigeta.sizePolicy().hasHeightForWidth())
        self.comboBox_anzeigeta.setSizePolicy(sizePolicy)
        self.comboBox_anzeigeta.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_anzeigeta.setAcceptDrops(False)
        self.comboBox_anzeigeta.setObjectName("comboBox_anzeigeta")
        self.gridLayout_7.addWidget(self.comboBox_anzeigeta, 28, 0, 1, 1)
        self.comboBox_gak = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_gak.sizePolicy().hasHeightForWidth())
        self.comboBox_gak.setSizePolicy(sizePolicy)
        self.comboBox_gak.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_gak.setAcceptDrops(False)
        self.comboBox_gak.setObjectName("comboBox_gak")
        self.gridLayout_7.addWidget(self.comboBox_gak, 26, 0, 1, 1)
        self.comboBox_unterkontyp = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_unterkontyp.sizePolicy().hasHeightForWidth())
        self.comboBox_unterkontyp.setSizePolicy(sizePolicy)
        self.comboBox_unterkontyp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_unterkontyp.setAcceptDrops(False)
        self.comboBox_unterkontyp.setObjectName("comboBox_unterkontyp")
        self.gridLayout_7.addWidget(self.comboBox_unterkontyp, 21, 2, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("font: 8pt \"Century Gothic\";")
        self.label_34.setObjectName("label_34")
        self.gridLayout_7.addWidget(self.label_34, 0, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.gridLayout_7.addWidget(self.label_37, 7, 0, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.gridLayout_7.addWidget(self.label_71, 25, 2, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.gridLayout_7.addWidget(self.label_38, 4, 2, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.gridLayout_7.addWidget(self.label_68, 14, 2, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.gridLayout_7.addWidget(self.label_74, 17, 2, 1, 1)
        self.label_161 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_161.setFont(font)
        self.label_161.setObjectName("label_161")
        self.gridLayout_7.addWidget(self.label_161, 22, 0, 1, 1)
        self.comboBox_ladest = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_ladest.sizePolicy().hasHeightForWidth())
        self.comboBox_ladest.setSizePolicy(sizePolicy)
        self.comboBox_ladest.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_ladest.setAcceptDrops(False)
        self.comboBox_ladest.setObjectName("comboBox_ladest")
        self.gridLayout_7.addWidget(self.comboBox_ladest, 15, 0, 1, 1)
        self.comboBox_unterkon = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_unterkon.sizePolicy().hasHeightForWidth())
        self.comboBox_unterkon.setSizePolicy(sizePolicy)
        self.comboBox_unterkon.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_unterkon.setAcceptDrops(False)
        self.comboBox_unterkon.setObjectName("comboBox_unterkon")
        self.gridLayout_7.addWidget(self.comboBox_unterkon, 21, 0, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.gridLayout_7.addWidget(self.label_43, 10, 2, 1, 1)
        self.comboBox_modul = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_modul.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_modul.sizePolicy().hasHeightForWidth())
        self.comboBox_modul.setSizePolicy(sizePolicy)
        self.comboBox_modul.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_modul.setAcceptDrops(False)
        self.comboBox_modul.setObjectName("comboBox_modul")
        self.gridLayout_7.addWidget(self.comboBox_modul, 1, 0, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.gridLayout_7.addWidget(self.label_35, 2, 2, 1, 1)
        self.comboBox_sensor = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_sensor.sizePolicy().hasHeightForWidth())
        self.comboBox_sensor.setSizePolicy(sizePolicy)
        self.comboBox_sensor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_sensor.setAcceptDrops(False)
        self.comboBox_sensor.setObjectName("comboBox_sensor")
        self.gridLayout_7.addWidget(self.comboBox_sensor, 30, 0, 1, 1)
        self.comboBox_leistungsr = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_leistungsr.sizePolicy().hasHeightForWidth())
        self.comboBox_leistungsr.setSizePolicy(sizePolicy)
        self.comboBox_leistungsr.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_leistungsr.setAcceptDrops(False)
        self.comboBox_leistungsr.setObjectName("comboBox_leistungsr")
        self.gridLayout_7.addWidget(self.comboBox_leistungsr, 13, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem1, 31, 0, 1, 1)
        self.comboBox_wrtyp = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_wrtyp.sizePolicy().hasHeightForWidth())
        self.comboBox_wrtyp.setSizePolicy(sizePolicy)
        self.comboBox_wrtyp.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_wrtyp.setAcceptDrops(False)
        self.comboBox_wrtyp.setObjectName("comboBox_wrtyp")
        self.gridLayout_7.addWidget(self.comboBox_wrtyp, 3, 2, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.gridLayout_7.addWidget(self.label_67, 27, 2, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.gridLayout_7.addWidget(self.label_73, 29, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 3, 1, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Tab2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 553, 353))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_138 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_138.setFont(font)
        self.label_138.setObjectName("label_138")
        self.gridLayout_12.addWidget(self.label_138, 10, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_12.addWidget(self.lineEdit_2, 7, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_12.addWidget(self.lineEdit_3, 11, 0, 1, 1)
        self.label_144 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_144.setFont(font)
        self.label_144.setObjectName("label_144")
        self.gridLayout_12.addWidget(self.label_144, 14, 3, 1, 1)
        self.label_149 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_149.setFont(font)
        self.label_149.setObjectName("label_149")
        self.gridLayout_12.addWidget(self.label_149, 18, 3, 1, 1)
        self.label_135 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_135.setFont(font)
        self.label_135.setObjectName("label_135")
        self.gridLayout_12.addWidget(self.label_135, 6, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.gridLayout_12.addWidget(self.label_21, 8, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_12.addWidget(self.lineEdit_4, 15, 0, 1, 1)
        self.label_147 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_147.setFont(font)
        self.label_147.setObjectName("label_147")
        self.gridLayout_12.addWidget(self.label_147, 18, 2, 1, 1)
        self.label_141 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_141.setFont(font)
        self.label_141.setObjectName("label_141")
        self.gridLayout_12.addWidget(self.label_141, 10, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.gridLayout_12.addWidget(self.label_20, 4, 1, 1, 1)
        self.lineEdit_planer_plz = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_planer_plz.setObjectName("lineEdit_planer_plz")
        self.gridLayout_12.addWidget(self.lineEdit_planer_plz, 3, 2, 1, 1)
        self.lineEdit_elektroin_strasse = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_elektroin_strasse.setObjectName("lineEdit_elektroin_strasse")
        self.gridLayout_12.addWidget(self.lineEdit_elektroin_strasse, 11, 1, 1, 1)
        self.comboBox_elektroin_ort = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_elektroin_ort.sizePolicy().hasHeightForWidth())
        self.comboBox_elektroin_ort.setSizePolicy(sizePolicy)
        self.comboBox_elektroin_ort.setObjectName("comboBox_elektroin_ort")
        self.gridLayout_12.addWidget(self.comboBox_elektroin_ort, 11, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.gridLayout_12.addWidget(self.label_22, 12, 1, 1, 1)
        self.lineEdit_elektroin_plz = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_elektroin_plz.setObjectName("lineEdit_elektroin_plz")
        self.gridLayout_12.addWidget(self.lineEdit_elektroin_plz, 11, 2, 1, 1)
        self.lineEdit_abs_strasse = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_abs_strasse.setObjectName("lineEdit_abs_strasse")
        self.gridLayout_12.addWidget(self.lineEdit_abs_strasse, 15, 1, 1, 1)
        self.lineEdit_pv_strasse = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_pv_strasse.setObjectName("lineEdit_pv_strasse")
        self.gridLayout_12.addWidget(self.lineEdit_pv_strasse, 7, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.gridLayout_12.addWidget(self.label_23, 16, 1, 1, 1)
        self.comboBox_abs_ort = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_abs_ort.sizePolicy().hasHeightForWidth())
        self.comboBox_abs_ort.setSizePolicy(sizePolicy)
        self.comboBox_abs_ort.setMouseTracking(True)
        self.comboBox_abs_ort.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBox_abs_ort.setObjectName("comboBox_abs_ort")
        self.gridLayout_12.addWidget(self.comboBox_abs_ort, 15, 3, 1, 1)
        self.label_148 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_148.setFont(font)
        self.label_148.setObjectName("label_148")
        self.gridLayout_12.addWidget(self.label_148, 18, 1, 1, 1)
        self.comboBox_pv_ort = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_pv_ort.sizePolicy().hasHeightForWidth())
        self.comboBox_pv_ort.setSizePolicy(sizePolicy)
        self.comboBox_pv_ort.setObjectName("comboBox_pv_ort")
        self.gridLayout_12.addWidget(self.comboBox_pv_ort, 7, 3, 1, 1)
        self.label_133 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_133.setFont(font)
        self.label_133.setObjectName("label_133")
        self.gridLayout_12.addWidget(self.label_133, 2, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem2, 20, 1, 1, 1)
        self.lineEdit_geruste_plz = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_geruste_plz.setObjectName("lineEdit_geruste_plz")
        self.gridLayout_12.addWidget(self.lineEdit_geruste_plz, 19, 2, 1, 1)
        self.lineEdit_Geruste_strasse = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_Geruste_strasse.setObjectName("lineEdit_Geruste_strasse")
        self.gridLayout_12.addWidget(self.lineEdit_Geruste_strasse, 19, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_12.addWidget(self.lineEdit_5, 19, 0, 1, 1)
        self.comboBox_geruste_ort = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_geruste_ort.sizePolicy().hasHeightForWidth())
        self.comboBox_geruste_ort.setSizePolicy(sizePolicy)
        self.comboBox_geruste_ort.setMouseTracking(True)
        self.comboBox_geruste_ort.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBox_geruste_ort.setObjectName("comboBox_geruste_ort")
        self.gridLayout_12.addWidget(self.comboBox_geruste_ort, 19, 3, 1, 1)
        self.label_139 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_139.setFont(font)
        self.label_139.setObjectName("label_139")
        self.gridLayout_12.addWidget(self.label_139, 10, 1, 1, 1)
        self.label_79 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_79.setFont(font)
        self.label_79.setObjectName("label_79")
        self.gridLayout_12.addWidget(self.label_79, 2, 2, 1, 1)
        self.label_132 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_132.setFont(font)
        self.label_132.setObjectName("label_132")
        self.gridLayout_12.addWidget(self.label_132, 2, 1, 1, 1)
        self.label_143 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_143.setFont(font)
        self.label_143.setObjectName("label_143")
        self.gridLayout_12.addWidget(self.label_143, 14, 2, 1, 1)
        self.lineEdit_abs_plz = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_abs_plz.setObjectName("lineEdit_abs_plz")
        self.gridLayout_12.addWidget(self.lineEdit_abs_plz, 15, 2, 1, 1)
        self.lineEdit_pv_plz = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_pv_plz.setObjectName("lineEdit_pv_plz")
        self.gridLayout_12.addWidget(self.lineEdit_pv_plz, 7, 2, 1, 1)
        self.label_136 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_136.setFont(font)
        self.label_136.setObjectName("label_136")
        self.gridLayout_12.addWidget(self.label_136, 6, 2, 1, 1)
        self.lineEdit_planer_strasse = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit_planer_strasse.setObjectName("lineEdit_planer_strasse")
        self.gridLayout_12.addWidget(self.lineEdit_planer_strasse, 3, 1, 1, 1)
        self.comboBox_planer_ort = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_planer_ort.sizePolicy().hasHeightForWidth())
        self.comboBox_planer_ort.setSizePolicy(sizePolicy)
        self.comboBox_planer_ort.setObjectName("comboBox_planer_ort")
        self.gridLayout_12.addWidget(self.comboBox_planer_ort, 3, 3, 1, 1)
        self.label_137 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_137.setFont(font)
        self.label_137.setObjectName("label_137")
        self.gridLayout_12.addWidget(self.label_137, 6, 3, 1, 1)
        self.label_145 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_145.setFont(font)
        self.label_145.setObjectName("label_145")
        self.gridLayout_12.addWidget(self.label_145, 14, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_12.addWidget(self.lineEdit, 3, 0, 1, 1)
        self.label_80 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_80.setFont(font)
        self.label_80.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_80.setObjectName("label_80")
        self.gridLayout_12.addWidget(self.label_80, 0, 0, 1, 1)
        self.label_134 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_134.setFont(font)
        self.label_134.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_134.setObjectName("label_134")
        self.gridLayout_12.addWidget(self.label_134, 4, 0, 1, 1)
        self.label_140 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_140.setFont(font)
        self.label_140.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_140.setObjectName("label_140")
        self.gridLayout_12.addWidget(self.label_140, 8, 0, 1, 1)
        self.label_142 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_142.setFont(font)
        self.label_142.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_142.setObjectName("label_142")
        self.gridLayout_12.addWidget(self.label_142, 12, 0, 1, 1)
        self.label_146 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_146.setFont(font)
        self.label_146.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_146.setObjectName("label_146")
        self.gridLayout_12.addWidget(self.label_146, 16, 0, 1, 1)
        self.label_174 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_174.setFont(font)
        self.label_174.setObjectName("label_174")
        self.gridLayout_12.addWidget(self.label_174, 2, 0, 1, 1)
        self.label_175 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_175.setFont(font)
        self.label_175.setObjectName("label_175")
        self.gridLayout_12.addWidget(self.label_175, 6, 0, 1, 1)
        self.label_181 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_181.setFont(font)
        self.label_181.setObjectName("label_181")
        self.gridLayout_12.addWidget(self.label_181, 10, 0, 1, 1)
        self.label_182 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_182.setFont(font)
        self.label_182.setObjectName("label_182")
        self.gridLayout_12.addWidget(self.label_182, 14, 0, 1, 1)
        self.label_183 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_183.setFont(font)
        self.label_183.setObjectName("label_183")
        self.gridLayout_12.addWidget(self.label_183, 18, 0, 1, 1)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_3.addWidget(self.scrollArea_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 226, 432))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_154 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_154.setFont(font)
        self.label_154.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_154.setObjectName("label_154")
        self.gridLayout_13.addWidget(self.label_154, 15, 0, 1, 1)
        self.pushButton_blitzschutz = QtWidgets.QPushButton(self.scrollAreaWidgetContents_5)
        self.pushButton_blitzschutz.setObjectName("pushButton_blitzschutz")
        self.gridLayout_13.addWidget(self.pushButton_blitzschutz, 10, 0, 1, 1)
        self.pushButton_schema = QtWidgets.QPushButton(self.scrollAreaWidgetContents_5)
        self.pushButton_schema.setObjectName("pushButton_schema")
        self.gridLayout_13.addWidget(self.pushButton_schema, 7, 0, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.gridLayout_13.addWidget(self.label_45, 14, 0, 1, 1)
        self.checkBox_modulanortnung = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_modulanortnung.setText("")
        self.checkBox_modulanortnung.setObjectName("checkBox_modulanortnung")
        self.gridLayout_13.addWidget(self.checkBox_modulanortnung, 1, 1, 1, 1)
        self.pushButton_schema_steuerung = QtWidgets.QPushButton(self.scrollAreaWidgetContents_5)
        self.pushButton_schema_steuerung.setObjectName("pushButton_schema_steuerung")
        self.gridLayout_13.addWidget(self.pushButton_schema_steuerung, 13, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.gridLayout_13.addWidget(self.label_32, 11, 0, 1, 1)
        self.pushButton_schema_ueberwachung = QtWidgets.QPushButton(self.scrollAreaWidgetContents_5)
        self.pushButton_schema_ueberwachung.setObjectName("pushButton_schema_ueberwachung")
        self.gridLayout_13.addWidget(self.pushButton_schema_ueberwachung, 16, 0, 1, 1)
        self.label_152 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_152.setFont(font)
        self.label_152.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_152.setObjectName("label_152")
        self.gridLayout_13.addWidget(self.label_152, 6, 0, 1, 1)
        self.label_150 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_150.setFont(font)
        self.label_150.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_150.setObjectName("label_150")
        self.gridLayout_13.addWidget(self.label_150, 0, 0, 1, 1)
        self.checkBox_schema_ueberwachung = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_schema_ueberwachung.setText("")
        self.checkBox_schema_ueberwachung.setObjectName("checkBox_schema_ueberwachung")
        self.gridLayout_13.addWidget(self.checkBox_schema_ueberwachung, 16, 1, 1, 1)
        self.pushButton_moulanortnung = QtWidgets.QPushButton(self.scrollAreaWidgetContents_5)
        self.pushButton_moulanortnung.setObjectName("pushButton_moulanortnung")
        self.gridLayout_13.addWidget(self.pushButton_moulanortnung, 1, 0, 1, 1)
        self.checkBox_string = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_string.setText("")
        self.checkBox_string.setObjectName("checkBox_string")
        self.gridLayout_13.addWidget(self.checkBox_string, 4, 1, 1, 1)
        self.label_156 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_156.setFont(font)
        self.label_156.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_156.setObjectName("label_156")
        self.gridLayout_13.addWidget(self.label_156, 12, 0, 1, 1)
        self.label_153 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_153.setFont(font)
        self.label_153.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_153.setObjectName("label_153")
        self.gridLayout_13.addWidget(self.label_153, 9, 0, 1, 1)
        self.checkBox_blitzschutz = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_blitzschutz.setText("")
        self.checkBox_blitzschutz.setObjectName("checkBox_blitzschutz")
        self.gridLayout_13.addWidget(self.checkBox_blitzschutz, 10, 1, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_46.setText("")
        self.label_46.setObjectName("label_46")
        self.gridLayout_13.addWidget(self.label_46, 17, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.gridLayout_13.addWidget(self.label_24, 2, 0, 1, 1)
        self.label_151 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_151.setFont(font)
        self.label_151.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_151.setObjectName("label_151")
        self.gridLayout_13.addWidget(self.label_151, 3, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.gridLayout_13.addWidget(self.label_28, 8, 0, 1, 1)
        self.pushButton_string = QtWidgets.QPushButton(self.scrollAreaWidgetContents_5)
        self.pushButton_string.setObjectName("pushButton_string")
        self.gridLayout_13.addWidget(self.pushButton_string, 4, 0, 1, 1)
        self.checkBox_schema_steuerung = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_schema_steuerung.setText("")
        self.checkBox_schema_steuerung.setObjectName("checkBox_schema_steuerung")
        self.gridLayout_13.addWidget(self.checkBox_schema_steuerung, 13, 1, 1, 1)
        self.checkBox_schema = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_5)
        self.checkBox_schema.setText("")
        self.checkBox_schema.setObjectName("checkBox_schema")
        self.gridLayout_13.addWidget(self.checkBox_schema, 7, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.gridLayout_13.addWidget(self.label_27, 5, 0, 1, 1)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_4.addWidget(self.scrollArea_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.tab_6)
        self.scrollArea_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 276, 341))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_50 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_50.setText("")
        self.label_50.setObjectName("label_50")
        self.gridLayout_15.addWidget(self.label_50, 0, 0, 1, 1)
        self.pushButton_montage_sicherheit = QtWidgets.QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_montage_sicherheit.setObjectName("pushButton_montage_sicherheit")
        self.gridLayout_15.addWidget(self.pushButton_montage_sicherheit, 7, 0, 1, 1)
        self.label_159 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_159.setFont(font)
        self.label_159.setObjectName("label_159")
        self.gridLayout_15.addWidget(self.label_159, 6, 0, 1, 1)
        self.label_160 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_160.setFont(font)
        self.label_160.setObjectName("label_160")
        self.gridLayout_15.addWidget(self.label_160, 9, 0, 1, 1)
        self.label_155 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_155.setFont(font)
        self.label_155.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.label_155.setObjectName("label_155")
        self.gridLayout_15.addWidget(self.label_155, 1, 0, 1, 1)
        self.checkBox_datenblatt_sicherheit = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        self.checkBox_datenblatt_sicherheit.setText("")
        self.checkBox_datenblatt_sicherheit.setObjectName("checkBox_datenblatt_sicherheit")
        self.gridLayout_15.addWidget(self.checkBox_datenblatt_sicherheit, 10, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_15.addItem(spacerItem3, 14, 0, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_49.setText("")
        self.label_49.setObjectName("label_49")
        self.gridLayout_15.addWidget(self.label_49, 11, 0, 1, 1)
        self.pushButton_lageplan_sicherheit = QtWidgets.QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_lageplan_sicherheit.setObjectName("pushButton_lageplan_sicherheit")
        self.gridLayout_15.addWidget(self.pushButton_lageplan_sicherheit, 2, 0, 1, 1)
        self.label_157 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_157.setFont(font)
        self.label_157.setObjectName("label_157")
        self.gridLayout_15.addWidget(self.label_157, 3, 0, 1, 1)
        self.checkBox_pruefbuch_sicherheit = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        self.checkBox_pruefbuch_sicherheit.setText("")
        self.checkBox_pruefbuch_sicherheit.setObjectName("checkBox_pruefbuch_sicherheit")
        self.gridLayout_15.addWidget(self.checkBox_pruefbuch_sicherheit, 4, 1, 1, 1)
        self.label_158 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_158.setFont(font)
        self.label_158.setObjectName("label_158")
        self.gridLayout_15.addWidget(self.label_158, 12, 0, 1, 1)
        self.pushButton_pruefbuch_sicherheit = QtWidgets.QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_pruefbuch_sicherheit.setObjectName("pushButton_pruefbuch_sicherheit")
        self.gridLayout_15.addWidget(self.pushButton_pruefbuch_sicherheit, 4, 0, 1, 1)
        self.checkBox_montage_sicherheit = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        self.checkBox_montage_sicherheit.setText("")
        self.checkBox_montage_sicherheit.setObjectName("checkBox_montage_sicherheit")
        self.gridLayout_15.addWidget(self.checkBox_montage_sicherheit, 7, 1, 1, 1)
        self.checkBox_ertragsb_sicherheit = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        self.checkBox_ertragsb_sicherheit.setText("")
        self.checkBox_ertragsb_sicherheit.setObjectName("checkBox_ertragsb_sicherheit")
        self.gridLayout_15.addWidget(self.checkBox_ertragsb_sicherheit, 13, 1, 1, 1)
        self.pushButton_ertragsb_sicherheit = QtWidgets.QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_ertragsb_sicherheit.setObjectName("pushButton_ertragsb_sicherheit")
        self.gridLayout_15.addWidget(self.pushButton_ertragsb_sicherheit, 13, 0, 1, 1)
        self.pushButton_datenblatt_sicherheit = QtWidgets.QPushButton(self.scrollAreaWidgetContents_7)
        self.pushButton_datenblatt_sicherheit.setObjectName("pushButton_datenblatt_sicherheit")
        self.gridLayout_15.addWidget(self.pushButton_datenblatt_sicherheit, 10, 0, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_47.setText("")
        self.label_47.setObjectName("label_47")
        self.gridLayout_15.addWidget(self.label_47, 5, 0, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_48.setText("")
        self.label_48.setObjectName("label_48")
        self.gridLayout_15.addWidget(self.label_48, 8, 0, 1, 1)
        self.checkBox_lageplan_sicherheit = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_7)
        self.checkBox_lageplan_sicherheit.setText("")
        self.checkBox_lageplan_sicherheit.setObjectName("checkBox_lageplan_sicherheit")
        self.gridLayout_15.addWidget(self.checkBox_lageplan_sicherheit, 2, 1, 1, 1)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_7)
        self.gridLayout_8.addWidget(self.scrollArea_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.scrollArea_7 = QtWidgets.QScrollArea(self.tab_7)
        self.scrollArea_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 267, 1149))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_9)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_230 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_230.setText("")
        self.label_230.setObjectName("label_230")
        self.gridLayout_10.addWidget(self.label_230, 32, 0, 1, 1)
        self.checkBox_37 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_37.setText("")
        self.checkBox_37.setObjectName("checkBox_37")
        self.gridLayout_10.addWidget(self.checkBox_37, 37, 1, 1, 1)
        self.checkBox_41 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_41.setText("")
        self.checkBox_41.setObjectName("checkBox_41")
        self.gridLayout_10.addWidget(self.checkBox_41, 46, 1, 1, 1)
        self.label_179 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_179.setFont(font)
        self.label_179.setObjectName("label_179")
        self.gridLayout_10.addWidget(self.label_179, 39, 0, 1, 1)
        self.label_169 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_169.setFont(font)
        self.label_169.setObjectName("label_169")
        self.gridLayout_10.addWidget(self.label_169, 0, 0, 1, 1)
        self.checkBox_grundbuchauszug = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_grundbuchauszug.setText("")
        self.checkBox_grundbuchauszug.setObjectName("checkBox_grundbuchauszug")
        self.gridLayout_10.addWidget(self.checkBox_grundbuchauszug, 9, 1, 1, 1)
        self.checkBox_anmeldung_pronovo = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_anmeldung_pronovo.setText("")
        self.checkBox_anmeldung_pronovo.setObjectName("checkBox_anmeldung_pronovo")
        self.gridLayout_10.addWidget(self.checkBox_anmeldung_pronovo, 2, 1, 1, 1)
        self.checkBox_grundeigentmer = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_grundeigentmer.setText("")
        self.checkBox_grundeigentmer.setObjectName("checkBox_grundeigentmer")
        self.gridLayout_10.addWidget(self.checkBox_grundeigentmer, 6, 1, 1, 1)
        self.label_168 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_168.setFont(font)
        self.label_168.setObjectName("label_168")
        self.gridLayout_10.addWidget(self.label_168, 24, 0, 1, 1)
        self.label_130 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_130.setText("")
        self.label_130.setObjectName("label_130")
        self.gridLayout_10.addWidget(self.label_130, 13, 0, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_10.addWidget(self.pushButton_25, 46, 0, 1, 1)
        self.checkBox_beglaubigung_pronovo = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_beglaubigung_pronovo.setText("")
        self.checkBox_beglaubigung_pronovo.setObjectName("checkBox_beglaubigung_pronovo")
        self.gridLayout_10.addWidget(self.checkBox_beglaubigung_pronovo, 12, 1, 1, 1)
        self.checkBox_meldeformular = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_meldeformular.setText("")
        self.checkBox_meldeformular.setObjectName("checkBox_meldeformular")
        self.gridLayout_10.addWidget(self.checkBox_meldeformular, 25, 1, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_10.addWidget(self.pushButton_30, 40, 0, 1, 1)
        self.checkBox_39 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_39.setText("")
        self.checkBox_39.setObjectName("checkBox_39")
        self.gridLayout_10.addWidget(self.checkBox_39, 34, 1, 1, 1)
        self.label_228 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_228.setText("")
        self.label_228.setObjectName("label_228")
        self.gridLayout_10.addWidget(self.label_228, 26, 0, 1, 1)
        self.checkBox_plan_ESTI = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_plan_ESTI.setText("")
        self.checkBox_plan_ESTI.setObjectName("checkBox_plan_ESTI")
        self.gridLayout_10.addWidget(self.checkBox_plan_ESTI, 19, 1, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_10.addWidget(self.pushButton_26, 53, 0, 1, 1)
        self.label_128 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_128.setText("")
        self.label_128.setObjectName("label_128")
        self.gridLayout_10.addWidget(self.label_128, 7, 0, 1, 1)
        self.label_231 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_231.setText("")
        self.label_231.setObjectName("label_231")
        self.gridLayout_10.addWidget(self.label_231, 35, 0, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_10.addWidget(self.pushButton_17, 34, 0, 1, 1)
        self.pushButton_meldeformular = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_meldeformular.setObjectName("pushButton_meldeformular")
        self.gridLayout_10.addWidget(self.pushButton_meldeformular, 25, 0, 1, 1)
        self.label_177 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_177.setFont(font)
        self.label_177.setObjectName("label_177")
        self.gridLayout_10.addWidget(self.label_177, 49, 0, 1, 1)
        self.checkBox_baubewilligung = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_baubewilligung.setText("")
        self.checkBox_baubewilligung.setObjectName("checkBox_baubewilligung")
        self.gridLayout_10.addWidget(self.checkBox_baubewilligung, 28, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_10.addWidget(self.pushButton_16, 31, 0, 1, 1)
        self.checkBox_44 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_44.setText("")
        self.checkBox_44.setObjectName("checkBox_44")
        self.gridLayout_10.addWidget(self.checkBox_44, 31, 1, 1, 1)
        self.pushButton_fertigstellung_ESTI = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_fertigstellung_ESTI.setObjectName("pushButton_fertigstellung_ESTI")
        self.gridLayout_10.addWidget(self.pushButton_fertigstellung_ESTI, 22, 0, 1, 1)
        self.label_167 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_167.setFont(font)
        self.label_167.setObjectName("label_167")
        self.gridLayout_10.addWidget(self.label_167, 18, 0, 1, 1)
        self.label_232 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_232.setText("")
        self.label_232.setObjectName("label_232")
        self.gridLayout_10.addWidget(self.label_232, 38, 0, 1, 1)
        self.label_226 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_226.setText("")
        self.label_226.setObjectName("label_226")
        self.gridLayout_10.addWidget(self.label_226, 20, 0, 1, 1)
        self.pushButton_TAG = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_TAG.setObjectName("pushButton_TAG")
        self.gridLayout_10.addWidget(self.pushButton_TAG, 16, 0, 1, 1)
        self.pushButton_baubewilligung = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_baubewilligung.setObjectName("pushButton_baubewilligung")
        self.gridLayout_10.addWidget(self.pushButton_baubewilligung, 28, 0, 1, 1)
        self.pushButton_grundeigentmer = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_grundeigentmer.sizePolicy().hasHeightForWidth())
        self.pushButton_grundeigentmer.setSizePolicy(sizePolicy)
        self.pushButton_grundeigentmer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_grundeigentmer.setObjectName("pushButton_grundeigentmer")
        self.gridLayout_10.addWidget(self.pushButton_grundeigentmer, 6, 0, 1, 1)
        self.label_172 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_172.setFont(font)
        self.label_172.setObjectName("label_172")
        self.gridLayout_10.addWidget(self.label_172, 14, 0, 1, 1)
        self.label_178 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_178.setFont(font)
        self.label_178.setObjectName("label_178")
        self.gridLayout_10.addWidget(self.label_178, 36, 0, 1, 1)
        self.checkBox_38 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_38.setText("")
        self.checkBox_38.setObjectName("checkBox_38")
        self.gridLayout_10.addWidget(self.checkBox_38, 40, 1, 1, 1)
        self.checkBox_42 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_42.setText("")
        self.checkBox_42.setObjectName("checkBox_42")
        self.gridLayout_10.addWidget(self.checkBox_42, 50, 1, 1, 1)
        self.label_162 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_162.setFont(font)
        self.label_162.setObjectName("label_162")
        self.gridLayout_10.addWidget(self.label_162, 8, 0, 1, 1)
        self.label_131 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_131.setText("")
        self.label_131.setObjectName("label_131")
        self.gridLayout_10.addWidget(self.label_131, 17, 0, 1, 1)
        self.label_163 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_163.setFont(font)
        self.label_163.setObjectName("label_163")
        self.gridLayout_10.addWidget(self.label_163, 33, 0, 1, 1)
        self.label_166 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_166.setFont(font)
        self.label_166.setObjectName("label_166")
        self.gridLayout_10.addWidget(self.label_166, 11, 0, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_10.addWidget(self.pushButton_29, 37, 0, 1, 1)
        self.label_233 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_233.setText("")
        self.label_233.setObjectName("label_233")
        self.gridLayout_10.addWidget(self.label_233, 41, 0, 1, 1)
        self.checkBox_43 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_43.setText("")
        self.checkBox_43.setObjectName("checkBox_43")
        self.gridLayout_10.addWidget(self.checkBox_43, 53, 1, 1, 1)
        self.label_173 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_173.setFont(font)
        self.label_173.setObjectName("label_173")
        self.gridLayout_10.addWidget(self.label_173, 45, 0, 1, 1)
        self.label_237 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_237.setText("")
        self.label_237.setObjectName("label_237")
        self.gridLayout_10.addWidget(self.label_237, 48, 0, 1, 1)
        self.label_165 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_165.setFont(font)
        self.label_165.setObjectName("label_165")
        self.gridLayout_10.addWidget(self.label_165, 30, 0, 1, 1)
        self.pushButton_anmeldung_pronovo = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_anmeldung_pronovo.sizePolicy().hasHeightForWidth())
        self.pushButton_anmeldung_pronovo.setSizePolicy(sizePolicy)
        self.pushButton_anmeldung_pronovo.setObjectName("pushButton_anmeldung_pronovo")
        self.gridLayout_10.addWidget(self.pushButton_anmeldung_pronovo, 2, 0, 1, 1)
        self.label_235 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_235.setText("")
        self.label_235.setObjectName("label_235")
        self.gridLayout_10.addWidget(self.label_235, 51, 0, 1, 1)
        self.checkBox_40 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_40.setText("")
        self.checkBox_40.setObjectName("checkBox_40")
        self.gridLayout_10.addWidget(self.checkBox_40, 43, 1, 1, 1)
        self.pushButton_beglaubigung_pronovo = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_beglaubigung_pronovo.setObjectName("pushButton_beglaubigung_pronovo")
        self.gridLayout_10.addWidget(self.pushButton_beglaubigung_pronovo, 12, 0, 1, 1)
        self.label_234 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_234.setText("")
        self.label_234.setObjectName("label_234")
        self.gridLayout_10.addWidget(self.label_234, 44, 0, 1, 1)
        self.label_176 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_176.setFont(font)
        self.label_176.setObjectName("label_176")
        self.gridLayout_10.addWidget(self.label_176, 42, 0, 1, 1)
        self.pushButton_plan_ESTI = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_plan_ESTI.setObjectName("pushButton_plan_ESTI")
        self.gridLayout_10.addWidget(self.pushButton_plan_ESTI, 19, 0, 1, 1)
        self.label_129 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_129.setText("")
        self.label_129.setObjectName("label_129")
        self.gridLayout_10.addWidget(self.label_129, 10, 0, 1, 1)
        self.checkBox_fertigstellung_ESTI = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_fertigstellung_ESTI.setText("")
        self.checkBox_fertigstellung_ESTI.setObjectName("checkBox_fertigstellung_ESTI")
        self.gridLayout_10.addWidget(self.checkBox_fertigstellung_ESTI, 22, 1, 1, 1)
        self.label_227 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_227.setText("")
        self.label_227.setObjectName("label_227")
        self.gridLayout_10.addWidget(self.label_227, 23, 0, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout_10.addWidget(self.pushButton_32, 50, 0, 1, 1)
        self.pushButton_grundbuchauszug = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_grundbuchauszug.setObjectName("pushButton_grundbuchauszug")
        self.gridLayout_10.addWidget(self.pushButton_grundbuchauszug, 9, 0, 1, 1)
        self.label_171 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_171.setFont(font)
        self.label_171.setObjectName("label_171")
        self.gridLayout_10.addWidget(self.label_171, 21, 0, 1, 1)
        self.label_180 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_180.setFont(font)
        self.label_180.setObjectName("label_180")
        self.gridLayout_10.addWidget(self.label_180, 52, 0, 1, 1)
        self.label_164 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_164.setFont(font)
        self.label_164.setObjectName("label_164")
        self.gridLayout_10.addWidget(self.label_164, 27, 0, 1, 1)
        self.checkBox_TAG = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_9)
        self.checkBox_TAG.setText("")
        self.checkBox_TAG.setObjectName("checkBox_TAG")
        self.gridLayout_10.addWidget(self.checkBox_TAG, 16, 1, 1, 1)
        self.label_229 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_229.setText("")
        self.label_229.setObjectName("label_229")
        self.gridLayout_10.addWidget(self.label_229, 29, 0, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_10.addWidget(self.pushButton_31, 43, 0, 1, 1)
        self.label_170 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_170.setFont(font)
        self.label_170.setObjectName("label_170")
        self.gridLayout_10.addWidget(self.label_170, 5, 0, 1, 1)
        self.label_127 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_127.setText("")
        self.label_127.setObjectName("label_127")
        self.gridLayout_10.addWidget(self.label_127, 4, 0, 1, 1)
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_9)
        self.gridLayout_9.addWidget(self.scrollArea_7, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea_merge = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea_merge.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea_merge.setWidgetResizable(True)
        self.scrollArea_merge.setObjectName("scrollArea_merge")
        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 255, 141))
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_10)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.pushButton_merge = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_merge.sizePolicy().hasHeightForWidth())
        self.pushButton_merge.setSizePolicy(sizePolicy)
        self.pushButton_merge.setObjectName("pushButton_merge")
        self.gridLayout_14.addWidget(self.pushButton_merge, 4, 1, 1, 1)
        self.pushButton_saveto = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_saveto.sizePolicy().hasHeightForWidth())
        self.pushButton_saveto.setSizePolicy(sizePolicy)
        self.pushButton_saveto.setObjectName("pushButton_saveto")
        self.gridLayout_14.addWidget(self.pushButton_saveto, 0, 2, 1, 1)
        self.pushButton_reset = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_reset.sizePolicy().hasHeightForWidth())
        self.pushButton_reset.setSizePolicy(sizePolicy)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.gridLayout_14.addWidget(self.pushButton_reset, 4, 2, 1, 1)
        self.pushButton_delet = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_delet.sizePolicy().hasHeightForWidth())
        self.pushButton_delet.setSizePolicy(sizePolicy)
        self.pushButton_delet.setObjectName("pushButton_delet")
        self.gridLayout_14.addWidget(self.pushButton_delet, 4, 0, 1, 1)
        self.lineEdit_saveto = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        self.lineEdit_saveto.setObjectName("lineEdit_saveto")
        self.gridLayout_14.addWidget(self.lineEdit_saveto, 0, 0, 1, 2)
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_10)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_14.addWidget(self.listWidget, 1, 0, 1, 3)
        self.scrollArea_merge.setWidget(self.scrollAreaWidgetContents_10)
        self.gridLayout_5.addWidget(self.scrollArea_merge, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 63, 16))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_8)
        self.gridLayout_6.addWidget(self.scrollArea_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 3)
        self.label = QtWidgets.QLabel(Form)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 75 20pt \"Century Gothic\";\n"
"color: rgb(241, 180, 52);")
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(-1)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label.raise_()
        self.tabWidget.raise_()
        self.label_29.raise_()

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "Kunde"))
        self.label_13.setText(_translate("Form", "kWp Leistung"))
        self.label_8.setText(_translate("Form", "Strasse & Nr."))
        self.label_5.setText(_translate("Form", "PLZ"))
        self.label_16.setText(_translate("Form", "Inbetriebnahme:"))
        self.label_4.setText(_translate("Form", "Nachname"))
        self.label_14.setText(_translate("Form", "Bauphase von:"))
        self.label_30.setText(_translate("Form", "Sprache"))
        self.label_25.setText(_translate("Form", "kVA Leistung "))
        self.groupBox_DragDrop.setTitle(_translate("Form", "Drag and Drop"))
        self.label_10.setText(_translate("Form", "hier auch aurichten, fenster genau gleich wie titelbild"))
        self.checkBox_objekt.setText(_translate("Form", "Objekt"))
        self.label_11.setText(_translate("Form", "Ort"))
        self.label_17.setText(_translate("Form", "bis:"))
        self.label_7.setText(_translate("Form", "Ort"))
        self.label_3.setText(_translate("Form", "Vor- oder Firmenname"))
        self.label_18.setText(_translate("Form", "PLZ"))
        self.label_12.setText(_translate("Form", "Strasse & Nr."))
        self.label_15.setText(_translate("Form", "kWh Leistung"))
        self.label_26.setText(_translate("Form", "m2 Feldgrösse"))
        self.pushButton_PDF.setText(_translate("Form", "PDF Zusammenfügen"))
        self.pushButton_speichern.setText(_translate("Form", "Zwischenpeichern"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Kunde"))
        self.label_70.setText(_translate("Form", "Unterkonstruktion"))
        self.label_44.setText(_translate("Form", "Leistungsregler"))
        self.label_42.setText(_translate("Form", "Typ"))
        self.label_69.setText(_translate("Form", "Überspannungsschutz"))
        self.label_65.setText(_translate("Form", "Ladestation"))
        self.label_33.setText(_translate("Form", "Typ"))
        self.label_72.setText(_translate("Form", "Sensoren"))
        self.label_66.setText(_translate("Form", "Typ"))
        self.label_75.setText(_translate("Form", "Batterie"))
        self.label_40.setText(_translate("Form", "Typ"))
        self.label_36.setText(_translate("Form", "Wechselrichter"))
        self.label_64.setText(_translate("Form", "Anzeigetafeln / Moniitoren"))
        self.label_41.setText(_translate("Form", "Anlageüberwachung"))
        self.label_39.setText(_translate("Form", "Leistungsoptimierer"))
        self.pushButton_unterkonberechnung.setText(_translate("Form", "Computer Durchsuchen"))
        self.label_34.setText(_translate("Form", "Solarmodule"))
        self.label_37.setText(_translate("Form", "Zähler"))
        self.label_71.setText(_translate("Form", "Typ"))
        self.label_38.setText(_translate("Form", "Typ"))
        self.label_68.setText(_translate("Form", "Typ"))
        self.label_74.setText(_translate("Form", "Typ"))
        self.label_161.setText(_translate("Form", "Berechnungen Unterkonstruktion"))
        self.label_43.setText(_translate("Form", "Typ"))
        self.label_35.setText(_translate("Form", "Typ"))
        self.label_67.setText(_translate("Form", "Typ"))
        self.label_73.setText(_translate("Form", "Typ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab2), _translate("Form", "Anlage"))
        self.label_138.setText(_translate("Form", "PLZ"))
        self.label_144.setText(_translate("Form", "Ort"))
        self.label_149.setText(_translate("Form", "Ort"))
        self.label_135.setText(_translate("Form", "Strasse & Nr."))
        self.label_147.setText(_translate("Form", "PLZ"))
        self.label_141.setText(_translate("Form", "Ort"))
        self.label_148.setText(_translate("Form", "Strasse & Nr."))
        self.label_133.setText(_translate("Form", "Ort"))
        self.label_139.setText(_translate("Form", "Strasse & Nr."))
        self.label_79.setText(_translate("Form", "PLZ"))
        self.label_132.setText(_translate("Form", "Strasse & Nr."))
        self.label_143.setText(_translate("Form", "PLZ"))
        self.label_136.setText(_translate("Form", "PLZ"))
        self.label_137.setText(_translate("Form", "Ort"))
        self.label_145.setText(_translate("Form", "Strasse & Nr."))
        self.label_80.setText(_translate("Form", "Planer"))
        self.label_134.setText(_translate("Form", "PV-Installateur"))
        self.label_140.setText(_translate("Form", "Elektroinstallateur"))
        self.label_142.setText(_translate("Form", "ABS-Installateur"))
        self.label_146.setText(_translate("Form", "Gerüstebauer"))
        self.label_174.setText(_translate("Form", "Name"))
        self.label_175.setText(_translate("Form", "Name"))
        self.label_181.setText(_translate("Form", "Name"))
        self.label_182.setText(_translate("Form", "Name"))
        self.label_183.setText(_translate("Form", "Name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Unternehmen"))
        self.label_154.setText(_translate("Form", "Schema Anlageüberwachung"))
        self.pushButton_blitzschutz.setText(_translate("Form", "Computer Durchsuchen"))
        self.pushButton_schema.setText(_translate("Form", "Computer Durchsuchen"))
        self.pushButton_schema_steuerung.setText(_translate("Form", "Computer Durchsuchen"))
        self.pushButton_schema_ueberwachung.setText(_translate("Form", "Computer Durchsuchen"))
        self.label_152.setText(_translate("Form", "Schemas"))
        self.label_150.setText(_translate("Form", "Modulanortnung"))
        self.pushButton_moulanortnung.setText(_translate("Form", "Computer Durchsuchen"))
        self.label_156.setText(_translate("Form", "Schema sonstige Steuerungen"))
        self.label_153.setText(_translate("Form", "Blitzschutzplan"))
        self.label_151.setText(_translate("Form", "String-Plan"))
        self.pushButton_string.setText(_translate("Form", "Computer Durchsuchen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Plände"))
        self.pushButton_montage_sicherheit.setText(_translate("Form", "Computer Durchsuchen"))
        self.label_159.setText(_translate("Form", "Montagedokumentation"))
        self.label_160.setText(_translate("Form", "Datenblatt Sicherheitssystem"))
        self.label_155.setText(_translate("Form", "Lageplan der Sicherheitseinrichtungen"))
        self.pushButton_lageplan_sicherheit.setText(_translate("Form", "Computer Durchsuchen"))
        self.label_157.setText(_translate("Form", "Prüfbuch Sicherheitssystem"))
        self.label_158.setText(_translate("Form", "Ertragsberechnung"))
        self.pushButton_pruefbuch_sicherheit.setText(_translate("Form", "Computer Durchsuchen"))
        self.pushButton_ertragsb_sicherheit.setText(_translate("Form", "Computer Durchsuchen"))
        self.pushButton_datenblatt_sicherheit.setText(_translate("Form", "Computer Durchsuchen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "ABS"))
        self.label_179.setText(_translate("Form", "MPP DC"))
        self.label_169.setText(_translate("Form", "Anmeldung Pronovo"))
        self.label_168.setText(_translate("Form", "Meldeformular Solaranlage"))
        self.pushButton_25.setText(_translate("Form", "Computer Durchsuchen"))
        self.pushButton_30.setText(_translate("Form", "Computer Durchsuchen"))
        self.pushButton_26.setText(_translate("Form", "Computer Durchsuchen"))
        self.pushButton_17.setText(_translate("Form", "Computer Durchsuchen"))
        self.pushButton_meldeformular.setText(_translate("Form", "Computer Durchsuchen"))
        self.label_177.setText(_translate("Form", "Stückprüfprotokoll Verteilungen"))
        self.pushButton_16.setText(_translate("Form", "Computer Durchsuchen"))
        self.pushButton_fertigstellung_ESTI.setText(_translate("Form", "Computer Durchsuchen"))
        self.label_167.setText(_translate("Form", "Plangenehmigung ESTI"))
        self.pushButton_TAG.setText(_translate("Form", "Computer Durchsuchen"))
        self.pushButton_baubewilligung.setText(_translate("Form", "Computer Durchsuchen"))
        self.pushButton_grundeigentmer.setText(_translate("Form", "Computer Durchsuchen"))
        self.label_172.setText(_translate("Form", "Technisches Anschlussgesuch Netzbetreiber"))
        self.label_178.setText(_translate("Form", "MPP AC"))
        self.label_162.setText(_translate("Form", "Grundbuchauszug"))
        self.label_163.setText(_translate("Form", "SiNa AC"))
        self.label_166.setText(_translate("Form", "Beglaubigung Pronovo"))
        self.pushButton_29.setText(_translate("Form", "Computer Durchsuchen"))
        self.label_173.setText(_translate("Form", "Stückprüfprotokoll GAK"))
        self.label_165.setText(_translate("Form", "Inbetriebnahmeprotokoll"))
        self.pushButton_anmeldung_pronovo.setText(_translate("Form", "Computer Durchsuchen"))
        self.pushButton_beglaubigung_pronovo.setText(_translate("Form", "Computer Durchsuchen"))
        self.label_176.setText(_translate("Form", "VNB Abnahmeprotokoll"))
        self.pushButton_plan_ESTI.setText(_translate("Form", "Computer Durchsuchen"))
        self.pushButton_32.setText(_translate("Form", "Computer Durchsuchen"))
        self.pushButton_grundbuchauszug.setText(_translate("Form", "Computer Durchsuchen"))
        self.label_171.setText(_translate("Form", "Fertigstellungsanzeige ESTI"))
        self.label_180.setText(_translate("Form", "Abnahmeprotokoll"))
        self.label_164.setText(_translate("Form", "Dokumente Baubewilligung"))
        self.pushButton_31.setText(_translate("Form", "Computer Durchsuchen"))
        self.label_170.setText(_translate("Form", "Zustimmung Grundeigentümer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Form", "Administration"))
        self.pushButton_merge.setText(_translate("Form", "Merge"))
        self.pushButton_saveto.setText(_translate("Form", "Save To"))
        self.pushButton_reset.setText(_translate("Form", "Reset"))
        self.pushButton_delet.setText(_translate("Form", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Sortieren"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Einstellungen"))
        self.label.setText(_translate("Form", " PV-Anlagen-Generator"))
        
        
                ###nachträglich###
        ##direkt einfügen oben
        #self.dateEdit_bis = QtWidgets.QDateEdit(, calendarPopup=True)
        #self.dateEdit_von = QtWidgets.QDateEdit(calendarPopup=True)
        #self.dateEdit_inbetriebnahme = QtWidgets.QDateEdit(calendarPopup=True)
        
        #nur eingabe von zahlen möglich
        self.lineEdit_plz.setValidator(QIntValidator())
        self.lineEdit_plzobjekt.setValidator(QIntValidator())
        self.lineEdit_geruste_plz.setValidator(QIntValidator())
        self.lineEdit_abs_plz.setValidator(QIntValidator())
        self.lineEdit_planer_plz.setValidator(QIntValidator())
        self.lineEdit_pv_plz.setValidator(QIntValidator())
        self.lineEdit_elektroin_plz.setValidator(QIntValidator())
        self.lineEdit_kwp.setValidator(QIntValidator())
        self.lineEdit_kva.setValidator(QIntValidator())
        self.lineEdit_kwh.setValidator(QIntValidator())
        self.lineEdit_m2.setValidator(QIntValidator())
        
        #alleinstehende comboBox befüllen
        self.comboBox_sprache.addItems(["DE", "FR", "EN"])
        
        #informationen abfragen
        self.pushButton_PDF.clicked.connect(self.clicked)
        #self.uebertragen.clicked.connect(self.datenblaetter)
        
        
        
  
       
        
    ####Befüllung####        
                
        mainLayout = QHBoxLayout()
        
        self.model_modul = QStandardItemModel()
        self.comboBox_modul.setModel(self.model_modul)
        self.comboBox_modultyp.setModel(self.model_modul)
        
        self.model_wr = QStandardItemModel()
        self.comboBox_wr.setModel(self.model_wr)
        self.comboBox_wrtyp.setModel(self.model_wr)

        self.model_leistungso = QStandardItemModel()
        self.comboBox_leistungso.setModel(self.model_leistungso)
        self.comboBox_leistungsotyp.setModel(self.model_leistungso)

        self.model_zahler = QStandardItemModel()
        self.comboBox_zahler.setModel(self.model_zahler)
        self.comboBox_zahlertyp.setModel(self.model_zahler)
        
        self.model_uberwach = QStandardItemModel()
        self.comboBox_uberwach.setModel(self.model_uberwach)
        self.comboBox_uberwachtyp.setModel(self.model_uberwach)
        
        self.model_leistungsr = QStandardItemModel()
        self.comboBox_leistungsr.setModel(self.model_leistungsr)
        self.comboBox_leistungsrtyp.setModel(self.model_leistungsr)
        
        self.model_ladest = QStandardItemModel()
        self.comboBox_ladest.setModel(self.model_ladest)
        self.comboBox_lasttyp.setModel(self.model_ladest)
        
        self.model_batterie = QStandardItemModel()
        self.comboBox_batterie.setModel(self.model_batterie)
        self.comboBox_batterietyp.setModel(self.model_batterie)
        
        self.model_unterkon = QStandardItemModel()
        self.comboBox_unterkon.setModel(self.model_unterkon)
        self.comboBox_unterkontyp.setModel(self.model_unterkon)
        
        self.model_gak = QStandardItemModel()
        self.comboBox_gak.setModel(self.model_gak)
        self.comboBox_gaktyp.setModel(self.model_gak)
        
        self.model_anzeigeta = QStandardItemModel()
        self.comboBox_anzeigeta.setModel(self.model_anzeigeta)
        self.comboBox_anzeigetaftyp.setModel(self.model_anzeigeta)
        
        self.model_sensor = QStandardItemModel()
        self.comboBox_sensor.setModel(self.model_sensor)
        self.comboBox_sensortyp.setModel(self.model_sensor)
        
        
        a1 = self.comboBox_modul
        a2 = self.comboBox_wr
        a3 = self.comboBox_leistungso
        a4 = self.comboBox_zahler
        a5 = self.comboBox_uberwach
        a6 = self.comboBox_leistungsr
        a7 = self.comboBox_ladest
        a8 = self.comboBox_batterie
        a9 = self.comboBox_unterkon
        b1 = self.comboBox_gak
        b2 = self.comboBox_anzeigeta
        b3 = self.comboBox_sensor


        def comboBox_füllen(a, c, m, hh): 
            for k, v in a.items():
                marken = QStandardItem(k)
                m.appendRow(marken)
                for value in v:
                    typ = QStandardItem(value)
                    marken.appendRow(typ)

            c.currentIndexChanged.connect(hh)
            hh(0)

        comboBox_füllen(data_sol, a1, self.model_modul, self.update_modul)    
        comboBox_füllen(data_wr, a2, self.model_wr, self.update_wr)
        comboBox_füllen(data_leist_o, a3, self.model_leistungso, self.update_leistungso)    
        comboBox_füllen(data_zeh, a4, self.model_zahler, self.update_zahler)
        comboBox_füllen(data_anlage, a5, self.model_uberwach, self.update_uberwach)    
        comboBox_füllen(data_leist_r, a6, self.model_leistungsr, self.update_leistungsr)
        comboBox_füllen(data_lade, a7, self.model_ladest, self.update_ladest)    
        comboBox_füllen(data_batt, a8, self.model_batterie, self.update_batterie)
        comboBox_füllen(data_unterkon, a9, self.model_unterkon, self.update_unterkon)    
        comboBox_füllen(data_ueberspan, b1, self.model_gak, self.update_gak)
        comboBox_füllen(data_anzeiget, b2, self.model_anzeigeta, self.update_anzeigeta)    
        comboBox_füllen(data_sens, b3, self.model_sensor, self.update_sensor)

     
        sp0 = self.comboBox_sprache.currentText()
        for i in sp0:
            if i == 'DE':
                mo = monateDE
                sp = 0
                objekt = 'Objekt'
                #def_wr = xlsx_listeg[int(listen_nr[0])][1:10:3]
            elif i == 'FR':
                mo = monateFR
                sp = 1
                objekt = 'objet'
                #def_wr = xlsx_listeg[int(listen_nr[0])][2:10:3]
            elif i == 'EN':
                mo = monateEN
                sp = 2
                objekt = 'object'
                #def_wr = xlsx_listeg[int(listen_nr[0])][3:10:3]
            else:
                mo = monateDE
                sp = 0
                objekt = 'Objekt'
                #def_wr = xlsx_listeg[int(listen_nr[0])][1:10:3]
                ###else ist nur weill alles andere momentan nicht geht


        #Kunde:

        #w1 = self
        w2 = self.lineEdit_name.text()
        w3 = self.lineEdit_nachname.text()
        w4 = self.lineEdit_strasse.text()
        w5 = self.lineEdit_plz.text()
        w6 = self.lineEdit_ort_2.text()
        w7 = self.lineEdit_strasseobjekt.text()
        w8 = self.lineEdit_plzobjekt.text()
        w9 = self.lineEdit_ortobjekt_2.text()
        w10 = self.lineEdit_m2.text()
        w11 = self.lineEdit_kwp.text()
        w12 = self.lineEdit_kva.text()
        w13 = self.lineEdit_kwh.text()

        date1 = self.dateEdit_inbetriebnahme.text()
        ap1=str(date1)
        ap2=ap1.split('.')
        dateM = mo[int(ap2[1])]

        #Anlage:
        m1 = self.comboBox_modul.currentText()
        m2 = self.comboBox_modultyp.currentText()
        m3 = self.comboBox_wr.currentText()
        m4 = self.comboBox_wrtyp.currentText()
        m5 = self.comboBox_leistungso.currentText()
        m6 = self.comboBox_leistungsotyp.currentText()
        m7 = self.comboBox_zahler.currentText()
        m8 = self.comboBox_zahlertyp.currentText()
        m9 = self.comboBox_uberwach.currentText()
        m10 = self.comboBox_uberwachtyp.currentText()
        m11 = self.comboBox_leistungsr.currentText()
        m12 = self.comboBox_leistungsrtyp.currentText()
        m13 = self.comboBox_ladest.currentText()
        m14 = self.comboBox_lasttyp.currentText()
        m15 = self.comboBox_batterie.currentText()
        m16 = self.comboBox_batterietyp.currentText()
        m17 = self.comboBox_unterkon.currentText()
        m18 = self.comboBox_unterkontyp.currentText()
        m19 = self.comboBox_gak.currentText()
        m20 = self.comboBox_gaktyp.currentText()
        m21 = self.comboBox_anzeigeta.currentText()
        m22 = self.comboBox_anzeigetaftyp.currentText()
        m23 = self.comboBox_sensor.currentText()
        m24 = self.comboBox_sensortyp.currentText()

        

        #Unternehmen:
        u1 = self.lineEdit.text()
        u2 = self.lineEdit_planer_strasse.text()
        u3 = self.lineEdit_planer_plz.text()
        u4 = self.comboBox_planer_ort.currentText()
        u5 = self.lineEdit_2.text()
        u6 = self.lineEdit_pv_strasse.text()
        u7 = self.lineEdit_pv_plz.text()
        u8 = self.comboBox_pv_ort.currentText()
        u9 = self.lineEdit_3.text()
        u10 = self.lineEdit_elektroin_strasse.text()
        u11 = self.lineEdit_elektroin_plz.text()
        u12 = self.comboBox_elektroin_ort.currentText()
        u13 = self.lineEdit_4.text()
        u14 = self.lineEdit_abs_strasse.text()
        u15 = self.lineEdit_abs_plz.text()
        u16 = self.comboBox_abs_ort.currentText()
        u17 = self.lineEdit_5.text()
        u18 = self.lineEdit_Geruste_strasse.text()
        u19 = self.lineEdit_geruste_plz.text()
        u20 = self.comboBox_geruste_ort.currentText()

    
    
    
    
    
      
        
        
        
        
    
    def update_modul(self, index):
        indx = self.model_modul.index(index, 0, self.comboBox_modul.rootModelIndex())
        self.comboBox_modultyp.setRootModelIndex(indx)
        self.comboBox_modultyp.setCurrentIndex(0)
        
    def update_wr(self, index):
        indx = self.model_wr.index(index, 0, self.comboBox_wr.rootModelIndex())
        self.comboBox_wrtyp.setRootModelIndex(indx)
        self.comboBox_wrtyp.setCurrentIndex(0)

    def update_leistungso(self, index):
        indx = self.model_leistungso.index(index, 0, self.comboBox_leistungso.rootModelIndex())
        self.comboBox_leistungsotyp.setRootModelIndex(indx)
        self.comboBox_leistungsotyp.setCurrentIndex(0)

    def update_zahler(self, index):
        indx = self.model_zahler.index(index, 0, self.comboBox_zahler.rootModelIndex())
        self.comboBox_zahlertyp.setRootModelIndex(indx)
        self.comboBox_zahlertyp.setCurrentIndex(0)

    def update_uberwach(self, index):
        indx = self.model_uberwach.index(index, 0, self.comboBox_uberwach.rootModelIndex())
        self.comboBox_uberwachtyp.setRootModelIndex(indx)
        self.comboBox_uberwachtyp.setCurrentIndex(0)

    def update_leistungsr(self, index):
        indx = self.model_leistungsr.index(index, 0, self.comboBox_leistungsr.rootModelIndex())
        self.comboBox_leistungsrtyp.setRootModelIndex(indx)
        self.comboBox_leistungsrtyp.setCurrentIndex(0)

    def update_ladest(self, index):
        indx = self.model_ladest.index(index, 0, self.comboBox_ladest.rootModelIndex())
        self.comboBox_lasttyp.setRootModelIndex(indx)
        self.comboBox_lasttyp.setCurrentIndex(0)

    def update_batterie(self, index):
        indx = self.model_batterie.index(index, 0, self.comboBox_batterie.rootModelIndex())
        self.comboBox_batterietyp.setRootModelIndex(indx)
        self.comboBox_batterietyp.setCurrentIndex(0)

    def update_unterkon(self, index):
        indx = self.model_unterkon.index(index, 0, self.comboBox_unterkon.rootModelIndex())
        self.comboBox_unterkontyp.setRootModelIndex(indx)
        self.comboBox_unterkontyp.setCurrentIndex(0)

    def update_gak(self, index):
        indx = self.model_gak.index(index, 0, self.comboBox_gak.rootModelIndex())
        self.comboBox_gaktyp.setRootModelIndex(indx)
        self.comboBox_gaktyp.setCurrentIndex(0)

    def update_anzeigeta(self, index):
        indx = self.model_anzeigeta.index(index, 0, self.comboBox_anzeigeta.rootModelIndex())
        self.comboBox_anzeigetaftyp.setRootModelIndex(indx)
        self.comboBox_anzeigetaftyp.setCurrentIndex(0)

    def update_sensor(self, index):
        indx = self.model_sensor.index(index, 0, self.comboBox_sensor.rootModelIndex())
        self.comboBox_sensortyp.setRootModelIndex(indx)
        self.comboBox_sensortyp.setCurrentIndex(0)

        
    


    def clicked(self, i):
#        nr1 = []
#        nr2 = []
#        nr3 = []
#        nr4 = []
#        nr5 = []
#        nr6 = []
        
#        def test(fix):
#            def copy(a, b):
#                for i in range(len(wr_doc_nr)):
#                    if b in wr_doc_nr[i]:
#                        a.append('%s' % i)
#                else:
#                    print(penis)
#            copy(nr1, self.comboBox_modultyp.currentText())       
#        print(nr1)
        #    ww = b[int(nr1[0])]
            
            
        #PDFwr = []
     
        #for i in Path("Wechselrichter", self.comboBox_wr.currentText()).glob("*"):
        #    if i.suffix == ".pdf":
        #        PDFwr.append(i.name)  
            
        doc = []

        for i in PDFwr:
            if def_wr[0] in i:
                doc.append(i)
            elif def_wr[1] in i:
                doc.append(i)
            elif def_wr[2] in i:
                doc.append(i)
            
        
        
        
        

        #Pläne:


        t1 = ['1.-3. Dokumentationsblätter/0 Titelblatt DE.docx', 
              '1.-3. Dokumentationsblätter/0 Titelblatt FR.docx', 
              '1.-3. Dokumentationsblätter/0 Titelblatt EN.docx']
        t2 = ['1.-3. Dokumentationsblätter/1.2 Beteiligte Unternehmen DE.docx', 
              '1.-3. Dokumentationsblätter/1.2 Beteiligte Unternehmen FR.docx', 
              '1.-3. Dokumentationsblätter/1.2 Beteiligte Unternehmen EN.docx']
        t4 = ['1.-3. Dokumentationsblätter/1.5 Wartung & Unterhalt DE.docx',
              '1.-3. Dokumentationsblätter/1.5 Wartung & Unterhalt FR.docx',
              '1.-3. Dokumentationsblätter/1.5 Wartung & Unterhalt EN.docx']

        c1 = ['Anlagebetreiber', 'Opérateur de usine', 'Plant operator']
        c2 = ['Planer', 'Planificateur', 'Planner']
        c3 = ['Installateur PV-Anlage', 'Installateur de systèmes PV', 'Installer PV plant']
        c4 = ['Elektroinstallateur', 'Électricien', 'Electrician']
        c5 = ['Installateur ABS', 'Installateur ABS', 'Installer ABS']
        c6 = ['Gerüstebauer', 'Monteurs des échafaudages', 'Scaffolding erector']


        template = t1[sp]
        titelblatt = MailMerge(template)

        template2 = t2[sp]
        unternehmen = MailMerge(template2)
        
        template3 = t4[sp]
        wartung = MailMerge(template3)

        
        
        for i in self.lineEdit_strasseobjekt.text():
            if i != ('*'):
                titelblatt.merge(
                Objekt = objekt,
                O_Strasse = w7,
                O_PLZ = w8,
                O_Ort = w9)
            else:
                continue        
                
                
        titelblatt.merge(
            Monat_Abschluss = dateM,
            Jahr_Abschluss = ap2[2],
            NameFirma = w2,
            Nachname = w3,
            Strass_Nr = w4,
            PLZ = w5,
            Ort = w6,
            m2_Feldgrösse = w10,
            kWp_Leistung = w11,
            kVA_Leistung = w12,
            kWh_Jahresertrag = w13)

        ##########Brauche eine schlaufe, bei der es immer zu oberst eingefügt wird, wenn etwas nicht vorhanden ist.
        for i in self.lineEdit_strasseobjekt.text():
            if i != ('*'):
                unternehmen.merge(
                Strass_Nr = w4,
                PLZ = w5,
                Ort = w6)
            elif i == ('*'):
                unternehmen.merge(
                Strass_Nr = w7,
                PLZ = w8,
                Ort = w9)
        
        unternehmen.merge(
            titel1 = c1[sp],
            NameFirma = w2,
            Nachname = w3,
            
            titel2 = c2[sp],
            Name1 = u1,
            Strass_Nr1 = u2,
            PLZ1 = u3,
            Ort1 = u4,
            
            titel3 = c3[sp],
            Name2 = u5,
            Strass_Nr2 = u6,
            PLZ2 = u7,
            Ort2 = u8,
            
            titel4 = c4[sp],
            Name3 = u9,
            Strass_Nr3 = u10,
            PLZ3 = u11,
            Ort3 = u12,
            
            titel5 = c5[sp],
            ABSInstal_NameFirma = u13,
            Strass_Nr4 = u14,
            PLZ4 = u15,
            Ort4 = u16,
            titel6 = c6[sp],
            GerüstInstal_NameFirma = u17,
            Strass_Nr5 = u18,
            PLZ5 = u19,
            Ort5 = u20)
        ##########
        
        

#Wartung & Unterhalt
        for i in self.lineEdit_strasseobjekt.text():
            if i != ('*'):
                wartung.merge(
                O_Strasse_Nr = w4,
                O_PLZ = w5,
                O_Ort = w6)
            elif i == ('*'):
                wartung.merge(
                O_Strasse_Nr = w7,
                O_PLZ = w8,
                O_Ort = w9)
                      
                
        #source = r'1.-3. Dokumentationsblätter\3.6 Suva_Arbeiten auf Dächern-DE - Kopie.pdf'
        #destination = r'Output\new.pdf'
        #shutil.copyfile(source,destination)
        
        #titelblatt.write('Output/Titelblatt-'+w4+'.docx')
        #convert('Output/Titelblatt-'+w4+'.docx', 'Output/Titelblatt-'+w4+'.pdf')
        #unternehmen.write('Output/Beteiligte Unternehmen-'+w4+'.docx')
        #convert('Output/Beteiligte Unternehmen-'+w4+'.docx', 'Output/Beteiligte Unternehmen-'+w4+'.pdf')
        #wartung.write('Output/Wartung & Unterhalt-'+w4+'.docx')
        #convert('Output/Wartung & Unterhalt-'+w4+'.docx', 'Output/Wartung & Unterhalt-'+w4+'.pdf')
        
        
        titelblatt.close()
        unternehmen.close()
        wartung.close()
            
        
        
data_sol = {
    "":[""],
    sol_marken[0]:sol_typen1,
    sol_marken[1]:sol_typen2,
    sol_marken[2]:sol_typen3,
    sol_marken[3]:sol_typen4
    #sol_marken[4]:sol_typen5,
    #sol_marken[5]:sol_typen6,
    #sol_marken[6]:sol_typen7,
    #sol_marken[7]:sol_typen8,
    #sol_marken[8]:sol_typen9,
    #sol_marken[9]:sol_typen10
}

data_wr = {
    "":[""],
    wr_marken[0]:wr_typen1,
    wr_marken[1]:wr_typen2,
    wr_marken[2]:wr_typen3,
    wr_marken[3]:wr_typen4,
    wr_marken[4]:wr_typen5
}

data_leist_o = {
    "":[""],
    leist_o_marken[0]:leist_o_typen1,
    leist_o_marken[1]:leist_o_typen2
}

data_zeh = {
    "":[""],
    zeh_marken[0]:zeh_typen1,
    zeh_marken[1]:zeh_typen2,
    zeh_marken[2]:zeh_typen3
}

data_anlage = {
    "":[""],
    anlage_marken[0]:anlage_typen1,
    anlage_marken[1]:anlage_typen2,
    anlage_marken[2]:anlage_typen3,
    anlage_marken[3]:anlage_typen4
}

data_leist_r = {
    "":[""],
    leist_r_marken[0]:leist_typen1,
    leist_r_marken[1]:leist_typen2,
    leist_r_marken[2]:leist_typen3
}

data_lade = {
    "":[""],
    lade_marken[0]:lade_typen1,
    lade_marken[1]:lade_typen2,
    lade_marken[2]:lade_typen3,
    lade_marken[3]:lade_typen4
}

data_batt = {
    "":[""],
    batt_marken[0]:batt_typen1,
    batt_marken[1]:batt_typen2,
    batt_marken[2]:batt_typen3,
    batt_marken[3]:batt_typen4,
    batt_marken[4]:batt_typen5,
    batt_marken[5]:batt_typen6,
    batt_marken[6]:batt_typen7
}

data_unterkon = {
    "":[""],
    unterkon_marken[0]:unterkon_typen1
}

data_ueberspan = {
    "":[""],
    ueberspan_marken[0]:ueberspan_typen1,
    ueberspan_marken[1]:ueberspan_typen2,
    ueberspan_marken[2]:ueberspan_typen3
}

data_anzeiget = {
    "":[""],
    anzeiget_marken[0]:anzeiget_typen1
}

data_sens = {
    "":[""],
    sens_marken[0]:sens_typen1,
    sens_marken[1]:sens_typen2

}  




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())