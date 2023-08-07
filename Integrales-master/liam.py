import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication

class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # Cargando la interfaz desde tu ruta
        uic.loadUi(r"c:\Users\Admin\OneDrive\Escritorio\Integrales\Integrales-master\interfaz.ui", self)
        # Print
        self.btnCalcular.clicked.connect(self.hola)
        # Añadiendo iconos a botones
        self.btnIntegralDef.setIcon(QIcon(r"c:\Users\Admin\OneDrive\Escritorio\Integrales\Integrales-master\assets\IntegralDefinida.png"))
        self.btnIntegral.setIcon(QIcon(r"c:\Users\Admin\OneDrive\Escritorio\Integrales\Integrales-master\assets\Integral.png"))
        self.btnDerivada.setIcon(QIcon(r"c:\Users\Admin\OneDrive\Escritorio\Integrales\Integrales-master\assets\Derivada.png"))
        # Botones
        self.btnC.clicked.connect(self.limpiar)

        # Variable para almacenar el contenido de la pantalla
        self.pantalla = ""

        # Conectar botones 1, 2, 3, 4 y 5 a sus funciones correspondientes
        self.btn1.clicked.connect(lambda: self.agregar_contenido("1"))
        self.btn2.clicked.connect(lambda: self.agregar_contenido("2"))
        self.btn3.clicked.connect(lambda: self.agregar_contenido("3"))
        self.btn4.clicked.connect(lambda: self.agregar_contenido("4"))
        self.btn5.clicked.connect(lambda: self.agregar_contenido("5"))

    # Modificaciones para agregar funcionalidad a los botones 1, 2, 3, 4 y 5
    def agregar_contenido(self, valor):
        self.pantalla += valor
        self.textEdit.setText(self.pantalla)

    def limpiar(self):
        self.pantalla = ""
        self.textEdit.setText("")

    def hola(self):
        print("Hola mundo")


