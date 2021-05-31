#TODO Sumatoria de numeros pares
""" Programa Sumatoria#
    Calcula la sumatoria
    de numeros desde 1 hasta
    un limite dado
    Jorge Vivas
    Mayo 27-2021 """

def calcular_sumatoria(limite):

  
  cont=1 #Inicializa el contador
  sumatoria=0 #inicializa la suma en 0
  while cont <= limite: 
    sumatoria=sumatoria+cont # Realiza la suma
    cont+=1 #incrementa el contador
    print("El valor de la sumatoria es:", sumatoria )

  return sumatoria  
 
#====================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# ===================================================================

limite_sumatoria=int(input("Digite el número hasta el cual realizará la sumatoria:"))
#Validacion del valor de entrada
if limite_sumatoria <= 0:
  print("debe ingresar un número mayor a cero") 
else:
  suma_total=calcular_sumatoria(limite_sumatoria)
  print("El valor de la sumatoria es:",suma_total)