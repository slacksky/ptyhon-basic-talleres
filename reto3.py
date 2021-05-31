def main():
    import math
    import produccion
    import venta_semanal

    #vacas=94
    #Kgmant=250
    #Kgqueso=250
    P_MANT=6500
    P_QUES=7200
    #calculo de la venta
    #calculo de las vacas requridas


    print("##Calculo del valor de venta en base a la vacas##")

    vacas=int(input("Ingrese el numero de vacas disponibles:"))
    
    KgM,KgQ=produccion.produccion_semanal(vacas)
    print("Kgs de matequilla a la semana",KgM,"\nKgs de queso a la semana",KgQ)
    Venta=venta_semanal.convenio_ventas(KgM,KgQ,P_MANT,P_QUES)
    print("Precio final de venta ",Venta," COP")

    print("\n##Calculo de las vacas requridas para la venta##")

    Kgmant=float(input("Ingrese los Kgs de Mantequilla a vender:"))
    Kgqueso=float(input("Ingrese los Kgs de Queso a vender:"))

    Nv=produccion.vacas_requeridas(Kgmant, Kgqueso)
    print("se necesitan ",Nv," vacas para la produccion estimada, redondeado hacia arriba")
    
    #calculo de la venta ingrasando precios y produccion
    print("\n##Calculo de la venta basada en produccion##")

    Kgmant=float(input("Ingrese los Kgs de Mantequilla a vender:"))
    Kgqueso=float(input("Ingrese los Kgs de Queso a vender:"))
    pmant=float(input("Ingrese el precio de venta de Mantequilla:"))
    pques=float(input("Ingrese el precio de venta de Queso:"))
    print("recalculando con los nuevo precios de venta")
    Venta=venta_semanal.convenio_ventas(Kgmant,Kgqueso,pmant,pques)
    print("Precio final de venta ",Venta," COP")
    


    

if __name__ == "__main__":
    main()