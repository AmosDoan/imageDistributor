from os import listdir
from os.path import isfile, join

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from DistributorDialog import DistributorDialog


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 800, 500)
        self.setFixedSize(800, 500)
        self.setWindowTitle("Image Distributor v0.0.3 For UHwan")
        self.setWindowIcon(QIcon("resources/imageDistributor.ico"))

        self.sourceDirectorySelectButton = QPushButton("이미지 폴더 선택")
        self.sourceDirectorySelectButton.clicked.connect(self.sourceDirectorySelectButtonClicked)

        self.targetDirectorySelectButton = QPushButton("타겟 폴더 선택")
        self.targetDirectorySelectButton.clicked.connect(self.targetDirectorySelectButtonClicked)

        self.sourceDirectoryLabel = QLabel("선택된 이미지 폴더 : ")
        self.targetDirectoryLabel = QLabel("선택된 타겟 폴더 : ")

        self.instagramIdLabel = QLabel("인스타 그램 계정 명 - 콤마(,)로 구분 : ")
        self.instagramId = QLineEdit()
        self.numberOfFiles = QLabel("분배할 파일 수 : 0")

        self.startButton = QPushButton("생성하기")
        self.startButton.clicked.connect(self.startButtonClicked)

        layout = QGridLayout()
        layout.addWidget(self.sourceDirectoryLabel, 0, 0, 1, 2)
        layout.addWidget(self.targetDirectoryLabel, 1, 0, 1, 2)
        layout.addWidget(self.instagramIdLabel, 2, 0)
        layout.addWidget(self.instagramId, 2, 1, 1, 2)
        layout.addWidget(self.numberOfFiles, 3, 0)
        layout.addWidget(self.sourceDirectorySelectButton, 4, 0)
        layout.addWidget(self.targetDirectorySelectButton, 4, 1)
        layout.addWidget(self.startButton, 4, 2)

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
        self.numberOfFiles.setText("분배할 파일 수 : " + str(len(self.files)))
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

        instagramIdList = self.instagramId.text().split(',')
        numberOfDirectory = len(instagramIdList)
        if numberOfDirectory > len(self.files):
            msg = QMessageBox()
            msg.setText("인스타그램 계정 수는 파일 수보다 클 수 없습니다. ")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

        for instagramId in instagramIdList:
            if instagramId == '':
                msg = QMessageBox()
                msg.setText("공백인 인스타그램 계정이 있습니다.")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return

        distributorDialog = DistributorDialog(self.files, self.sourceDir, self.targetDir, instagramIdList)
        distributorDialog.exec_()
