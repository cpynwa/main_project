import sys
import re
import ipcalc
from PyQt5.QtWidgets import *


class ConfigFinder(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.setWindowTitle('Config_Finder')
        self.setGeometry(300, 300, 1400, 700)
        self.show()

        #파일 열기
        self.filename = QLineEdit()
        self.openButton = QPushButton('열기')
        self.openButton.clicked.connect(self.openButtonClicked)

        # 오른쪽 창
        self.search_input = QLineEdit()
        self.search_input.returnPressed.connect(self.searchButtonClicked)
        self.search_output = QTextEdit()
        self.searchButton = QPushButton('실행')
        self.searchButton.clicked.connect(self.searchButtonClicked)

        # 왼쪽창
        self.interface_input = QLineEdit()
        self.interface_input.returnPressed.connect(self.excuteButtonClicked)
        self.result_output = QTextEdit()
        self.excuteButton = QPushButton('실행')
        self.excuteButton.clicked.connect(self.excuteButtonClicked)

        grid.addWidget(QLabel('File:'), 0, 0)
        grid.addWidget(QLabel('Search:'), 1, 0)
        grid.addWidget(QLabel('Result:'), 2, 0)

        grid.addWidget(self.filename, 0, 1)
        grid.addWidget(self.openButton, 0, 2)

        grid.addWidget(self.search_input, 1, 1)
        grid.addWidget(self.searchButton, 1, 2)
        grid.addWidget(self.interface_input, 1, 3)
        grid.addWidget(self.excuteButton, 1, 4)

        grid.addWidget(self.search_output, 2, 1)
        grid.addWidget(self.result_output, 2, 3)

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

    def excuteButtonClicked(self):
        filename = self.filename.text()
        interface_name = self.interface_input.text()
        if filename and interface_name:
            result = self.config_finder(filename, interface_name)
            result1 = "\n".join(result)
            self.result_output.setText(result1)
        else:
            self.result_output.setText("읽어올 파일경로와 인터페이스를 입력하세요.")

    def searchButtonClicked(self):
        filename = self.filename.text()
        search = self.search_input.text()
        if filename and search:
            result = self.config_finder(filename, search)
            result1 = "\n".join(result)
            self.search_output.setText(result1)
        else:
            self.search_output.setText("읽어올 파일경로와 인터페이스를 입력하세요.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ConfigFinder()
    sys.exit(app.exec_())