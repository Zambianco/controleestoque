# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PainelABN_cadmaterial.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_CadMaterial(object):
    def setupUi(self, Form_CadMaterial):
        Form_CadMaterial.setObjectName("Form_CadMaterial")
        Form_CadMaterial.setWindowModality(QtCore.Qt.WindowModal)
        Form_CadMaterial.resize(1031, 410)
        self.tabWidget = QtWidgets.QTabWidget(Form_CadMaterial)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1011, 391))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 986, 281))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 3, 3, 1, 1)
        self.lineEdit_descrlonga = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_descrlonga.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_descrlonga.setText("")
        self.lineEdit_descrlonga.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_descrlonga.setObjectName("lineEdit_descrlonga")
        self.gridLayout_2.addWidget(self.lineEdit_descrlonga, 4, 2, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setEnabled(True)
        self.label_8.setMinimumSize(QtCore.QSize(125, 0))
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setIndent(-1)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 8, 1, 1, 1)
        self.pushButton_excluirfoto = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_excluirfoto.setObjectName("pushButton_excluirfoto")
        self.gridLayout_2.addWidget(self.pushButton_excluirfoto, 11, 6, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 10, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setMinimumSize(QtCore.QSize(125, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_17.setMinimumSize(QtCore.QSize(125, 0))
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 5, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setEnabled(True)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 9, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.doubleSpinBox_AgrSai = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox_AgrSai.setMaximumSize(QtCore.QSize(50, 16777215))
        self.doubleSpinBox_AgrSai.setObjectName("doubleSpinBox_AgrSai")
        self.horizontalLayout_5.addWidget(self.doubleSpinBox_AgrSai)
        self.Combobox_AgrSai = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.Combobox_AgrSai.setMaximumSize(QtCore.QSize(50, 16777215))
        self.Combobox_AgrSai.setObjectName("Combobox_AgrSai")
        self.horizontalLayout_5.addWidget(self.Combobox_AgrSai)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 9, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.doubleSpinBox_AgrEnt = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox_AgrEnt.setMaximumSize(QtCore.QSize(50, 16777215))
        self.doubleSpinBox_AgrEnt.setObjectName("doubleSpinBox_AgrEnt")
        self.horizontalLayout.addWidget(self.doubleSpinBox_AgrEnt)
        self.Combobox_AgrEntr2_2 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.Combobox_AgrEntr2_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.Combobox_AgrEntr2_2.setObjectName("Combobox_AgrEntr2_2")
        self.horizontalLayout.addWidget(self.Combobox_AgrEntr2_2)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        self.Combobox_AgrEntr2 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.Combobox_AgrEntr2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.Combobox_AgrEntr2.setObjectName("Combobox_AgrEntr2")
        self.horizontalLayout.addWidget(self.Combobox_AgrEntr2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 8, 2, 1, 1)
        self.lineEdit_codbarean13 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_codbarean13.setMinimumSize(QtCore.QSize(180, 20))
        self.lineEdit_codbarean13.setText("")
        self.lineEdit_codbarean13.setMaxLength(7)
        self.lineEdit_codbarean13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_codbarean13.setObjectName("lineEdit_codbarean13")
        self.gridLayout_2.addWidget(self.lineEdit_codbarean13, 7, 2, 1, 1)
        self.lineEdit_descrreduzida = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_descrreduzida.setMinimumSize(QtCore.QSize(180, 20))
        self.lineEdit_descrreduzida.setText("")
        self.lineEdit_descrreduzida.setMaxLength(7)
        self.lineEdit_descrreduzida.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_descrreduzida.setObjectName("lineEdit_descrreduzida")
        self.gridLayout_2.addWidget(self.lineEdit_descrreduzida, 5, 2, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 7, 3, 1, 1)
        self.checkBox_restrito = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_restrito.setObjectName("checkBox_restrito")
        self.gridLayout_2.addWidget(self.checkBox_restrito, 2, 1, 1, 1)
        self.lineEdit_codfabricante = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_codfabricante.setMinimumSize(QtCore.QSize(180, 20))
        self.lineEdit_codfabricante.setText("")
        self.lineEdit_codfabricante.setMaxLength(7)
        self.lineEdit_codfabricante.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_codfabricante.setObjectName("lineEdit_codfabricante")
        self.gridLayout_2.addWidget(self.lineEdit_codfabricante, 7, 4, 1, 1)
        self.pushButton_inlcuirfoto = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_inlcuirfoto.setObjectName("pushButton_inlcuirfoto")
        self.gridLayout_2.addWidget(self.pushButton_inlcuirfoto, 11, 5, 1, 1)
        self.graphicsView_fotoitem = QtWidgets.QGraphicsView(self.gridLayoutWidget_2)
        self.graphicsView_fotoitem.setMinimumSize(QtCore.QSize(218, 180))
        self.graphicsView_fotoitem.setObjectName("graphicsView_fotoitem")
        self.gridLayout_2.addWidget(self.graphicsView_fotoitem, 2, 5, 9, 2)
        self.lineEdit_frabricante = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_frabricante.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_frabricante.setText("")
        self.lineEdit_frabricante.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_frabricante.setObjectName("lineEdit_frabricante")
        self.gridLayout_2.addWidget(self.lineEdit_frabricante, 6, 2, 1, 1)
        self.comboBox_grupo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_grupo.setObjectName("comboBox_grupo")
        self.gridLayout_2.addWidget(self.comboBox_grupo, 3, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 7, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setEnabled(True)
        self.label_16.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 6, 1, 1, 1)
        self.checkBox_ativo = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_ativo.setObjectName("checkBox_ativo")
        self.gridLayout_2.addWidget(self.checkBox_ativo, 2, 2, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_Loc1 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_Loc1.setMinimumSize(QtCore.QSize(50, 20))
        self.lineEdit_Loc1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_Loc1.setObjectName("lineEdit_Loc1")
        self.horizontalLayout_10.addWidget(self.lineEdit_Loc1)
        self.lineEdit_Loc2 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_Loc2.setMinimumSize(QtCore.QSize(51, 20))
        self.lineEdit_Loc2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_Loc2.setObjectName("lineEdit_Loc2")
        self.horizontalLayout_10.addWidget(self.lineEdit_Loc2)
        self.lineEdit_Loc3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_Loc3.setMinimumSize(QtCore.QSize(51, 20))
        self.lineEdit_Loc3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_Loc3.setObjectName("lineEdit_Loc3")
        self.horizontalLayout_10.addWidget(self.lineEdit_Loc3)
        self.lineEdit_Loc4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_Loc4.setMinimumSize(QtCore.QSize(51, 20))
        self.lineEdit_Loc4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_Loc4.setObjectName("lineEdit_Loc4")
        self.horizontalLayout_10.addWidget(self.lineEdit_Loc4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 10, 2, 1, 1)
        self.lineEdit_sku = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_sku.setMinimumSize(QtCore.QSize(85, 0))
        self.lineEdit_sku.setMaximumSize(QtCore.QSize(85, 16777215))
        self.lineEdit_sku.setText("")
        self.lineEdit_sku.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_sku.setReadOnly(False)
        self.lineEdit_sku.setClearButtonEnabled(False)
        self.lineEdit_sku.setObjectName("lineEdit_sku")
        self.gridLayout_2.addWidget(self.lineEdit_sku, 3, 4, 1, 1)
        self.pushButton_busca = QtWidgets.QPushButton(self.tab)
        self.pushButton_busca.setGeometry(QtCore.QRect(300, 20, 75, 23))
        self.pushButton_busca.setObjectName("pushButton_busca")
        self.lineEdit_busca = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_busca.setGeometry(QtCore.QRect(20, 20, 271, 20))
        self.lineEdit_busca.setObjectName("lineEdit_busca")
        self.pushButton_Salvar = QtWidgets.QPushButton(self.tab)
        self.pushButton_Salvar.setGeometry(QtCore.QRect(470, 340, 75, 23))
        self.pushButton_Salvar.setObjectName("pushButton_Salvar")
        self.pushButton_Excluir = QtWidgets.QPushButton(self.tab)
        self.pushButton_Excluir.setGeometry(QtCore.QRect(550, 340, 75, 23))
        self.pushButton_Excluir.setObjectName("pushButton_Excluir")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 10, 211, 200))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 5, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 7, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.doubleSpinBox_dimF = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_dimF.setObjectName("doubleSpinBox_dimF")
        self.gridLayout.addWidget(self.doubleSpinBox_dimF, 6, 1, 1, 1)
        self.doubleSpinBox_dimA = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_dimA.setObjectName("doubleSpinBox_dimA")
        self.gridLayout.addWidget(self.doubleSpinBox_dimA, 1, 1, 1, 1)
        self.doubleSpinBox_dimB = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_dimB.setObjectName("doubleSpinBox_dimB")
        self.gridLayout.addWidget(self.doubleSpinBox_dimB, 2, 1, 1, 1)
        self.doubleSpinBox_dimC = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_dimC.setObjectName("doubleSpinBox_dimC")
        self.gridLayout.addWidget(self.doubleSpinBox_dimC, 3, 1, 1, 1)
        self.doubleSpinBox_dimE = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_dimE.setObjectName("doubleSpinBox_dimE")
        self.gridLayout.addWidget(self.doubleSpinBox_dimE, 5, 1, 1, 1)
        self.doubleSpinBox_peso = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_peso.setObjectName("doubleSpinBox_peso")
        self.gridLayout.addWidget(self.doubleSpinBox_peso, 7, 1, 1, 1)
        self.doubleSpinBox_dimD = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_dimD.setObjectName("doubleSpinBox_dimD")
        self.gridLayout.addWidget(self.doubleSpinBox_dimD, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.comboBox_dimunitB = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_dimunitB.setMaximumSize(QtCore.QSize(50, 16777215))
        self.comboBox_dimunitB.setObjectName("comboBox_dimunitB")
        self.gridLayout.addWidget(self.comboBox_dimunitB, 2, 2, 1, 1)
        self.comboBox_dimunitC = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_dimunitC.setMaximumSize(QtCore.QSize(50, 16777215))
        self.comboBox_dimunitC.setObjectName("comboBox_dimunitC")
        self.gridLayout.addWidget(self.comboBox_dimunitC, 3, 2, 1, 1)
        self.comboBox_dimunitE = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_dimunitE.setMaximumSize(QtCore.QSize(50, 16777215))
        self.comboBox_dimunitE.setObjectName("comboBox_dimunitE")
        self.gridLayout.addWidget(self.comboBox_dimunitE, 5, 2, 1, 1)
        self.comboBox_dimunitD = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_dimunitD.setMaximumSize(QtCore.QSize(50, 16777215))
        self.comboBox_dimunitD.setObjectName("comboBox_dimunitD")
        self.gridLayout.addWidget(self.comboBox_dimunitD, 4, 2, 1, 1)
        self.comboBox_dimunitF = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_dimunitF.setMaximumSize(QtCore.QSize(50, 16777215))
        self.comboBox_dimunitF.setObjectName("comboBox_dimunitF")
        self.gridLayout.addWidget(self.comboBox_dimunitF, 6, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.comboBox_dimunitA = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_dimunitA.setMaximumSize(QtCore.QSize(50, 20))
        self.comboBox_dimunitA.setMaxVisibleItems(15)
        self.comboBox_dimunitA.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_dimunitA.setObjectName("comboBox_dimunitA")
        self.gridLayout.addWidget(self.comboBox_dimunitA, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 7, 2, 1, 1)
        self.graphicsView_desenho = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_desenho.setGeometry(QtCore.QRect(250, 10, 291, 231))
        self.graphicsView_desenho.setObjectName("graphicsView_desenho")
        self.pushButton_incluirdesenho = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_incluirdesenho.setGeometry(QtCore.QRect(250, 250, 72, 23))
        self.pushButton_incluirdesenho.setObjectName("pushButton_incluirdesenho")
        self.pushButton_excluirdesenho = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_excluirdesenho.setGeometry(QtCore.QRect(470, 250, 72, 23))
        self.pushButton_excluirdesenho.setObjectName("pushButton_excluirdesenho")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.plainTextEdit_Observacao = QtWidgets.QPlainTextEdit(self.tab_3)
        self.plainTextEdit_Observacao.setGeometry(QtCore.QRect(13, 10, 931, 211))
        self.plainTextEdit_Observacao.setObjectName("plainTextEdit_Observacao")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form_CadMaterial)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form_CadMaterial)
        Form_CadMaterial.setTabOrder(self.tabWidget, self.lineEdit_busca)
        Form_CadMaterial.setTabOrder(self.lineEdit_busca, self.pushButton_busca)
        Form_CadMaterial.setTabOrder(self.pushButton_busca, self.checkBox_restrito)
        Form_CadMaterial.setTabOrder(self.checkBox_restrito, self.checkBox_ativo)
        Form_CadMaterial.setTabOrder(self.checkBox_ativo, self.comboBox_grupo)
        Form_CadMaterial.setTabOrder(self.comboBox_grupo, self.lineEdit_sku)
        Form_CadMaterial.setTabOrder(self.lineEdit_sku, self.lineEdit_descrlonga)
        Form_CadMaterial.setTabOrder(self.lineEdit_descrlonga, self.lineEdit_descrreduzida)
        Form_CadMaterial.setTabOrder(self.lineEdit_descrreduzida, self.lineEdit_frabricante)
        Form_CadMaterial.setTabOrder(self.lineEdit_frabricante, self.lineEdit_codbarean13)
        Form_CadMaterial.setTabOrder(self.lineEdit_codbarean13, self.lineEdit_codfabricante)
        Form_CadMaterial.setTabOrder(self.lineEdit_codfabricante, self.doubleSpinBox_AgrEnt)
        Form_CadMaterial.setTabOrder(self.doubleSpinBox_AgrEnt, self.Combobox_AgrEntr2_2)
        Form_CadMaterial.setTabOrder(self.Combobox_AgrEntr2_2, self.doubleSpinBox)
        Form_CadMaterial.setTabOrder(self.doubleSpinBox, self.Combobox_AgrEntr2)
        Form_CadMaterial.setTabOrder(self.Combobox_AgrEntr2, self.doubleSpinBox_AgrSai)
        Form_CadMaterial.setTabOrder(self.doubleSpinBox_AgrSai, self.Combobox_AgrSai)
        Form_CadMaterial.setTabOrder(self.Combobox_AgrSai, self.lineEdit_Loc1)
        Form_CadMaterial.setTabOrder(self.lineEdit_Loc1, self.lineEdit_Loc2)
        Form_CadMaterial.setTabOrder(self.lineEdit_Loc2, self.lineEdit_Loc3)
        Form_CadMaterial.setTabOrder(self.lineEdit_Loc3, self.lineEdit_Loc4)
        Form_CadMaterial.setTabOrder(self.lineEdit_Loc4, self.graphicsView_fotoitem)
        Form_CadMaterial.setTabOrder(self.graphicsView_fotoitem, self.pushButton_inlcuirfoto)
        Form_CadMaterial.setTabOrder(self.pushButton_inlcuirfoto, self.pushButton_excluirfoto)
        Form_CadMaterial.setTabOrder(self.pushButton_excluirfoto, self.doubleSpinBox_dimA)
        Form_CadMaterial.setTabOrder(self.doubleSpinBox_dimA, self.comboBox_dimunitA)
        Form_CadMaterial.setTabOrder(self.comboBox_dimunitA, self.doubleSpinBox_dimB)
        Form_CadMaterial.setTabOrder(self.doubleSpinBox_dimB, self.comboBox_dimunitB)
        Form_CadMaterial.setTabOrder(self.comboBox_dimunitB, self.doubleSpinBox_dimC)
        Form_CadMaterial.setTabOrder(self.doubleSpinBox_dimC, self.comboBox_dimunitC)
        Form_CadMaterial.setTabOrder(self.comboBox_dimunitC, self.doubleSpinBox_dimD)
        Form_CadMaterial.setTabOrder(self.doubleSpinBox_dimD, self.comboBox_dimunitD)
        Form_CadMaterial.setTabOrder(self.comboBox_dimunitD, self.doubleSpinBox_dimE)
        Form_CadMaterial.setTabOrder(self.doubleSpinBox_dimE, self.comboBox_dimunitE)
        Form_CadMaterial.setTabOrder(self.comboBox_dimunitE, self.doubleSpinBox_dimF)
        Form_CadMaterial.setTabOrder(self.doubleSpinBox_dimF, self.comboBox_dimunitF)
        Form_CadMaterial.setTabOrder(self.comboBox_dimunitF, self.doubleSpinBox_peso)
        Form_CadMaterial.setTabOrder(self.doubleSpinBox_peso, self.graphicsView_desenho)
        Form_CadMaterial.setTabOrder(self.graphicsView_desenho, self.pushButton_incluirdesenho)
        Form_CadMaterial.setTabOrder(self.pushButton_incluirdesenho, self.pushButton_excluirdesenho)
        Form_CadMaterial.setTabOrder(self.pushButton_excluirdesenho, self.plainTextEdit_Observacao)
        Form_CadMaterial.setTabOrder(self.plainTextEdit_Observacao, self.pushButton_Salvar)
        Form_CadMaterial.setTabOrder(self.pushButton_Salvar, self.pushButton_Excluir)

    def retranslateUi(self, Form_CadMaterial):
        _translate = QtCore.QCoreApplication.translate
        Form_CadMaterial.setWindowTitle(_translate("Form_CadMaterial", "Form"))
        self.label_20.setText(_translate("Form_CadMaterial", "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Item</span></p></body></html>"))
        self.label_8.setText(_translate("Form_CadMaterial", "<html><head/><body><p align=\"right\">Agrupamento de entrada</p></body></html>"))
        self.pushButton_excluirfoto.setText(_translate("Form_CadMaterial", "Excluir"))
        self.label_14.setText(_translate("Form_CadMaterial", "<html><head/><body><p align=\"right\">Localização</p></body></html>"))
        self.label_3.setText(_translate("Form_CadMaterial", "<html><head/><body><p align=\"right\">Descrição longa</p></body></html>"))
        self.label_17.setText(_translate("Form_CadMaterial", "<html><head/><body><p align=\"right\">Descrição reduzida</p></body></html>"))
        self.label_13.setText(_translate("Form_CadMaterial", "<html><head/><body><p align=\"right\">Agrupamento de saída</p></body></html>"))
        self.label_2.setText(_translate("Form_CadMaterial", "<html><head/><body><p align=\"right\">Cod. Fabr.</p></body></html>"))
        self.checkBox_restrito.setText(_translate("Form_CadMaterial", "Item restrito"))
        self.pushButton_inlcuirfoto.setText(_translate("Form_CadMaterial", "Incluir"))
        self.label_18.setText(_translate("Form_CadMaterial", "<html><head/><body><p align=\"right\">Cód. Barra</p></body></html>"))
        self.label_16.setText(_translate("Form_CadMaterial", "<html><head/><body><p align=\"right\">Grupo</p></body></html>"))
        self.label.setText(_translate("Form_CadMaterial", "<html><head/><body><p align=\"right\">Fabricante</p></body></html>"))
        self.checkBox_ativo.setText(_translate("Form_CadMaterial", "Item ativo"))
        self.pushButton_busca.setText(_translate("Form_CadMaterial", "Buscar"))
        self.pushButton_Salvar.setText(_translate("Form_CadMaterial", "Salvar"))
        self.pushButton_Excluir.setText(_translate("Form_CadMaterial", "Excluir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form_CadMaterial", "Dados de cadastro"))
        self.label_11.setText(_translate("Form_CadMaterial", "Dimensão E"))
        self.label_12.setText(_translate("Form_CadMaterial", "Peso padrão"))
        self.label_9.setText(_translate("Form_CadMaterial", "Dimensão F"))
        self.label_6.setText(_translate("Form_CadMaterial", "Dimensão A"))
        self.label_7.setText(_translate("Form_CadMaterial", "Dimensão C"))
        self.label_5.setText(_translate("Form_CadMaterial", "Dimensão B"))
        self.label_10.setText(_translate("Form_CadMaterial", "Dimensão D"))
        self.label_4.setText(_translate("Form_CadMaterial", "Valor"))
        self.label_15.setText(_translate("Form_CadMaterial", "Unidade"))
        self.label_19.setText(_translate("Form_CadMaterial", "Kg"))
        self.pushButton_incluirdesenho.setText(_translate("Form_CadMaterial", "Incluir"))
        self.pushButton_excluirdesenho.setText(_translate("Form_CadMaterial", "Excluir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form_CadMaterial", "Características físicas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form_CadMaterial", "Observação"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_CadMaterial = QtWidgets.QWidget()
    ui = Ui_Form_CadMaterial()
    ui.setupUi(Form_CadMaterial)
    Form_CadMaterial.show()
    sys.exit(app.exec_())
