import sys
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from sympy import sympify
from sympy import *
import math
import sympy as sp

class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(r"c:\Users\hilar\Desktop\Integrales-master\interfaz.ui", self)
        
        # Print
        self.btnCalcular.clicked.connect(self.calcular_resultado)
        # Añadiendo iconos a botones
        self.btnIntegralDef.setIcon(QIcon( r"c:\Users\hilar\Desktop\Integrales-master\assets\IntegralDefinida.png"))
        self.btnIntegral.setIcon(QIcon( r"c:\Users\hilar\Desktop\Integrales-master\assets\Integral.png"))
        
        # Botones
        self.btnC.clicked.connect(self.eliminar_caracter)
        self.btnCA.clicked.connect(self.limpiar_todo)

        # Variable para almacenar el contenido de la pantalla
        self.pantalla = ""

        # Lista para almacenar las operaciones
        self.operaciones = []
        self.result1= 0
        self.result2 = 0
        self.calculado = False

        # Conectar botones a funciones
        # Botones de Liam
        self.btn1.clicked.connect(self.btn1F)
        self.btn2.clicked.connect(self.btn2F)
        self.btn3.clicked.connect(self.btn3F)
        self.btn4.clicked.connect(self.btn4F)
        self.btn5.clicked.connect(self.btn5F)

        # Botones de Jesus
        self.btn6.clicked.connect(self.btn6F)
        self.btn7.clicked.connect(self.btn7F)
        self.btn8.clicked.connect(self.btn8F)
        self.btn9.clicked.connect(self.btn9F)
        self.btn0.clicked.connect(self.btn0F)
        self.btnParentesis.clicked.connect(self.btnParentesisF)

        # Botones de Hilari
        self.btnY.clicked.connect(self.btnYF)
        self.btnX.clicked.connect(self.btnXF)
        self.btnResta.clicked.connect(self.btnRestaF)
        self.btnSuma.clicked.connect(self.btnSumaF)
        self.btnMultiplicar.clicked.connect(self.btnMultiplicarF)
        self.btnDividir.clicked.connect(self.btnDividirF)
        self.btnComa.clicked.connect(self.btnComaF)
        self.btnCuadrado.clicked.connect(self.btnCuadradoF)
        
        # Botones de Francesco
        self.btnPi.clicked.connect(self.btnPiF)
        self.btnSin.clicked.connect(self.btnSinF)
        self.btnTan.clicked.connect(self.btnTanF)
        self.btnCos.clicked.connect(self.btnCosF)
        self.btnIntegral.clicked.connect(self.btnIntegralF)
        self.btnIntegralDef.clicked.connect(self.btnIntegralDefF)
        
        ## Funcion para que la lista se vacie despues del resultado
        self.textEdit.textChanged.connect(self.borrarTexto)
      
    #Funciones para agregar botones a la lista

    def borrarTexto(self):
        if self.calculado == True:
            self.textEdit.clear()
            self.calculado = False
    
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

    def btnParentesisF(self):
        if self.pantalla.endswith("("):
            self.agregar_contenido(")")
        elif self.pantalla and self.pantalla[-1].isdigit():
            self.agregar_contenido(")")
        else:
            self.agregar_contenido("(")
        self.agregar_a_operaciones(self.btnParentesis)


    def btnYF(self):
        self.agregar_contenido('y')
        self.agregar_a_operaciones(self.btnY)

    def btnXF(self):
        self.agregar_contenido('x')
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
        self.agregar_contenido("/")
        self.agregar_a_operaciones(self.btnDividir)

    def btnComaF(self):
       self.agregar_contenido(",")
       self.agregar_a_operaciones(self.btnComa)

    def btnCuadradoF(self):
        self.agregar_contenido("")
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
    
    def btnCuadradoF(self):
        self.agregar_contenido("^")
        self.agregar_a_operaciones(self.btnCuadrado)

    def btnIntegralF(self):
        f = self.pantalla
        x = symbols('x')
        try:
            resultado = integrate(f,(x))
            self.textEdit.setText(str(resultado))
        except Exception as e:
            self.textEdit.setText("Error")  

    def btnIntegralDefF(self):
        
        valores1 = []
        valores2 = []
        valores3 = []
        # Transforma cada array en un string y despues los devuelve como numero
                
        if self.pantalla.endswith("∫["):
                self.textEdit.textChanged.connect(self.agregarOp,E)
                self.agregar_a_operaciones(self.operaciones.append())
                self.agregar_contenido("]")  
        elif self.pantalla.__contains__("∫[") and self.pantalla.__contains__("]"):
            self.btnIntegralDefCalcular(self.result1,self.result2)
            self.operaciones.clear()
            valores1.clear()
            valores2.clear()
            valores3.clear()
        elif self.pantalla and self.pantalla[-1] == "]":
            self.agregar_contenido("")  
        elif self.pantalla and self.pantalla[-1].isdigit():
            num = 0
            if num == 0:
                self.agregar_contenido("]")
                num+1  
        else:
            self.agregar_contenido("∫[")  

            ## Iterar a través del array self.operaciones
        for i in range(len(self.operaciones)):
            if self.operaciones[i] == ",":
                ## Ingresar los números desde el principio hasta el operador en valores1
                for l in range(0, i):
                    if self.operaciones[l] != '':
                        valores1.append(self.operaciones[l])
                
                ## Ingresar los números desde el operador hasta el siguiente elemento vacío en valores2
                a = i + 1
                
                while a < len(self.operaciones) and self.operaciones[a] != '':
                    valores2.append(self.operaciones[a])
                    a += 1
                
                ## Ingresar los elementos vacíos después de valores2 en valores3
                while a < len(self.operaciones):
                    valores3.append(self.operaciones[a])
                    a += 1
                
                break  ## Terminar el bucle después de encontrar el primer operador
        sep1 = ""
        self.result1 = sep1.join(valores1)
        
        sep2 = ""
        self.result2= sep2.join(valores2)

        self.agregar_a_operaciones(self.btnIntegralDef)


    #Agregar Contenido a la pantalla
    def btnIntegralDefCalcular(self,valores1,valores2):
        x = symbols('x')
        
        f = self.obtener_valores_despues_de_corchete(self.pantalla)
        try:
            resultado2 = integrate(f,(x,valores1,valores2))
            self.textEdit.setText(str(resultado2))
        except Exception as e:
            self.textEdit.setText("Error")
    
    def obtener_valores_despues_de_corchete(self,cadena):
        valores_despues = ""
        encontro_corchete = False
        
        for caracter in cadena:
            if encontro_corchete:
                valores_despues += caracter
            elif caracter == "]":
                encontro_corchete = True
        
        return valores_despues
    
    def agregarOp(self,E):
        self.operaciones.append(E)
    
    def agregar_contenido(self, valor):
        self.pantalla += valor
        self.textEdit.setText(self.pantalla)

    #Limpiar Pantalla
    def limpiar(self):
        self.pantalla = ""
        self.textEdit.clear()  

     #Eliminar un caracter cuando le de la boton C
    def eliminar_caracter(self):
        contenido = self.textEdit.text()
        self.operaciones.pop()
        if contenido:
            
            contenido = contenido[:-1]
            self.textEdit.setText(contenido)
            self.pantalla = contenido

    #Eliminar todo cuando le de al boton CA
    def limpiar_todo(self):
        self.operaciones.clear()
        self.textEdit.clear()
        self.pantalla = ""

    #Calcular resultado
    def calcular_resultado(self):
         # Obtener la expresión ingresada por el usuario
        expresion = self.pantalla
         # Suma
        if '+' in expresion:
            partes = expresion.split('+') # Dividir la expresión en partes usando el signo '+'
            numeros = [float(part.strip()) for part in partes] # Convertir las partes en números y quitar espacios
            resultado = sum(numeros)  # Sumar los números
        elif '-' in expresion:     # Resta
            partes = expresion.split('-') # Dividir la expresión en partes usando el signo '-'
            numeros = [float(part.strip()) for part in partes]  # Convertir las partes en números y quitar espacios
            resultado = numeros[0] - sum(numeros[1:]) # Restar el primer número por la suma de los siguientes
        elif '*' in expresion:
            partes = expresion.split('*')  # Dividir la expresión en partes usando el signo '*'
            numeros = [float(part.strip()) for part in partes] # Convertir las partes en números y quitar espacios
            resultado = 1.0
            for num in numeros:
                resultado *= num  # Multiplicar cada número por el resultado actual
        elif '/' in expresion:  # División
            partes = expresion.split('/')  # Dividir la expresión en partes usando el signo '/'
            numeros = [float(part.strip()) for part in partes] # Convertir las partes en números y quitar espacios  
            resultado = numeros[0] / float(numeros[1])  # Dividir el primer número por el segundo
        elif '^' in expresion:   # Potenciación
            base, exponente = expresion.split('^') # Dividir la expresión en base y exponente
            resultado = float(base) ** float(exponente) # Calcular la potencia
        elif '√' in expresion:  # Raíz cuadrada
            radicando = expresion.split('√')[1] # Obtener el número al que se le calculará la raíz
            resultado = float(radicando) ** 0.5  # Calcular la raíz cuadrada
            # Funciones trigonométricas
        elif 'Sin(' in expresion: 
            angulo = expresion.split('Sin(')[1][:-1]  # Obtener el ángulo de la expresión
            resultado = math.sin(float(angulo)) # Calcular el seno del ángulo
        elif 'Cos(' in expresion:
            angulo = expresion.split('Cos(')[1][:-1]  # Obtener el ángulo de la expresión
            resultado = math.cos(float(angulo)) # Calcular el coseno del ángulo
        elif 'Tan(' in expresion:
            angulo = expresion.split('Tan(')[1][:-1] # Obtener el ángulo de la expresión
            resultado = math.tan(float(angulo)) # Calcular la tangente del ángulo
        elif 'pi' in expresion: 
            resultado = math.pi # Establecer el valor de pi
            # Si no se identifica ninguna operación válida
        else:
            resultado = None

           # Si se calculó un resultado válido
        if resultado is not None:
            self.pantalla = str(resultado)  # Convertir el resultado en texto
            self.textEdit.setText(self.pantalla)  # Mostrar el resultado en un widget de interfaz de usuario
