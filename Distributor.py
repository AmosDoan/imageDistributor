from os import mkdir
import random
import shutil

class Distributor:
    def distribute(self, files, sourcePath, targetDirPath, instagramIdList):
        random.shuffle(files)

        targetPaths = [targetDirPath + "/" + instagramId for instagramId in instagramIdList]
        for path in targetPaths:
            mkdir(path)

        i = 0
        for file in files:
            sourceFile = sourcePath + "/" + file
            copyFile = targetPaths[i]
            shutil.copy2(sourceFile, copyFile)

            i = (i + 1) % len(targetPaths)
