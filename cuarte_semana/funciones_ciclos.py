""" Modulo Ciclos
    Funciones para practicas con ciclos
    Jorge Vivas
    Mayo 29-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def simulador_caida_libre(altura):
  #TODO Comentar código
  t=0

  while altura >= 0:
    d = (9.8/2)*(t**2)
    altura-=d
    print("a los ",t, "segundos estamos a ",altura," del suelo")
    t+=1
  print("terminamos de caer")

  return "No implementada aún"

def generador_generaciones(generacion):
  ##in: generacion, mid: total_p, out: total_p
  total_p=1
  gen=range(generacion)
  for x in gen:
    total_p+= 2**x
  return total_p
  """en resumida cuentas seria sumatorias con elevacion de 2 por cada genracion"""
  

def constructor_triangulos(pisos):
  #TODO Comentar código
  #TODO Implementar la función

  """numero de piso triangulares revisar con fibonachi para fors anidados"""
  return "No implementada aún"

def constructor_tableros(longitud):
  #TODO Comentar código
  #TODO Implementar la función

  ##usar un template para cada rectaincugna y  pone for anidados para crear la cuadricula
  return "No implementada aún"