import sys
import re
import ipcalc
from PyQt5.QtWidgets import *

class ConfigFinder(QWidget):
#class ConfigFinder(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Config_Finder')
        self.setGeometry(300, 300, 1400, 700)

        #파일 열기
        self.filename = QLineEdit()
        self.openButton = QPushButton('열기')
        self.openButton.clicked.connect(self.openButtonClicked)
        self.openButton.setAutoDefault(False)


        # 오른쪽 창
        self.search1_input = QLineEdit()
        self.search1_input.returnPressed.connect(self.search1ButtonClicked)
        self.search1_output = QTextEdit()
        self.search1Button = QPushButton('실행')
        self.search1Button.clicked.connect(self.search1ButtonClicked)
        self.search1Button.setAutoDefault(False)

        # 왼쪽창
        self.search2_input = QLineEdit()
        self.search2_input.returnPressed.connect(self.search2ButtonClicked)
        self.search2_output = QTextEdit()
        self.search2Button = QPushButton('실행')
        self.search2Button.clicked.connect(self.search2ButtonClicked)
        self.search2Button.setAutoDefault(False)

        grid = QGridLayout()
        grid.addWidget(QLabel('File:'), 0, 0)
        grid.addWidget(QLabel('Search:'), 1, 0)
        grid.addWidget(QLabel('Result:'), 2, 0)

        grid.addWidget(self.filename, 0, 1)
        grid.addWidget(self.openButton, 0, 2)

        grid.addWidget(self.search1_input, 1, 1)
        grid.addWidget(self.search1Button, 1, 2)
        grid.addWidget(self.search2_input, 1, 3)
        grid.addWidget(self.search2Button, 1, 4)

        grid.addWidget(self.search1_output, 2, 1)
        grid.addWidget(self.search2_output, 2, 3)

        self.setLayout(grid)

    def openButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.filename.setText(fname[0])

    def config_finder(self, filename, interface_name):
        with open(filename, "r") as file:
            all_config = file.readlines()

        lines = list(map(lambda s: s.strip(), all_config))
        set_config_list = [line for line in lines if re.match(f'^set ', line)]
        config_list = [line for line in set_config_list if re.match(f'.*{interface_name}.*', line)]

        for line in config_list:
            if re.match(r'.*inet address.*', line):
                ipv4 = line.split()[8]
            elif re.match(r'.*inet6 address.*', line):
                ipv6 = line.split()[8]
        try:
            for network in ipcalc.Network(ipv4):
                if network == ipv4:
                    continue
                else:
                    config_list = config_list + [line for line in set_config_list if re.match(f'(.*{network}.*)', line)]
                    # for line in set_config_list:
                    #     if re.match(f'(.*{network}.*)', line):
                    #         config_list.append(line)
            for network in ipcalc.Network(ipv6):
                ipv6_comp = network.to_compressed()
                if network == ipv6:
                    continue
                else:
                    config_list = config_list + [line for line in set_config_list if re.match(f'(.*{ipv6_comp}.*)', line)]
        except:
            pass

        return config_list

    def search1ButtonClicked(self):
        filename = self.filename.text()
        search1 = self.search1_input.text()
        if filename and search1:
            result = self.config_finder(filename, search1)
            result1 = "\n".join(result)
            self.search1_output.setText(result1)
        else:
            self.search1_output.setText("읽어올 파일경로와 인터페이스를 입력하세요.")

    def search2ButtonClicked(self):
        filename = self.filename.text()
        search2 = self.search2_input.text()
        if filename and search2:
            result = self.config_finder(filename, search2)
            result1 = "\n".join(result)
            self.search2_output.setText(result1)
        else:
            self.search2_output.setText("읽어올 파일경로와 인터페이스를 입력하세요.")


    # def showModal(self):
    #     return super().exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ConfigFinder()
    ex.show()
    sys.exit(app.exec_())