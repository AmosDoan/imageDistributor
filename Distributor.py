from os import mkdir
import random
import shutil

class Distributor:
    def distribute(self, files, sourcePath, targetDirPath, numberOfDirectory):
        random.shuffle(files)

        targetPaths = [targetDirPath + "/" + str(i) for i in range(1, numberOfDirectory + 1)]
        for path in targetPaths:
            mkdir(path)

        i = 0
        for file in files:
            sourceFile = sourcePath + "/" + file
            copyFile = targetPaths[i]
            shutil.copy2(sourceFile, copyFile)

            i = (i + 1) % len(targetPaths)
