from os import listdir
from os.path import isfile, join
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, distributor):
        self.distributor = distributor
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        self.setWindowTitle("Image Distributor v0.0.1 For UHwan")

        self.sourceDirectorySelectButton = QPushButton("이미지 폴더 선택")
        self.sourceDirectorySelectButton.clicked.connect(self.sourceDirectorySelectButtonClicked)

        self.targetDirectorySelectButton = QPushButton("타겟 폴더 선택")
        self.targetDirectorySelectButton.clicked.connect(self.targetDirectorySelectButtonClicked)

        self.sourceDirectoryLabel = QLabel("선택된 이미지 폴더 : ")
        self.targetDirectoryLabel = QLabel("선택된 타겟 폴더 : ")

        self.numberOfDirectory = QLineEdit()
        self.numberOfDirectory.setValidator(QIntValidator())

        self.numberOfImageFilesLabel = QLabel("분배할 파일 수 : ")

        self.startButton = QPushButton("생성하기")
        self.startButton.clicked.connect(self.startButtonClicked)

        layout = QVBoxLayout()
        layout.addWidget(self.sourceDirectorySelectButton)
        layout.addWidget(self.targetDirectorySelectButton)
        layout.addWidget(self.sourceDirectoryLabel)
        layout.addWidget(self.targetDirectoryLabel)
        layout.addWidget(self.numberOfImageFilesLabel)
        layout.addWidget(self.numberOfDirectory)
        layout.addWidget(self.startButton)

        self.setLayout(layout)

        # Member variable initialize
        self.sourceDir = ""
        self.targetDir = ""
        self.files = list()


    def sourceDirectorySelectButtonClicked(self):
        self.sourceDir = str(QFileDialog.getExistingDirectory(self, "이미지 있는 파일을 고르셈"))
        if self.sourceDir == "":
            return

        self.files = [f for f in listdir(self.sourceDir) if isfile(join(self.sourceDir, f))]
        self.numberOfImageFilesLabel.setText("분배할 파일 수 : " + str(len(self.files)))
        self.sourceDirectoryLabel.setText("선택된 이미지 폴더 : " + self.sourceDir)


    def targetDirectorySelectButtonClicked(self):
        self.targetDir = str(QFileDialog.getExistingDirectory(self, "이미지 있는 파일을 고르셈"))
        if self.targetDir == "":
            return

        self.targetDirectoryLabel.setText("선택된 타겟 폴더 : " + self.targetDir)


    def startButtonClicked(self):
        if self.sourceDir == "" or self.targetDir == "":
            msg = QMessageBox()
            msg.setText("경로가 지정되어 있지 않습니다. ")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

        numberOfDirectory = int(self.numberOfDirectory.text())
        if numberOfDirectory > len(self.files):
            msg = QMessageBox()
            msg.setText("폴더 수는 파일 수보다 클 수 없습니다. ")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

        self.distributor.distribute(self.files, self.sourceDir, self.targetDir, numberOfDirectory)

