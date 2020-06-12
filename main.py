import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

from geruniforme import GerUniforme

import time
#===== Conexão ao banco de dados =====#
import sqlite3
conn = sqlite3.connect('abn.db')
cursor = conn.cursor()
#=====================================#
  
class MainWindow(QtWidgets.QMainWindow):
    
    
    def show_geruniforme(self):
        self.geruniforme.show()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("PainelABN.ui", self)
        # ===== Tela de gerencimento de uniformes =====#
        self.geruniforme = GerUniforme(self)
        self.actionUniforme.triggered.connect(self.show_geruniforme)
        # =============================================#
     

app = QtWidgets.QApplication(sys.argv)
inicio = MainWindow()
inicio.show()




app.exec_()

