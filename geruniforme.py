import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

from selecionafuncionario import SelFunc

import time

#===== Conexão ao banco de dados =====#
import sqlite3
conn = sqlite3.connect('abn.db')
cursor = conn.cursor()
#=====================================#

class GerUniforme(QtWidgets.QDialog):
    # Define os metódos para o formulário de gerenciamento de uniformes
    def removemovimentacao(self):
        # Remove a movimentação selecioinada
        selecionado = self.tableWidget_movimentacao.currentRow()
        self.tableWidget_movimentacao.removeRow(selecionado)
        print(selecionado)
    
    def adicionamovimentacao(self):
        # Adiciona uma movimentação de acordo com os dados informados
        self.movimentacao = {
            'ação': None,
	    'uniforme': self.comboBox_descricaouniforme.currentText(),
	    'tamanho': self.comboBox_tamanho.currentText(),
	    'qtd': str(self.spinBox_qtd.value()),
	    'obs': self.textEdit_obs.toPlainText()}
        
        if self.radioButton_retirada.isChecked():
            self.movimentacao['ação'] = "retirada"

        if self.radioButton_devolucao.isChecked():
            self.movimentacao['ação'] = "devolucao"

        if self.movimentacao['uniforme'] == "":
        # Caso não seja infomado o tipo de uniforme é exibida mensaggem de erro
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setText("É necessário selecionar um uniforme")
            self.msgBox.setWindowTitle("Sem uniforme selecionado")
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            self.msgBox.exec_()

        elif self.movimentacao['tamanho'] == "":
        # Caso não seja infomado o tamanho é exibida mensaggem de erro
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setText("É necessário selecionar um tamanho")
            self.msgBox.setWindowTitle("Sem tamanho selecionado")
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            self.msgBox.exec_()

        elif self.movimentacao['qtd'] == "0":
        # Caso não seja infomado a quantidade é exibida mensaggem de erro
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setText("É necessário informar uma quantidade")
            self.msgBox.setWindowTitle("Sem quantidade informada")
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            self.msgBox.exec_()

        else:
            # Caso não tenha sido exibida nenhuma mensagem de erro os dados são
            #lançados na tabela de movimentação
            rowPosition = self.tableWidget_movimentacao.rowCount()
            self.tableWidget_movimentacao.insertRow(rowPosition)
            self.tableWidget_movimentacao.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(self.movimentacao['ação']))
            self.tableWidget_movimentacao.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(self.movimentacao['qtd']))
            self.tableWidget_movimentacao.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(self.movimentacao['uniforme']))
            self.tableWidget_movimentacao.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(self.movimentacao['tamanho']))
            self.tableWidget_movimentacao.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(self.movimentacao['obs']))
            print(time.time())
    def registramovimentacao(self):
        col_count = self.tableWidget_movimentacao.columnCount()
        row_count = self.tableWidget_movimentacao.rowCount()
        
        
        for i in range(row_count):
            rowdata = []
            for j in range(col_count):
                rowdata.append(self.tableWidget_movimentacao.item(i, j).text())   
        
            produtivo = self.idfuncionario
            data = time.time()
            acao = rowdata[0]
            qtd = rowdata[1]
            descricao = rowdata[2]
            tamanho = rowdata[3]
            obs = rowdata[4]                
            cursor.execute("""
                            INSERT INTO funcionario_controleuniforme(ID_produtivo,
                                                                    data,
                                                                    tipomovimentacao,
                                                                    tipouniforme,
                                                                    qtduniforme,
                                                                    tamanhouniforme,
                                                                    obs)
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                            """, (produtivo, data, acao, qtd, descricao, tamanho, obs))
        conn.commit()
    def show_buscafuncionario(self):
        dialog = self.buscafuncionario
        dialog.exec_()
        self.idfuncionario = dialog.seleciona()[0]
        self.nomeoficial = dialog.seleciona()[1]
        self.lcdNumber_idfuncionario.display(int(self.idfuncionario)) 
        self.lineEdit_busca.setText(self.nomeoficial)
        self.lineEdit_busca.setEnabled(False)      
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("PainelABN_geruniforme.ui", self)
        self.buscafuncionario = SelFunc(self)
        self.pushButton_adicionar.clicked.connect(self.adicionamovimentacao) # Botão [Adicionar]
        self.pushButton_remover.clicked.connect(self.removemovimentacao) # Botão [Remover]
        self.pushButton_registrar.clicked.connect(self.registramovimentacao) # Botão [Registrar]
        self.pushButton_busca.clicked.connect(self.show_buscafuncionario)
