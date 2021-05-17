import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from config_finder.config_finder import ConfigFinder
from netconf_tester.netconf_test import NetconfTest
from optic_finder.optic_finder import OpticFinder

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Network_Utility')
        self.setGeometry(200, 100, 1400, 900)

        self.Config_Finder_Button = QPushButton('Config_Finder')
        self.Config_Finder_Button.clicked.connect(self.Click_Config_Finder)
        self.Netconf_Test_Button = QPushButton('Netconf_Test')
        self.Netconf_Test_Button.clicked.connect(self.Click_Netconf_Test)
        self.Optic_Finder_Button = QPushButton('Optic_Finder_Test')
        self.Optic_Finder_Button.clicked.connect(self.Click_Optic_Finder)


        grid = QGridLayout()
        grid.addWidget(self.Config_Finder_Button, 0, 0)
        grid.addWidget(self.Netconf_Test_Button, 0, 1)
        grid.addWidget(self.Optic_Finder_Button, 1, 0)

        centralWidget = QWidget()
        centralWidget.setLayout(grid)
        self.setCentralWidget(centralWidget)


    def Click_Config_Finder(self):
        win = ConfigFinder()
        win.showModal()

    def Click_Netconf_Test(self):
        win = NetconfTest()
        win.showModal()

    def Click_Optic_Finder(self):
        win = OpticFinder()
        win.showModal()

    # def show(self):
    #     super().show()