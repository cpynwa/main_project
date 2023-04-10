import sys
from os import remove, path
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QTextEdit, QGridLayout, QLabel, QFileDialog, QApplication, QComboBox, QDialog
from forti_main import forti_search


#class fortiWindow(QWidget):
class fortiWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('forti')
        #self.setGeometry(100, 100, 800, 800)

        # 파일 열기
        self.filename = QLineEdit()
        self.openButton = QPushButton('열기')
        self.openButton.clicked.connect(self.openButtonClicked)
        self.openButton.setAutoDefault(False)

        # 검색
        self.search_input = QLineEdit()
        self.search_input.returnPressed.connect(self.searchButtonClicked)
        self.searchButton = QPushButton('실행')
        self.searchButton.clicked.connect(self.searchButtonClicked)
        self.searchButton.setAutoDefault(False)

        # 옵션 선택
        self.option_combobox = QComboBox()
        self.option_combobox.addItem('policy')
        self.option_combobox.addItem('address')

        # 결과화면
        self.search_output = QTextEdit()

        grid = QGridLayout()
        grid.addWidget(QLabel('File:'), 0, 0)
        grid.addWidget(self.filename, 0, 1)
        grid.addWidget(self.openButton, 0, 2)

        grid.addWidget(QLabel('Search:'), 1, 0)
        grid.addWidget(self.search_input, 1, 1)
        grid.addWidget(self.searchButton, 1, 2)

        grid.addWidget(QLabel('Select:'), 2, 0)
        grid.addWidget(self.option_combobox, 2, 1)

        grid.addWidget(QLabel('Result:'), 3, 0)
        grid.addWidget(self.search_output, 3, 1)

        self.setLayout(grid)

    def openButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.filename.setText(fname[0])

    def searchButtonClicked(self):
        filename = self.filename.text()
        search = self.search_input.text()
        select_option = self.option_combobox.currentText()
        if filename and search:
            forti_search(filename, search, select_option)
            with open("result.txt", "r") as result_file:
                result = result_file.read()
            self.search_output.setText(result)

            # 분류작업시 생성된 불필요 파일 삭제
            if path.isfile("result.txt"):
                remove("result.txt")
            else:
               pass

            if path.isfile('search_file.txt'):
                remove("search_file.txt")
            else:
                pass

        else:
            self.search_output.setText("읽어올 파일경로 또는 검색어를 입력하세요.")

    def showModal(self):
        return super().exec_()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MainWindow()
#     ex.show()
#     sys.exit(app.exec_())