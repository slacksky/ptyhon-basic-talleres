""" Modulo Listas
    Funciones para practicas con listas
    Jorge Vivas
    Mayo 30-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def suma_acumulativa(lista_numeros):
  #TODO Comentar código
  #TODO Implementar la función
  lista_acumulada=lista_numeros.copy()
  for i in range(1,len(lista_numeros)):
    lista_acumulada[i]=lista_acumulada[i]+lista_acumulada[i-1]
  return lista_acumulada

def traductor_pig_latin(lista_palabras):
  ora=lista_palabras
  #TODO Comentar código
  #TODO Implementar la función
  lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
  #ora = input('ingresa lo que quieres traducido a pig-latin y presiona ENTER: ')
  #ora = ora.split()
  for k in range(len(ora)):
    i = ora[k]
    if i[0] in ['a', 'e', 'i', 'o', 'u']:
      ora[k] = i+'ay'
    elif t(i) in lst:
      ora[k] = i[2:]+i[:2]+'ay'
    elif i.isalpha() == False:
      ora[k] = i
    else:
      ora[k] = i[1:]+i[0]+'ay'
  return ora
  #return ' '.join(ora)
  
def t(str):
  return str[0]+str[1]

def identificador_frutas(lista_frutas):
  #TODO Comentar código
  #TODO Implementar la función
  vitamina_a=[]
  for j in range(len(lista_frutas)):
    i= lista_frutas[j]
    if i[0] in ['a']:
      vitamina_a.append(i)

  return vitamina_a

def son_palindromos(frase_uno, frase_dos):
  #TODO Comentar código
  #TODO Implementar la función
  #frase_uno.split()
  #frase_dos.split()
  frase_uno=''.join(frase_uno)
  frase_dos=''.join(frase_dos)
  frase_dos=frase_dos[::-1]
  frase_uno=frase_uno.lower()
  frase_dos=frase_dos.lower()
  print(frase_uno)
  print(frase_dos)
  if frase_uno == frase_dos:
    print("la frase es palindromo")
  else:
    print("solo se que no es palindromo")

  #return 
