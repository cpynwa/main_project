import sys
from PyQt5.QtWidgets import *
from config_finder.config_finder import ConfigFinder

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Network_Utility')
        self.setGeometry(200, 100, 1400, 900)

        self.dialog = QDialog()

        self.Config_Finder_Button = QPushButton('Config_Finder')

        self.Netconf_Test_Button = QPushButton('Netconf_Test')

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.Config_Finder_Button, 0, 0)
        grid.addWidget(self.Netconf_Test_Button, 0, 1)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())