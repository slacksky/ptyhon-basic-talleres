
""" Programa para apoyar al marinero Seijo
    Jorge Vivas
    Mayo 3-2021 """


import utilidades as util
import time as t 

def probar_funciones():
  criatura, indiceb= util.aparecer_criatura()
  direccion, indiced=util.aparecer_direccion()
  print(criatura,indiceb, direccion, indiced)


def main():
    
    for x in range(15):
        util.anuncio()
        #probar_funciones()
        t.sleep(3)

    print("Ahoy!, Capitan!, Tierra a la vista, llegamos a puerto!!!")

if __name__ == "__main__":
    main()

