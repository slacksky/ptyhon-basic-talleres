def convenio_ventas(Kgmant, Kgqueso, Pmant, Pqueso):
    
    KgTotal=Kgmant+Kgqueso
    Venta_convenio=Venta_neta=Kgmant*Pmant+Kgqueso*Pqueso
    print("total de KGs de  productos: ", KgTotal," Kgs")
    print("precio de venta base: ", Venta_neta," COP")

    if 100>KgTotal>=50:
        Venta_convenio=Venta_neta*(1-0.08)
        print("los Kgs totales superan los 50 Kgs, pero queda por debajo de los 100 Kgs, se aplica  8% descuento, monto ", Venta_convenio, " COP")
    elif KgTotal>=100:
        Venta_convenio=Venta_neta*(1-0.12)
        print("los Kgs totales superan los 100 Kgs, se aplica  12% descuento, monto ", Venta_convenio, " COP")

    if Venta_convenio>500000:
        Venta_convenio=Venta_convenio*(1-0.03)
        print("se superan los 500000 COP de precio de venta aplicando el descuento de 3% ", Venta_convenio, " COP")

    return Venta_convenio
