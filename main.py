import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication

# main.py 
from Calculator import Ventana

### integral[1,2]   "   "" "
##Operaciones = ["pi", "2", "3"]
##  integral()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Ventana()
    GUI.show()
    sys.exit(app.exec_())



          