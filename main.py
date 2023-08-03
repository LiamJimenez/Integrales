import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication

## Clase de QMainWindow
class Ventana(QMainWindow):
    ## Constructor de ventanas
     def __init__(self):
         QMainWindow.__init__(self)
         ## Cargando la interfaz
         uic.loadUi(r"C:\Users\msnlo\Documents\practice\proyectoPy\interfaz.ui", self) 
         ##Print
         self.btnCalcular.clicked.connect(self.hola)
         ## Anadiendo iconos a botnones
         self.btnIntegralDef.setIcon(QIcon(r"C:\Users\msnlo\Documents\practice\proyectoPy\assets\IntegralDefinida.png"))
         self.btnIntegral.setIcon(QIcon(r"C:\Users\msnlo\Documents\practice\proyectoPy\assets\Integral.png"))
         self.btnDerivada.setIcon(QIcon(r"C:\Users\msnlo\Documents\practice\proyectoPy\assets\Derivada.png"))
          ## Botones
        
        # Limpiar con Boton C
         self.btnC.clicked.connect(self.limpiar)
        
        ##Funciones
     def limpiar(self): 
      self.textEdit.setText("")   
         
     def hola(self): 
        print(" Hola mundo")
     
        
## Inicializar la ventana
app = QApplication(sys.argv)
GUI = Ventana()
GUI.show()
app.exec_()
          