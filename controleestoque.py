# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def incluir(self):
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        texto = self.lineEdit.text()
        qtd = self.doubleSpinBox.text()
        
        if float(qtd.replace(",", ".")) > 0:        
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(qtd))
            self.tableWidget.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(texto))

        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("É necessário entrar com pelo menos um valor")
            msgBox.setWindowTitle("Valor inválido")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec_()
            
        
    def excluir(self):
        self.tableWidget.removeRow(self.tableWidget.currentRow())


    def imprimir(self):
        lista = []
        maxrow = self.tableWidget.rowCount()
        for i in range (0, maxrow):
            lista.append((self.tableWidget.item(i, 0).text(), (self.tableWidget.item(i, 1).text())))
        print(lista)
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(388, 321)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 210, 101, 20))
        self.lineEdit.setObjectName("lineEdit")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.incluir)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.excluir)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 44, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.imprimir)

        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 256, 192))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Qtd.", "Descrição"])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        
        self.tableWidget.setRowCount(0)

        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setEnabled(True)
        self.doubleSpinBox.setGeometry(QtCore.QRect(10, 210, 62, 21))
        self.doubleSpinBox.setAutoFillBackground(False)
        self.doubleSpinBox.setWrapping(False)
        self.doubleSpinBox.setFrame(True)
        self.doubleSpinBox.setReadOnly(False)
        self.doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 388, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Incluir"))
        self.pushButton_2.setText(_translate("MainWindow", "Excluir"))
        self.pushButton_3.setText(_translate("MainWindow", "Imprimir"))
        self.tableWidget.setSortingEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
