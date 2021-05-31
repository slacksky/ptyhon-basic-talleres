""" Modulo Multas
    Funciones para el cálculo de multas
    de tránsito 
    Jorge Vivas
    Mayo 24-2021 """

import random
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def multar_velocidad(dist1, dist2,t):
  #definiciones segun la normativa de velocidad 
  velocidad=round((abs(dist1-dist2)/t)*3.6,1)
  print("Beep..Beep, la velocidad del vehiculo es: ", velocidad," Km/h")

  texto_multa=""
  malcohol=""
  if velocidad>=1 and velocidad<21:
      texto_multa="llamado de atención por baja velocidad, detener solo advertencia\n"
  elif velocidad>=21 and velocidad<61:
      texto_multa="Velocidad normal, ignorar\n"
  elif velocidad>=61 and velocidad<81:
      texto_multa="llamado de atención por alta velocidad, detener solo advertencia\n"
  elif velocidad>=81 and velocidad<121:
      texto_multa="Multa Tipo I\n"
      alcohol=valor_alcoholemia()
      malcohol=multar_alcoholemia(alcohol)
  else:
      texto_multa="Multa Tipo II e inmobilizacion del vehiculo\n"
      alcohol=valor_alcoholemia()
      malcohol=multar_alcoholemia(alcohol)
  texto_multa=texto_multa+malcohol
  return texto_multa

def multar_alcoholemia(grado_alcohol):
#recibe el grado de alcohol generado en al funcion anterir y devuelve la sancion apropiada 
  texto_multa=""
  if grado_alcohol>=20 and grado_alcohol<40:
      texto_multa="Entre 20 y 39 mg de etanol/l00 ml de sangre total, además de las sanciones previstas en la presente ley, se decretará la suspensión de la licencia de conducción entre seis (6) y doce (12) meses.\n"
  elif grado_alcohol>=40 and grado_alcohol<100:
      texto_multa="Primer grado de embriaguez entre 40 y 99 mg de etanol/100 ml de sangre total, adicionalmente a la sanción multa, se decretará la suspensión de la Licencia de Conducción entre uno (1) y tres (3) años.\n"
  elif grado_alcohol>=100 and grado_alcohol<150:
      texto_multa="Segundo grado de embriaguez entre 100 y 149 mg de etanol/100 ml de sangre total, adicionalmente a la sanción multa, se decretará la suspensión de la Licencia de Conducción entre tres (3) y cinco (5) años, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de cuarenta (40) horas.\n"
  elif grado_alcohol>150:
      texto_multa="Tercer grado de embriaguez, desde 150 mg de etanol/100 ml de sangre total en adelante, adicionalmente a la sanción de la sanción de multa, se decretará la suspensión entre cinco (5) y diez (10) años de la Licencia de Conducción, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de ochenta (80) horas.\n"
  else:
      texto_multa="No hay multa por embriguez, niveles normales, corrija la velocidad y maneje con cuidado de aqui en mas.\n"
  return texto_multa

def valor_velocidad():
    ##Distancias uno, dos y tiempo entre medida t=2
    dist1 = round(random.uniform(1, 150),1)
    dist2 = round(random.uniform(1, 150),1)
    t=2
    
    return dist1, dist2, t


def valor_alcoholemia():
    alcoholemia = round(random.uniform(0, 151),1)
    print("alcoholemia:",alcoholemia," mg de etanol/100	ml de sangre")

    return alcoholemia

