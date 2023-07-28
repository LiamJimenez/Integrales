from sympy import integrate, init_printing
from sympy.abc import x 


init_printing(use_latex="mathjax")

f=input('Ingrese la funcion: ')
integrate(f)