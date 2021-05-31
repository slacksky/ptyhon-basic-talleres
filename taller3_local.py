""" Taller 2.3 Distancia mas corta #
    JOrge Vivas
    Mayo 16-21 """

# Definición de Funciones (Dividir)
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================


#def calcular_distancia_c1_a1(xc1,yc1,xa1,ya1):
  #TODO: comentarios
  #TODO: instrucciones
  #return
#-------------------------------------------
#def calcular_distancia_a1_ch(xa1,ya1,xch,ych):
  #TODO: comentarios
  #TODO: instrucciones
#  return
#-------------------------------------------
#def calcular_distancia_ch_a2(xch,ych,xa2,ya2):
  #TODO: comentarios
  #TODO: instrucciones
 # return
#-------------------------------------------
#def calcular_distancia_a2_c2(xa2,ya2,xc2,yc2):
  #TODO: comentarios
  #TODO: instrucciones
 # return
#-------------------------------------------
#def obtener_distancia_total (d1,d2,d3,d4):
  #TODO: comentarios
  #TODO: instrucciones
 # return 
#----------------
def dist_cart(A,B):##A y B tienen que ser arrays 2x1 para puntos cartesianos x/y
    dist=(((A[0]-B[0])**2)+((A[1]-B[1])**2))**(1/2)
    return dist

def carga_coord():##solo coordenadas en array 2x1
    Z=[0,0]
    Z[0]=float(input("favor ingresar coordenada en x:"))
    Z[1]=float(input("favor ingresar coordenada en y:"))
    return Z



def main():
#======================================================================
#          E S P A C I O    P R E _ _ C O N F I G U R A D O
# =====================================================================
#----------------
    def dist_cart(A,B):##A y B tienen que ser arrays 2x1 para puntos cartesianos x/y
      dist=(((A[0]-B[0])**2)+((A[1]-B[1])**2))**(1/2)
        return dist

    def carga_coord():##solo coordenadas en array 2x1
        Z=[0,0]
        Z[0]=float(input("favor ingresar coordenada en x:"))
        Z[1]=float(input("favor ingresar coordenada en y:"))
        return Z


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
#lectura coordenadas celular 1
#TODO: instrucciones
    print("necesitamos la localizacion del celular")
    cell=[1,1]
    cell=carga_coord()

#lectura coordenadas antena 1
#TODO: instrucciones
    print("necesitamos la localizacion de la primera antena")
    ant1=[2,2]
    ant1=carga_coord()
#lectura coordenadas central holi 
#TODO: instrucciones
    print("necesitamos la localizacion del HQ")
    HQholi=[0,0]
    HQholi=carga_coord()

#lectura coordenadas antena 2
#TODO: instrucciones
    print("necesitamos la localizacion de la segunda antena")
    ant2=[3,3]
    ant2=carga_coord()

#lectura coordenadas celular 1
#TODO: una vez haga os puntos anteriores quite el simbolo de comentarios
# y organice la identación

    dc1=dist_cart(cell,ant1)
    print("dist del celular a la primera antena:",dc1)
    d1H=dist_cart(ant1,HQholi)
    print("dist de HQ a Antena 1:",d1H)
    d2H=dist_cart(ant2,HQholi)
    print("dist de HQ a Antena 2:",d2H)
    dc2=dist_cart(cell,ant2)
    print("dist del celular a la segunda antena:",dc2)
    dist_total=dc1+d1H+d2H+dc2
    print("dist total:",dist_total)
    dcH=dist_cart(cell,HQholi)
    print("dist cell a HQ:",dcH)



#d1=calcular_distancia_c1_a1(xc1,yc1,xa1,ya1)
#d2=calcular_distancia_a1_ch(xa1,ya1,xch,ych)
#d3=calcular_distancia_ch_a2(xch,ych,xa2,ya2)
#d4=calcular_distancia_a2_c2(xa2,ya2,xc2,yc2)

#distancia_total=obtener_distancia_total (d1,d2,d3,d4)
#print("La distancia otal es",distancia_total)


if __name__ == "__main__":
    main()