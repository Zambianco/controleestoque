# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PainelABN_saidaitensparapedido.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import psycopg2
from PainelABN_cadastrodeitens import Ui_frm_cadprod

conn = psycopg2.connect("dbname=abn user=postgres password=abn2020")
cursor = conn.cursor()

class Ui_Form_Saidaparapedido(object):
    
    def incluir(self):
        self.tableWidget_listadeitensretirados.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        texto = self.lineEdit_resultadobusca.text()
        qtd = self.doubleSpinBox_qtd.text()
        
        if texto == "":
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setText("É necessário entrar com o código do item")
            self.msgBox.setWindowTitle("Valor inválido")
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            self.msgBox.exec_()
            self.doubleSpinBox_qtd.clear()
            self.lineEdit_resultadobusca.clear()
            return None
            
            
        if float(qtd.replace(",", ".")) > 0:
            rowPosition = self.tableWidget_listadeitensretirados.rowCount()
            self.tableWidget_listadeitensretirados.insertRow(rowPosition)
            self.tableWidget_listadeitensretirados.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(qtd))
            self.tableWidget_listadeitensretirados.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(texto))
            self.lineEdit_busca.clear()
            self.doubleSpinBox_qtd.clear()
            self.lineEdit_resultadobusca.clear()
            
        else:
            print('0')
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setText("É necessário entrar com pelo menos um valor")
            self.msgBox.setWindowTitle("Valor inválido")
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            self.msgBox.exec_()

        
    def retirar(self):
        self.tableWidget_listadeitensretirados.removeRow(self.tableWidget_listadeitensretirados.currentRow())

    def show(self):
        from PainelABN_cadmaterial import Ui_Form_CadMaterial
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_CadMaterial()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.setWindowModality(QtCore.Qt.WindowModal)
        
            
    def buscaitem(self):  
        barcode = self.lineEdit_busca.text()
        cursor.execute("""SELECT descricaolonga FROM sku_descricao WHERE barcodeean13='{}'""".format(barcode))
        resultado = cursor.fetchone()

        if resultado is not None:
            self.lineEdit_resultadobusca.setText(str(resultado[0]))
        else:
            QtCore.QTimer.singleShot(100, self.show)

        if self.checkBox_mododireto.isChecked():
            self.doubleSpinBox_qtd.setValue(1.00)
            self.incluir()
            self.lineEdit_busca.clear()
            self.lineEdit_busca.setFocus()
            

    def setupUi(self, Form_Saidaparapedido):
        Form_Saidaparapedido.setObjectName("Form_Saidaparapedido")
        Form_Saidaparapedido.setWindowModality(QtCore.Qt.ApplicationModal)
        Form_Saidaparapedido.resize(760, 440)
        Form_Saidaparapedido.setMaximumSize(QtCore.QSize(760, 441))
        Form_Saidaparapedido.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)

        self.cbox_pedido = QtWidgets.QComboBox(Form_Saidaparapedido)
        self.cbox_pedido.setGeometry(QtCore.QRect(10, 40, 69, 22))
        self.cbox_pedido.setObjectName("cbox_pedido")

        self.lbl_cboxpedido = QtWidgets.QLabel(Form_Saidaparapedido)
        self.lbl_cboxpedido.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.lbl_cboxpedido.setObjectName("lbl_cboxpedido")

        self.frame_funcionario = QtWidgets.QFrame(Form_Saidaparapedido)
        self.frame_funcionario.setGeometry(QtCore.QRect(90, 10, 291, 61))
        self.frame_funcionario.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_funcionario.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_funcionario.setObjectName("frame_funcionario")

        self.lbl_cboxfuncionario = QtWidgets.QPushButton(self.frame_funcionario)
        self.lbl_cboxfuncionario.setGeometry(QtCore.QRect(190, 30, 91, 23))
        self.lbl_cboxfuncionario.setObjectName("lbl_cboxfuncionario")

        self.cbox_Funcionario = QtWidgets.QComboBox(self.frame_funcionario)
        self.cbox_Funcionario.setGeometry(QtCore.QRect(10, 30, 171, 22))
        self.cbox_Funcionario.setObjectName("cbox_Funcionario")

        self.label_3 = QtWidgets.QLabel(self.frame_funcionario)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_3.setObjectName("label_3")

        self.button_registrar = QtWidgets.QPushButton(Form_Saidaparapedido)
        self.button_registrar.setGeometry(QtCore.QRect(10, 410, 101, 23))
        self.button_registrar.setObjectName("button_registrar")
        self.button_registrar.clicked.connect(self.show)
        
        self.button_cancelar = QtWidgets.QPushButton(Form_Saidaparapedido)
        self.button_cancelar.setGeometry(QtCore.QRect(670, 410, 75, 23))
        self.button_cancelar.setObjectName("button_cancelar")

        self.button_limpar = QtWidgets.QPushButton(Form_Saidaparapedido)
        self.button_limpar.setGeometry(QtCore.QRect(590, 410, 75, 23))
        self.button_limpar.setObjectName("button_limpar")

        self.tabWidget_relacao = QtWidgets.QTabWidget(Form_Saidaparapedido)
        self.tabWidget_relacao.setGeometry(QtCore.QRect(10, 70, 741, 331))
        self.tabWidget_relacao.setObjectName("tabWidget_relacao")

        self.tab_listaitensretirada = QtWidgets.QWidget()
        self.tab_listaitensretirada.setObjectName("tab_listaitensretirada")
        self.tableWidget_listadeitensretirados = QtWidgets.QTableWidget(self.tab_listaitensretirada)
        self.tableWidget_listadeitensretirados.setGeometry(QtCore.QRect(10, 10, 721, 231))
        self.tableWidget_listadeitensretirados.setObjectName("tableWidget_listadeitensretirados")
        self.tableWidget_listadeitensretirados.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_listadeitensretirados.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_listadeitensretirados.setAlternatingRowColors(True)
        self.tableWidget_listadeitensretirados.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_listadeitensretirados.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_listadeitensretirados.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)        
        self.tableWidget_listadeitensretirados.setColumnCount(2)
        self.tableWidget_listadeitensretirados.setHorizontalHeaderLabels(["Qtd.", "Descrição"])
        self.tableWidget_listadeitensretirados.horizontalHeader().setStretchLastSection(True)
        
        self.button_editar = QtWidgets.QPushButton(self.tab_listaitensretirada)
        self.button_editar.setGeometry(QtCore.QRect(10, 250, 51, 23))
        self.button_editar.setObjectName("button_editar")
        
        self.button_remover = QtWidgets.QPushButton(self.tab_listaitensretirada)
        self.button_remover.setGeometry(QtCore.QRect(70, 250, 61, 23))
        self.button_remover.setObjectName("button_retirar")
        self.button_remover.clicked.connect(self.retirar)

        self.pushButton_adicionar = QtWidgets.QPushButton(self.tab_listaitensretirada)
        self.pushButton_adicionar.setGeometry(QtCore.QRect(660, 280, 75, 23))
        self.pushButton_adicionar.setObjectName("pushButton_3")
        self.pushButton_adicionar.clicked.connect(self.incluir)

        self.lineEdit_resultadobusca = QtWidgets.QLineEdit(self.tab_listaitensretirada)
        self.lineEdit_resultadobusca.setEnabled(False)
        self.lineEdit_resultadobusca.setGeometry(QtCore.QRect(280, 280, 371, 20))
        self.lineEdit_resultadobusca.setObjectName("lineEdit_resultadobusca")

        self.doubleSpinBox_qtd = QtWidgets.QDoubleSpinBox(self.tab_listaitensretirada)
        self.doubleSpinBox_qtd.setGeometry(QtCore.QRect(10, 280, 71, 22))
        self.doubleSpinBox_qtd.setObjectName("doubleSpinBox_qtd")
        
        self.checkBox_mododireto = QtWidgets.QCheckBox(self.tab_listaitensretirada)
        self.checkBox_mododireto.setGeometry(QtCore.QRect(650, 250, 81, 20))
        self.checkBox_mododireto.setCheckable(True)
        self.checkBox_mododireto.setChecked(True)
        self.checkBox_mododireto.setAutoRepeat(False)
        self.checkBox_mododireto.setObjectName("checkBox_mododireto")

        self.lineEdit_busca = QtWidgets.QLineEdit(self.tab_listaitensretirada)
        self.lineEdit_busca.setGeometry(QtCore.QRect(90, 280, 141, 21))
        self.lineEdit_busca.setText("")
        self.lineEdit_busca.setObjectName("lineEdit_busca")
        
        self.pushButton_busca = QtWidgets.QPushButton(self.tab_listaitensretirada)
        self.pushButton_busca.setGeometry(QtCore.QRect(240, 280, 31, 23))
        self.pushButton_busca.setObjectName("pushButton_busca")
        self.pushButton_busca.clicked.connect(self.buscaitem)

        self.tabWidget_relacao.addTab(self.tab_listaitensretirada, "")
        self.tab_itensreservados = QtWidgets.QWidget()
        self.tab_itensreservados.setObjectName("tab_itensreservados")
        self.tableView = QtWidgets.QTableView(self.tab_itensreservados)
        self.tableView.setGeometry(QtCore.QRect(10, 60, 721, 211))
        self.tableView.setObjectName("tableView")

        self.button_retirartodos = QtWidgets.QPushButton(self.tab_itensreservados)
        self.button_retirartodos.setGeometry(QtCore.QRect(10, 280, 75, 23))
        self.button_retirartodos.setObjectName("button_retirartodos")

        self.button_retiraritem = QtWidgets.QPushButton(self.tab_itensreservados)
        self.button_retiraritem.setGeometry(QtCore.QRect(660, 280, 75, 23))
        self.button_retiraritem.setObjectName("button_retiraritem")

        self.lineEdit_selecionado = QtWidgets.QLineEdit(self.tab_itensreservados)
        self.lineEdit_selecionado.setEnabled(False)
        self.lineEdit_selecionado.setGeometry(QtCore.QRect(190, 280, 391, 20))
        self.lineEdit_selecionado.setObjectName("lineEdit_selecionado")

        self.doubleSpinBox_qtd_2 = QtWidgets.QDoubleSpinBox(self.tab_itensreservados)
        self.doubleSpinBox_qtd_2.setGeometry(QtCore.QRect(590, 280, 62, 22))
        self.doubleSpinBox_qtd_2.setObjectName("doubleSpinBox_qtd_2")

        self.cb_desenho = QtWidgets.QComboBox(self.tab_itensreservados)
        self.cb_desenho.setGeometry(QtCore.QRect(110, 30, 171, 22))
        self.cb_desenho.setObjectName("cb_desenho")

        self.lbl_cbdesenho = QtWidgets.QLabel(self.tab_itensreservados)
        self.lbl_cbdesenho.setGeometry(QtCore.QRect(110, 10, 47, 13))
        self.lbl_cbdesenho.setObjectName("lbl_cbdesenho")

        self.cb_rm = QtWidgets.QComboBox(self.tab_itensreservados)
        self.cb_rm.setGeometry(QtCore.QRect(10, 30, 91, 22))
        self.cb_rm.setObjectName("cb_rm")

        self.lbl_cbrm = QtWidgets.QLabel(self.tab_itensreservados)
        self.lbl_cbrm.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.lbl_cbrm.setObjectName("lbl_cbrm")
        self.tabWidget_relacao.addTab(self.tab_itensreservados, "")

        self.lineEdit_busca.returnPressed.connect(self.pushButton_busca.click)

        self.retranslateUi(Form_Saidaparapedido)
        self.tabWidget_relacao.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form_Saidaparapedido)
        Form_Saidaparapedido.setTabOrder(self.tabWidget_relacao, self.cbox_pedido)
        Form_Saidaparapedido.setTabOrder(self.cbox_pedido, self.cbox_Funcionario)
        Form_Saidaparapedido.setTabOrder(self.cbox_Funcionario, self.lbl_cboxfuncionario)
        Form_Saidaparapedido.setTabOrder(self.lbl_cboxfuncionario, self.tableWidget_listadeitensretirados)
        Form_Saidaparapedido.setTabOrder(self.tableWidget_listadeitensretirados, self.doubleSpinBox_qtd)
        Form_Saidaparapedido.setTabOrder(self.doubleSpinBox_qtd, self.lineEdit_busca)
        Form_Saidaparapedido.setTabOrder(self.lineEdit_busca, self.pushButton_busca)
        Form_Saidaparapedido.setTabOrder(self.pushButton_busca, self.lineEdit_resultadobusca)
        Form_Saidaparapedido.setTabOrder(self.lineEdit_resultadobusca, self.pushButton_adicionar)
        Form_Saidaparapedido.setTabOrder(self.pushButton_adicionar, self.cb_rm)
        Form_Saidaparapedido.setTabOrder(self.cb_rm, self.cb_desenho)
        Form_Saidaparapedido.setTabOrder(self.cb_desenho, self.tableView)
        Form_Saidaparapedido.setTabOrder(self.tableView, self.button_retirartodos)
        Form_Saidaparapedido.setTabOrder(self.button_retirartodos, self.lineEdit_selecionado)
        Form_Saidaparapedido.setTabOrder(self.lineEdit_selecionado, self.doubleSpinBox_qtd_2)
        Form_Saidaparapedido.setTabOrder(self.doubleSpinBox_qtd_2, self.button_retiraritem)
        Form_Saidaparapedido.setTabOrder(self.button_retiraritem, self.button_limpar)
        Form_Saidaparapedido.setTabOrder(self.button_limpar, self.button_cancelar)
        Form_Saidaparapedido.setTabOrder(self.button_cancelar, self.button_registrar)

    def retranslateUi(self, Form_Saidaparapedido):
        _translate = QtCore.QCoreApplication.translate
        Form_Saidaparapedido.setWindowTitle(_translate("Form_Saidaparapedido", "Saída de itens para pedido"))
        self.lbl_cboxpedido.setText(_translate("Form_Saidaparapedido", "Pedido"))
        self.lbl_cboxfuncionario.setText(_translate("Form_Saidaparapedido", "Pedido anterior"))
        self.label_3.setText(_translate("Form_Saidaparapedido", "Funcionário"))
        self.button_registrar.setText(_translate("Form_Saidaparapedido", "Registrar retirada"))
        self.button_cancelar.setText(_translate("Form_Saidaparapedido", "Cancelar"))
        self.button_limpar.setText(_translate("Form_Saidaparapedido", "Limpar"))
        self.pushButton_adicionar.setText(_translate("Form_Saidaparapedido", "Adicionar"))
        self.pushButton_busca.setText(_translate("Form_Saidaparapedido", "🔍"))
        self.tabWidget_relacao.setTabText(self.tabWidget_relacao.indexOf(self.tab_listaitensretirada), _translate("Form_Saidaparapedido", "Retiradas"))
        self.button_retirartodos.setText(_translate("Form_Saidaparapedido", "Retirar todos"))
        self.button_retiraritem.setText(_translate("Form_Saidaparapedido", "Retirar item"))
        self.lbl_cbdesenho.setText(_translate("Form_Saidaparapedido", "Desenho"))
        self.lbl_cbrm.setText(_translate("Form_Saidaparapedido", "R.M."))
        self.tabWidget_relacao.setTabText(self.tabWidget_relacao.indexOf(self.tab_itensreservados), _translate("Form_Saidaparapedido", "Reservados"))
        self.button_remover.setText(_translate("button_retirar", "Retirar"))
        self.checkBox_mododireto.setText(_translate("Form_Saidaparapedido", "Modo direto"))



def main():
    import sys
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Saidaparapedido = QtWidgets.QWidget()
    ui = Ui_Form_Saidaparapedido()
    ui.setupUi(Form_Saidaparapedido)
    Form_Saidaparapedido.show()
    sys.exit(app.exec_())

  
if __name__ == "__main__":
    main()
##    import sys
##    app = QtWidgets.QApplication(sys.argv)
##    Form_Saidaparapedido = QtWidgets.QMainWindow()
##    ui = Ui_Form_Saidaparapedido()
##    ui.setupUi(Form_Saidaparapedido)
##    Form_Saidaparapedido.show()
##    sys.exit(app.exec_())
