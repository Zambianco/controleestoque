import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

#===== Conexão ao banco de dados =====#
import sqlite3
conn = sqlite3.connect('abn.db')
cursor = conn.cursor()
#=====================================#

class SelFunc(QtWidgets.QDialog):
    def seleciona(self):
        currentrow = self.tableWidget_listafuncionario.currentRow()
        idfuncionario = self.tableWidget_listafuncionario.item(currentrow, 0).text()
        nomeoficial = self.tableWidget_listafuncionario.item(currentrow, 1).text()
        return idfuncionario, nomeoficial, self.close()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("PainelABN_selecionafuncionario.ui", self)
        
        # Preenchimento da tabela com a busca realizada
        cursor.execute("""SELECT IDfuncionario_dados, funcionario_nome, funcionario_apelido, funcionario_cargo
                          FROM produtivo""")
        records = cursor.fetchall()
        
        for funcionario in records:
            rowPosition = self.tableWidget_listafuncionario.rowCount()
            self.tableWidget_listafuncionario.insertRow(rowPosition)
            self.tableWidget_listafuncionario.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(funcionario[0])))
            self.tableWidget_listafuncionario.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(funcionario[1]))
            self.tableWidget_listafuncionario.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(funcionario[2]))
            self.tableWidget_listafuncionario.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(funcionario[3]))
            
        self.tableWidget_listafuncionario.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget_listafuncionario.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        self.pushButton_selecionar.clicked.connect(self.seleciona)
        self.buttonBox.accepted.connect(self.seleciona)