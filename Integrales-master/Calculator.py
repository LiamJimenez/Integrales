import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication

class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(r"c:\Users\Admin\OneDrive\Escritorio\Integrales_Proyect\Integrales-master\interfaz.ui", self)
        
        # Print
        self.btnCalcular.clicked.connect(self.hola)
        # Añadiendo iconos a botones
        self.btnIntegralDef.setIcon(QIcon(r"c:\Users\Admin\OneDrive\Escritorio\Integrales_Proyect\Integrales-master\assets\IntegralDefinida.png"))
        self.btnIntegral.setIcon(QIcon(r"c:\Users\Admin\OneDrive\Escritorio\Integrales_Proyect\Integrales-master\assets\Integral.png"))
        
        # Botones
        self.btnC.clicked.connect(self.eliminar_caracter)
        self.btnCA.clicked.connect(self.limpiar_todo)

        # Variable para almacenar el contenido de la pantalla
        self.pantalla = ""

        # Lista para almacenar las operaciones
        self.operaciones = []

        # Conectar botones a funciones
        self.btn1.clicked.connect(self.btn1F)
        self.btn2.clicked.connect(self.btn2F)
        self.btn3.clicked.connect(self.btn3F)
        self.btn4.clicked.connect(self.btn4F)
        self.btn5.clicked.connect(self.btn5F)

    def agregar_a_operaciones(self, boton):
        self.operaciones.append(boton.text())
        print("Operaciones:", self.operaciones)

    def btn1F(self):
        self.agregar_contenido("1")
        self.agregar_a_operaciones(self.btn1)

    def btn2F(self):
        self.agregar_contenido("2")
        self.agregar_a_operaciones(self.btn2)

    def btn3F(self):
        self.agregar_contenido("3")
        self.agregar_a_operaciones(self.btn3)

    def btn4F(self):
        self.agregar_contenido("4")
        self.agregar_a_operaciones(self.btn4)

    def btn5F(self):
        self.agregar_contenido("5")
        self.agregar_a_operaciones(self.btn5)


    def agregar_contenido(self, valor):
        self.pantalla += valor
        self.textEdit.setText(self.pantalla)

    def limpiar(self):
        self.pantalla = ""
        self.textEdit.clear()  

    def hola(self):
        print("Hola mundo")

    def eliminar_caracter(self):
        contenido = self.textEdit.text()
        if contenido:
            contenido = contenido[:-1]
            self.textEdit.setText(contenido)
            self.pantalla = contenido

    def limpiar_todo(self):
        self.textEdit.clear()
        self.pantalla = ""