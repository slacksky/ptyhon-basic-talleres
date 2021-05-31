

""" Laboratorio 3.1 La calculadora de Trigo 
    Jorge Vivas
    Mayo 26-2021 """

# Importar modulos/librerias
import math as m

# Definición de Funciones (Dividir)
def calcular_seno(angulo_grados):
  """ 
  Parameters
  ----------
  nangulo_grados:float
     un numero entre 0  y 360 que representa un ángulo en graados
  -------
  Return
  seno:float
    el seno del angulo_grados   
  """  
  seno= m.sin(m.radians(angulo_grados))
  return seno

def calcular_coseno(angulo_grados):
  coseno= m.cos(m.radians(angulo_grados))
  return coseno

def calcular_tangente(angulo_grados):
  tangente= m.tan(m.radians(angulo_grados))
  return tangente

def calcular_cotangente(angulo_grados):

  cotangente= 1/m.tan(m.radians(angulo_grados))
  return cotangente

def calcular_arcoseno(angulo_grados):
  arcoseno= m.asin(m.radians(angulo_grados))
  return arcoseno
def calcular_arcocoseno(angulo_grados):
  arcocoseno= m.acos(m.radians(angulo_grados))
  return arcocoseno
def calcular_arcotangente(angulo_grados):
  arcotangente= m.atan(m.radians(angulo_grados))
  return arcotangente
#TODO: Ayudar al profe con las demás funciones
"""
-  calcular_coseno(angulo_grados)
-  calcular_tangente(angulo_grados)
-  calcular_cotangente(angulo_grados)
-  calcular_arcoseno(angulo_grados)
-  calcular_arcocoseno(angulo_grados)
-  calcular_arcotangente(angulo_grados)
"""

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

#lectura angulo
angulo_g=float(input("Ingresa un ángulo entre 0 y 360 "))
r_seno=calcular_seno(angulo_g)
print("Seno(",angulo_g,")=",r_seno)
r_coseno=calcular_coseno(angulo_g)
print("Coseno(",angulo_g,")=",r_coseno)
r_tangente=calcular_tangente(angulo_g)
print("Tangente(",angulo_g,")=",r_tangente)
r_cotangente=calcular_cotangente(angulo_g)
print("Cotangente(",angulo_g,")=",r_cotangente)
r_arcoseno=calcular_arcoseno(angulo_g)
print("Arcoseno(",angulo_g,")=",r_arcoseno)
r_arcocoseno=calcular_arcocoseno(angulo_g)
print("Arcocoseno(",angulo_g,")=",r_arcocoseno)
r_arcotangente=calcular_arcotangente(angulo_g)
print("Arcotangente(",angulo_g,")=",r_arcotangente)
