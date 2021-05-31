""" Modulo generador aleatorio de cadenas #
    Funciones que retornan criaturas marinas
    y ubicaciones del barco 
    Jorge vivas
    Mayo 24-2021 """

import random
# Definición de Funcione
def aparecer_criatura():
  """ 
  Returns
  -------
  criatura:str
  Una de las 8 criaturas de la lista generadas aleatoriamente     
  """
  criaturas=["Kraken","Sirenas","Ballena","Hipocampo","Macaraprono","Pulpo","Leviatanes","Hidras"]
  indice = random.randint(0, 7)
  return criaturas[indice], indice

def aparecer_direccion():
  """ 
  Returns
  -------
  criatura:str
  Una de las 4 direcciones de la lista generadas aleatoriamente     
  """
  direccion=["babor","estribor","proa","popa"]
  indice = random.randint(0, 3)
  return direccion[indice],indice

def anuncio():
    ## print-> el mensaje para el capitan
    anuncio="Ajoy! Capitan, "
    #TODO: sumar los string por conducionales e imprimir al final 
    criatura, indiceb = aparecer_criatura()
    #print(indiceb)
    if (indiceb == 0 or indiceb == 3 or indiceb == 5):
        anuncio=anuncio+"Un "+str(criatura)+", "
    elif (indiceb == 2 or indiceb == 4 ):
        anuncio=anuncio+"Una "+str(criatura)+", "
    elif (indiceb == 1 or indiceb == 7 ):
        anuncio=anuncio+"Unas "+str(criatura)+", "
    else:
        anuncio=anuncio+"Unos "+str(criatura)+", "
    

    direccion, indiced=aparecer_direccion()

    if (direccion == 0 or direccion == 1):
        anuncio=anuncio+"A "+str(direccion)
    elif (direccion == 2 or direccion == 3):
        anuncio=anuncio+"Por la "+str(direccion)
    
    print(anuncio)


    

