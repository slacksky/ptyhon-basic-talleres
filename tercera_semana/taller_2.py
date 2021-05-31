""" Programa Apoyo multas#
    incorpora al modulo multas.py
    Jorge Vivas
    Mayo 24-2021 """

#---------------- Zona librerias------------
import multas as mult
import time as t

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

def main():
    
    
    for x in range(15):
        dist1, dist2, time=mult.valor_velocidad()
        multa=mult.multar_velocidad(dist1, dist2, time)
        print(multa)
        
        t.sleep(10)

    print("Bunas noches compa#ero, que noche tan ajetreada!, hasta ma#na.")

if __name__ == "__main__":
    main()