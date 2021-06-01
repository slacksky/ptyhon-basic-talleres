import funciones_listas as f
import random
def main():
    
    
    print("## Bienvenido, a multi-herramienta L ##")
    print("## 1->suma acumlada de lista         ##")
    print("## 2->traductor de pig latin         ##")
    print("## 3->frutas con vitmaina A?         ##")
    print("## 4->es palindromo?                 ##")

    menu=int(input("##porfavor, elegir una  opcion (1,2,3,4)## \n"))

    if menu == 1:
        lista = random.sample(range(10, 30), random.randint(1,10))
        lista_c=f.suma_acumulativa(lista)
        print("De la primer lista: ",lista)
        print("Se obtien la lista cumulativa: ",lista_c)
    elif menu == 2:
        w_list=input("ingresa la lista de palabras a traducir a pig latin, separada por espacio y presiona ENTER: ").split()
        oracion=f.traductor_pig_latin(w_list)
        print(oracion)       
    elif menu == 3:
        lista_frutas=input("ingresa la lista de frutas, separada por espacio y presiona ENTER: ").split()
        vitamina=f.identificador_frutas(lista_frutas)
        print(vitamina)
    elif menu == 4:
        frase1=input("introducir una frase ENTER: ").split()
        frase2=frase1.copy()
        f.son_palindromos(frase1, frase2)
    else:
        print("## porfavor elige uno de los numeros  del 1 al 4##")
    print("trabajo completado, Cerrando ... bye")



if __name__ == "__main__":
    main()