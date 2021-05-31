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
  total_p=0
  gen=range(generacion)
  for x in gen:
    print("generacion", x+1)##+1 para mejor entendimiento de las generaciones
    anc=2**x
    print("persona(s) en esta generacion: ", anc) 
    total_p+=anc 
    print("total acumulado, ",total_p," para la generacion ",x+1)
  return total_p
  """en resumida cuentas seria sumatorias con elevacion de 2 por cada genracion"""
  

def constructor_triangulos(pisos):
  #TODO Comentar código
  #TODO Implementar la función
  numero=1
  for i in range(1,pisos+1):
    for j in range(1,i+1):
      print(numero, end= ' ')
      numero+=1
    print()

  """numero de piso triangulares revisar con fibonachi para fors anidados"""
  #return "No implementada aún"

def constructor_tableros(longitud):
  #TODO Comentar código
  #TODO Implementar la función

  b=""
  w=""
  b,w=row_builder(longitud)
  board_builder(longitud,b,w)


def tile_third(color):
  if color == 0:
    return "***"
  else:
    return "   "

def full_tile(t3):
  for i in range(3):
    print(t3)

def row_builder(longitud):
  tileb=""
  tilew=""
  for i in range(longitud):
    tileb+=tile_third(i%2)
  
  if longitud>1:
    for i in range(longitud):
      tilew+=tile_third((i+1)%2)
  return tileb,tilew

def board_builder(longitud, black, white):
  for i in range(longitud):
    if i%2==0:
      full_tile(black)
    else:
      full_tile(white)


  ##usar un template para cada cuadrado y poner for anidados para crear la cuadricula
  ##return "No implementada aún"