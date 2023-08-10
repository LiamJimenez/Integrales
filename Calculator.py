import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication

class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(r"c:\Users\hilar\Desktop\Integrales-master\interfaz.ui", self)
        
        # Print
        self.btnCalcular.clicked.connect(self.hola)
        # Añadiendo iconos a botones
        self.btnIntegralDef.setIcon(QIcon(r"c:\Users\hilar\Desktop\Integrales-master\assets\IntegralDefinida.png"))
        self.btnIntegral.setIcon(QIcon(r"c:\Users\hilar\Desktop\Integrales-master\assets\Integral.png"))
        
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
        self.btn6.clicked.connect(self.btn6F)
        self.btn7.clicked.connect(self.btn7F)
        self.btn8.clicked.connect(self.btn8F)
        self.btn9.clicked.connect(self.btn9F)
        self.btn0.clicked.connect(self.btn0F)
        self.btnY.clicked.connect(self.btnYF)
        self.btnX.clicked.connect(self.btnXF)
        self.btnPi.clicked.connect(self.btnPiF)
        self.btnResta.clicked.connect(self.btnRestaF)
        self.btnSuma.clicked.connect(self.btnSumaF)
        self.btnMultiplicar.clicked.connect(self.btnMultiplicarF)
        self.btnDividir.clicked.connect(self.btnDividirF)
        self.btnRaiz.clicked.connect(self.btnRaizF)
        self.btnCuadrado.clicked.connect(self.btnCuadradoF)
        self.btnSin.clicked.connect(self.btnSinF)
        self.btnTan.clicked.connect(self.btnTanF)
        self.btnCos.clicked.connect(self.btnCosF)
        self.btnIntegral.clicked.connect(self.btnIntegralF)
        self.btnParentesis.clicked.connect(self.btnParentesisF)
        self.btnIntegralDef.clicked.connect(self.btnIntegralDefF)
        




     
        
        

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
    
    def btn6F(self):
        self.agregar_contenido("6")
        self.agregar_a_operaciones(self.btn6)

    def btn7F(self):
        self.agregar_contenido("7")
        self.agregar_a_operaciones(self.btn7)

    def btn8F(self):
        self.agregar_contenido("8")
        self.agregar_a_operaciones(self.btn8)

    def btn9F(self):
        self.agregar_contenido("9")
        self.agregar_a_operaciones(self.btn9)

    def btn0F(self):
        self.agregar_contenido("0")
        self.agregar_a_operaciones(self.btn0)

    def btnYF(self):
        self.agregar_contenido("Y")
        self.agregar_a_operaciones(self.btnY)

    def btnXF(self):
        self.agregar_contenido("X")
        self.agregar_a_operaciones(self.btnX)

    def btnPiF(self):
        self.agregar_contenido("π")
        self.agregar_a_operaciones(self.btnPi)
        
    def btnRestaF(self):
        self.agregar_contenido("-")
        self.agregar_a_operaciones(self.btnResta)

    def btnSumaF(self):
        self.agregar_contenido("+")
        self.agregar_a_operaciones(self.btnSuma)

    def btnMultiplicarF(self):
        self.agregar_contenido("*")
        self.agregar_a_operaciones(self.btnMultiplicar)

    def btnDividirF(self):
        self.agregar_contenido("÷")
        self.agregar_a_operaciones(self.btnDividir)

    def btnRaizF(self):
       self.agregar_contenido("√")
       self.agregar_a_operaciones(self.btnRaiz)

    def btnCuadradoF(self):
        self.agregar_contenido("^")
        self.agregar_a_operaciones(self.btnCuadrado)
     
    def btnSinF(self):
        self.agregar_contenido("Sin")
        self.agregar_a_operaciones(self.btnSin)

    def btnTanF(self):
        self.agregar_contenido("Tan")
        self.agregar_a_operaciones(self.btnTan)

    def btnCosF(self):
        self.agregar_contenido("Cos")
        self.agregar_a_operaciones(self.btnCos)

    def btnIntegralF(self):
        self.agregar_contenido("∫")
        self.agregar_a_operaciones(self.btnIntegral)

    def btnParentesisF(self):
        self.agregar_contenido("()")
        self.agregar_a_operaciones(self.btnParentesis)

    def btnIntegralDefF(self):
        self.agregar_contenido("∫[ ]")
        self.agregar_a_operaciones(self.btnIntegralDef)

    

        
    

    

    
    
   


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