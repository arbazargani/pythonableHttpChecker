import sys, requests
from datetime import datetime, timedelta
from balloontip import balloon_tip

from PyQt6.QtCore import QSize, Qt
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow, QPushButton, QPlainTextEdit


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    __historyTextBox = None
    __dispatchBtn = None

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Prime Dashboard")
        self.setWindowIcon(QtGui.QIcon('rss.png'))

        self.resize(QSize(1000, 400))

        # Set the central widget of the Window.
        self.setCentralWidget(self.initButton())
        # self.setCentralWidget(self.initHistory())

        layout = QVBoxLayout()

        layout.addWidget(self.initButton())
        layout.addWidget(self.initHistory())
        

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def initButton(self):
        button = QPushButton("Check status code")
        button.setFixedSize(120, 60)
        button.clicked.connect(self.handleButtonClick)
        self.__dispatchBtn = button
        return button

    def initHistory(self):
        textarea = QPlainTextEdit()
        textarea.setReadOnly(True)
        textarea.resize(100,380)
        self.__historyTextBox = textarea
        return textarea
        
    def handleButtonClick(self):
        start_time =  datetime.now()
        self.__dispatchBtn.setText('Saying hello to server ...')
        start_time_formatted = start_time.strftime('%Y-%m-%d %H:%M:%S')
        self.__historyTextBox.insertPlainText('request initiated.\n')

        req = Request().boot('https://rokna.net/').appendURI('feeds').bootPayload(None).send()
        timeTaken = datetime.now() - start_time

        self.__dispatchBtn.setText('Check status code')
        res = req.response()
        
        code = str(res.status_code)
        length = str(len(res.content))
        self.__historyTextBox.insertPlainText( start_time_formatted + ' ___ code ' + code + ' ___ len ' + length + ' bytes \n')
        print ('request finished.')


# boot request with instance of this class and her methods
class Request():

    url = None
    payload = None
    res = None

    def __init__(self):
        # balloon_tip('Booting request ...', 'to check response, head back to application.')
        print ('request initiated.')

    def boot(self, url):
        self.url = url
        return self
    
    def appendURI(self, uri):
        self.url += uri
        return self
    
    def bootPayload(self, payload):
        self.payload = payload
        return self
    
    def send(self):
        self.res = requests.get(self.url)
        return self
    
    def response(self):
        return self.res

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()