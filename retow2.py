""" Taller 2.3 Distancia mas corta #
    Jorge Vivas
    Mayo 16-21 """


import math

def main():
    ##global var area testing processes
    ##function area
    def hipotenusa(A,B):##para calcular longitud de cuerda de la polea
        C=(((A)**2)+((B)**2))**(1/2)
        return C

    def circunferencia(d):##para calcular longitud de cuerda de la polea
        p=2*math.pi*(d/100)#perimetro en metros de la rueda, (d/100para pasar de cm a m)
        return p

    def vueltas(p,rec):##permitro del circulo y recorrido de la polea, regresa n de vueltas (rad?)
        Nvue=rec/p
        return Nvue

    def chewies(Nvue):##redondea hacia arriba por si acaso 
        Nchew=math.ceil(Nvue/3)
        return Nchew

    def velo_rueda(rec,t):#recorrido mts, tiempo en mins,veolcidad lineal de la rueda en Cms/seg
        velol=(rec*100)/(t*60)
        return velol
    
    ##input area
    ##TODO: add input and float transforation for each
    #L=3 ##mts default unit, longintud del puente
    L=float(input("cual es el largo del puente, en metros?\n"))
    #d=50 ##cms tranformar antes de usar
    d=float(input("cual es el diametro de la polea en cm?\n"))
    #t=3 ##tiempo de cierre en min transformar antes d eusar
    t=float(input("cual es el tiempo en mins para que cierre con seguridad?\n"))

    ##results  area
    p=circunferencia(d)
    print("perimetro: ", round(p,4)," metros")
    rec=hipotenusa(L,L)
    print("recorrido de la cuerda de la polea para cerrar: ", round(rec,4)," metros")
    Nvue=vueltas(p,rec)
    print("vueltas requeridas para cerrar, ", round(Nvue,4)," vueltas")
    Nchew=chewies(Nvue)
    print("se requiren unos, ",Nchew," kashykianos, tan grandes como chewbacca")
    velol=velo_rueda(rec,t)
    print("la velocidad requerida para cerrar, con seguridad, en ", round(t,0)," mins, es como minimo,", round(velol,4), " cms/seg")
    






if __name__ == "__main__":
    main()