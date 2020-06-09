from os import mkdir
import random
import shutil

class Distributor:
    def distribute(self, files, sourcePath, targetDirPath, instagramIdList):
        random.shuffle(files)

        targetPaths = [targetDirPath + "/" + instagramId for instagramId in instagramIdList]
        targetIndex = [0] * len(targetPaths)
        for path in targetPaths:
            mkdir(path)

        i = 0
        for file in files:
            fileExtension = file.split('.')[1]
            sourceFile = sourcePath + "/" + file
            copyFile = targetPaths[i] + "/" + instagramIdList[i] + str(targetIndex[i]) + '.' + fileExtension
            shutil.copy2(sourceFile, copyFile)
            targetIndex[i] = targetIndex[i] + 1

            i = (i + 1) % len(targetPaths)
