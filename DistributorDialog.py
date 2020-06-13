from PyQt5 import QtCore
from PyQt5.QtCore import QThreadPool
from PyQt5.QtWidgets import *

from Distributor import Distributor


class DistributorDialog(QDialog):

    def __init__(self, files, sourcePath, targetDirPath, instagramIdList):
        super().__init__()
        self.files = files
        self.sourcePath = sourcePath
        self.targetDirPath = targetDirPath
        self.instagramIdList = instagramIdList
        self.setupUI()

    def setupUI(self):
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.setGeometry(800, 200, 800, 500)
        self.setFixedSize(400, 100)
        self.setWindowTitle("ImageDistributor Processing")
        self.progress = QLabel("진행 중")

        layout = QGridLayout()
        layout.addWidget(self.progress, 0, 0)

        self.setLayout(layout)
        self.distributor = Distributor(self.progress, self.files, self.sourcePath, self.targetDirPath,
                                       self.instagramIdList)

    def exec_(self):
        QThreadPool.globalInstance().start(self.distributor)
        super().exec_()
