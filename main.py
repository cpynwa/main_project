import sys
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QTextEdit, QGridLayout, QLabel, QFileDialog, QApplication, QComboBox



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('create vlan')

        grid = QGridLayout()

        # 장비 수량
        grid.addWidget(QLabel('Number of Deivce :'), 0, 0)

        #self.number_of_deivce = QLineEdit()
        #grid.addWidget(self.number_of_deivce, 0, 1)

        # # 장비 1
        # grid.addWidget(QLabel('Device 1 :'), 1, 0)
        #
        # self.hostname = QLineEdit()
        # grid.addWidget(self.hostname, 1, 1)
        #
        # self.username = QLineEdit()
        # grid.addWidget(self.username, 1, 2)
        #
        # self.password = QLineEdit()
        # grid.addWidget(self.password, 1, 3)
        #
        # self.interfaces = QLineEdit()
        # grid.addWidget(self.interfaces, 1, 4)

    def showModal(self):
        return super().exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
