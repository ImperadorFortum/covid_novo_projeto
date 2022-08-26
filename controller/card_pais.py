from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from model.pais import Pais 

FILE_UI = 'view/card_pais.ui'


class CardPais(QWidget):
    def __init__(self, p: Pais): 
        super(CardPais, self).__init__()
        uic.loadUi(FILE_UI,self)
        self.p = p 

        self.loadData()

    def loadData(self):
        self.titulo.setText(f'Status {self.p.country}')
        self.confirmados.Text.setText(f'{self.p.confirmed} Confirmados')
        