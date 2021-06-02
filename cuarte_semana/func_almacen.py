def input_prod(Prod, Cant,categ):
    p=input("ingrese el nombre del producto: ")
    c=int(input("ingrese cantidades del producto: "))

    if p in Prod[categ]:
        i=Prod[categ].index(p)
        Cant[categ][i]+=c
    else:
        Prod[categ].append(p)
        Cant[categ].append(c)
    return Prod,Cant

def categorias():
    c=int(input("elija la categoria:\n1.lacteos\n2.aseo\n3.granos\n(1 a 3): "))
    
    
    """if c  not == (1 or 2 or 3):
        print(" solo se acepta del 1 al 3, bye...")
    else:"""
    return c-1

def impresioninvent(Prod, Cant):
    for i in range(len(Prod)):
        if i == 0:
            print("## imprimiendo productos lacteos##")
        elif i == 1:
            print("\n## imprimiendo productos de aseo##")
        elif i == 2:
            print("\n## imprimiendo granos##")
        for j in range(len(Prod[i])):
            print("#para el producto, ",Prod[i][j])
            print("hay la siguientes unidades, ",Cant[i][j])
    print("##impresion de inventario finalizada##")

def continuar(cont):
    cont=int(input("continuar? \n 0 para si, 1 para no "))
    return cont