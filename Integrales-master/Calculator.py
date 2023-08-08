import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication

class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # Cargando la interfaz desde tu ruta
        uic.loadUi(r"c:\Users\Admin\OneDrive\Escritorio\Integrales_Proyect\Integrales-master\interfaz.ui", self)
        # Print
        self.btnCalcular.clicked.connect(self.hola)
        # Añadiendo iconos a botones
        self.btnIntegralDef.setIcon(QIcon(r"c:\Users\Admin\OneDrive\Escritorio\Integrales_Proyect\Integrales-master\assets\IntegralDefinida.png"))
        self.btnIntegral.setIcon(QIcon(r"c:\Users\Admin\OneDrive\Escritorio\Integrales_Proyect\Integrales-master\assets\Integral.png"))
        self.btnDerivada.setIcon(QIcon(r"c:\Users\Admin\OneDrive\Escritorio\Integrales_Proyect\Integrales-master\assets\Derivada.png"))
        # Botones
        self.btnC.clicked.connect(self.eliminar_caracter)
        self.btnCA.clicked.connect(self.limpiar_todo)

        # Variable para almacenar el contenido de la pantalla
        self.pantalla = ""

        #Botones de Liam
        self.btn1.clicked.connect(lambda: self.agregar_contenido("1"))
        self.btn2.clicked.connect(lambda: self.agregar_contenido("2"))
        self.btn3.clicked.connect(lambda: self.agregar_contenido("3"))
        self.btn4.clicked.connect(lambda: self.agregar_contenido("4"))
        self.btn5.clicked.connect(lambda: self.agregar_contenido("5"))

        #Botones de Hilari
        self.btnY.clicked.connect(lambda: self.agregar_contenido("Y"))
        self.btnX.clicked.connect(lambda: self.agregar_contenido("X"))
        self.btnSuma.clicked.connect(lambda: self.agregar_contenido("+"))
        self.btnResta.clicked.connect(lambda: self.agregar_contenido("-"))
        self.btnMultiplicar.clicked.connect(lambda: self.agregar_contenido("*"))
        self.btnDividir.clicked.connect(lambda: self.agregar_contenido("÷"))
        self.btnRaiz.clicked.connect(lambda: self.agregar_contenido(" √"))
        self.btnCuadrado.clicked.connect(lambda: self.agregar_contenido("^"))

    # Modificaciones para agregar funcionalidad a los botones
    def agregar_contenido(self, valor):
        self.pantalla += valor
        self.textEdit.setText(self.pantalla)

    def limpiar(self):
        self.pantalla = ""
        self.textEdit.clear()  

    def hola(self):
        print("Hola mundo")

    def eliminar_caracter(self):

        # Obtener el contenido actual de la pantalla
        contenido = self.textEdit.text()  

        # Verificar si hay algo que eliminar
        if contenido:
            # Eliminar el último carácter de la cadena
            contenido = contenido[:-1]
            self.textEdit.setText(contenido)

            # Actualizar la variable pantalla después de eliminar el carácter
            self.pantalla = contenido

    def limpiar_todo(self):
        self.textEdit.clear()  
        self.pantalla = ""  


