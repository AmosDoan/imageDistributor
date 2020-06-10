import random
import shutil
from os import mkdir

from PyQt5.QtCore import QRunnable


class Distributor(QRunnable):

    def __init__(self, progress, files, sourcePath, targetDirPath, instagramIdList):
        QRunnable.__init__(self)
        self.progress = progress
        self.files = files
        self.sourcePath = sourcePath
        self.targetDirPath = targetDirPath
        self.instagramIdList = instagramIdList

    def run(self):
        random.shuffle(self.files)

        targetPaths = [self.targetDirPath + "/" + instagramId for instagramId in self.instagramIdList]
        targetIndex = [0] * len(targetPaths)

        try:
            for path in targetPaths:
                mkdir(path)
        except FileExistsError:
            self.progress.setText("실패 - 이미 폴더가 존재합니다.")
            return

        i = 0
        for file in self.files:
            fileExtension = file.split('.')[1]
            sourceFile = self.sourcePath + "/" + file
            copyFile = targetPaths[i] + "/" + self.instagramIdList[i] + str(targetIndex[i]) + '.' + fileExtension
            shutil.copy2(sourceFile, copyFile)
            targetIndex[i] = targetIndex[i] + 1

            i = (i + 1) % len(targetPaths)

        self.progress.setText("완료")
