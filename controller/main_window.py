from random import randint
from PyQt5.QtWidgets import QMainWindow 
from PyQt5 import uic 
from controller.card_pais import CardPais

from model.pais import Pais

FILE_UI ='view/MainWindow.ui'


class MainWindow(QMainWindow): 

    def __init__(self): 
        super(MainWindow, self). __init__()
        uic.loadUi(FILE_UI, self)

        self.updateData.clicked.connect(self.updateDataCovid)

        def updateDataCovid(self):
         """ 
            1 - Acessar a API e baixar/atualizar os dados do banco de dados
            2 - Pegar os dados a partir do banco de dados
            3 - Limpar a tabela
            4 - Carregar os dados na tabela
            5 - Preencher os card com 5 países aleatório   
         """ 
         # limpar tabela
        self.tableEstados.clear()

        self.addEstados()

        # Limpa os cards
        self.clearCardFrame()
        for i in range(5):
            p = Pais(f'Pais {i}', randint(1, 99), randint(1, 99), randint(
                1, 99), randint(1, 99), '2020-03-18T23:00:00.000Z')

            card = CardPais(p)
            self.cardContainer.addWidget(card)

    def addEstados(self):
        pass

    def clearCardFrame(self):
        for i in range(self.cardContainer.count()):
            card = self.cardContainer.itemAt(i).widget()
            card.hide()   
