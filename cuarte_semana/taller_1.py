""" MAin taller 1
    Funciones para practicas con ciclos
    Jorge Vivas
    Mayo 29-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

import funciones_ciclos as f



def main():
    #TODO: menu
    print("## Bienvenido, a multi-herramienta T ##")
    print("## 1->simulacion caida libre    ##")
    print("## 2->calculo generacional      ##")
    print("## 3->triangulo de enteros      ##")
    print("## 4->tableros custom de ajedres##")

    menu=int(input("##porfavor, elegir una  opcion (1,2,3,4)## \n"))

    if menu == 1:
        dist=float(input("ingrese la altura en metros: "))
        f.simulador_caida_libre(dist)
    elif menu == 2:
        generacion=int(input("cuantas generaciones hacia atras quieres visualizar?:"))
        total_personas=f.generador_generaciones(generacion)
        print("en estas ",generacion," generaciones, han habido, ",total_personas," personas ")
    elif menu == 3:
        pisos=int(input("con cuantos pisos quieres el triangulo? "))
        f.constructor_triangulos(pisos)
    elif menu == 4:
        cuadros=int(input("cuantos cuadrosXcuadros para el tablero?"))
        f.constructor_tableros(cuadros)
    else:
        print("## porfavor elige uno de los numeros  del 1 al 4##")
    print("trabajo completado, Cerrando ... bye")



if __name__ == "__main__":
    main()