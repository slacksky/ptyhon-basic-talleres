""" Programa calculadora artimética amigable#
    Realiza las 4 operaciones (+,-,* /) 
    incorpora al modulo calculadora_aritmetica.py
    Jorge Vivas
    Mayo 24-2021 """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

def menu_operaciones():
  print("==================================================")
  print("| Menu")
  print("==================================================")
  print("| Ingresa un numero para realizar la operacion.")
  print("==================================================")
  print("| 1. Calcular suma: (1)")
  print("==================================================")
  print("| 2. Calcular la resta: (2)")
  print("==================================================")
  print("| 3. Calcular multiplicación: (3)")
  print("==================================================")
  print("==================================================")
  print("| 4. Calcular división: (4)")
  print("==================================================")
   
  opcion = input()
  return opcion



def main():
    #print("Hello World!")

    #======================================================================
    #   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
    # =====================================================================
    operacion=menu_operaciones()

    #======================================================================
    #          E S P A C I O    D E    T R A B A J O     A L U M N O
    # ====================================================================
    num1 = float(input("ingrese el numero 1:"))
    num2 = float(input("ingrese el numero 2:"))

    if operacion == "1":
        suma = calc.sumar_numeros(num1, num2)
        print("la suma es:", suma)
    elif operacion == "2":
        resta = calc.restar_numeros(num1, num2)
        print("la resta es:", resta)
    elif operacion == "3":
        multiplicacion = calc.multiplicar_numeros(num1, num2)
        print("la multiplicacion es:", multiplicacion)
    elif operacion == "4":
        if num2==0:
            print("error division por cero es infinto")
        else:
            division = calc.dividir_numeros(num1, num2)
            print("la division es:", division)
    else:
        print("opracion desconocida")



if __name__ == "__main__":
    main()