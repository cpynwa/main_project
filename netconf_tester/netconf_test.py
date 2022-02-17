from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import *
from lxml import etree
from PyQt5.QtWidgets import *

#class NetconfTest(QWidget):
class NetconfTest(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('netconf_test')
        self.setGeometry(300, 300, 1400, 700)

        #정보입력 창
        self.ip = QLineEdit()
        self.id = QLineEdit()
        self.pw = QLineEdit()
        self.pw.setEchoMode(QLineEdit.Password)
        self.input = QTextEdit()
        self.result = QTextEdit()
        self.compareButton = QPushButton('compare')
        self.compareButton.setAutoDefault(False)
        self.commitcheckButton = QPushButton('commit check')
        self.commitcheckButton.setAutoDefault(False)
        self.commitButton = QPushButton('commit')
        self.commitButton.setAutoDefault(False)
        self.cliButton = QPushButton('cli send')
        self.cliButton.setAutoDefault(False)

        Line1 = QHBoxLayout()
        Line1.addWidget(QLabel('IP:'))
        Line1.addWidget(self.ip)
        Line1.addWidget(QLabel('ID:'))
        Line1.addWidget(self.id)
        Line1.addWidget(QLabel('PW:'))
        Line1.addWidget(self.pw)

        Line2 = QHBoxLayout()
        Line2.addWidget(QLabel('명령어:'))
        Line2.addWidget(self.input)

        Line3 = QHBoxLayout()
        Line3.addWidget(QLabel('결  과:'))
        Line3.addWidget(self.result)

        right_button = QVBoxLayout()
        right_button.addWidget(self.compareButton)
        right_button.addWidget(self.commitcheckButton)
        right_button.addWidget(self.commitButton)
        right_button.addWidget(self.cliButton)

        input_layout = QVBoxLayout()
        input_layout.addLayout(Line1)
        input_layout.addLayout(Line2)
        input_layout.addLayout(Line3)

        all_layout = QGridLayout()
        all_layout.addLayout(input_layout, 0, 0)
        all_layout.addLayout(right_button, 0, 1)

        self.setLayout(all_layout)

        # TextEdit과 관련된 버튼에 기능 연결
        self.compareButton.clicked.connect(self.compare_button)
        self.commitcheckButton.clicked.connect(self.check_button)
        self.commitButton.clicked.connect(self.commit_button)
        self.cliButton.clicked.connect(self.cli_button)

    def compare_button(self):
        source = self.input.toPlainText()
        ip = self.ip.text()
        id = self.id.text()
        pw = self.pw.text()
        dev = Device(host=str(ip), user=str(id), password=str(pw)).open()

        with Config(dev, mode='private') as cu:
            try:
                cu.load(source, format='set')
                result = cu.diff()
                self.result.setText(result)
            except ConfigLoadError as err:
                self.result.setText(str(err))

    def check_button(self):
        source = self.input.toPlainText()
        ip = self.ip.text()
        id = self.id.text()
        pw = self.pw.text()
        dev = Device(host=ip, user=id, password=pw).open()
        try:
            with Config(dev, mode='private') as cu:
                try:
                    cu.load(source, format='set')
                    cu.commit_check()
                    self.result.setText("configuration check succeeds")
                except Exception as err:
                    self.result.setText(str(err))
                # except ConfigLoadError as err:
                #     self.result.setText(str(err))
                # except CommitError as comerr:
                #     self.result.setText(str(comerr))
        except Exception as cerr:
            self.result.setText(str(cerr))

    def commit_button(self):
        source = self.input.toPlainText()
        ip = self.ip.text()
        id = self.id.text()
        pw = self.pw.text()
        dev = Device(host=ip, user=id, password=pw).open()
        with Config(dev, mode='private') as cu:
            try:
                cu.load(source, format='set')
                cu.commit()
                self.result.setText("commit complete")
            except ConfigLoadError as err:
                self.result.setText(str(err))
            except CommitError as comerr:
                self.result.setText(str(comerr))

    def cli_button(self):
        source = self.input.toPlainText()
        ip = self.ip.text()
        id = self.id.text()
        pw = self.pw.text()
        with Device(host=ip, user=id, password=pw) as dev:
            try:
                result = dev.rpc.cli(command=source)
                self.result.setText(str(etree.tounicode(result)))
            except ConfigLoadError as err:
                self.result.setText(str(err))
            except CommitError as comerr:
                self.result.setText(str(comerr))

    def showModal(self):
        return super().exec_()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = NetconfTest()
#     ex.show()
#     sys.exit(app.exec_())