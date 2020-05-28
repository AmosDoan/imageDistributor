import sys
from Window import Window
from Distributor import Distributor
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    distributor = Distributor()
    window = Window(distributor)
    window.show()
    app.exec_()
