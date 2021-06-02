import func_almacen as fa

def main():
    #print("Hello World!")
    Prod=[["leche","queso", "tofu"],["jabon","cloro", "desengrasante"],["caraota","maiz","lenteja"]]##init de productos  base y cantidades
    Cant=[[10,3,5],[9,1,2],[100,200,300]] ##inventario inicial
    cont=0
    while cont == 0:
        
        categ=fa.categorias()
        Prod,Cant=fa.input_prod(Prod,Cant,categ)
        cont=fa.continuar(cont)
    fa.impresioninvent(Prod, Cant)    



    


if __name__ == "__main__":
    main()