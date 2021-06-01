import detector_virus as d_v

def main():
    V = 'coronavirus'
    P = input('ingrese las secuencias de las persona, c/u separada  por espacios y presione ENTER: ').split()
    positivos=[]
    negativos=[]

    for i in range(len(P)):
        if d_v.detector_v(V,P[i]):
            positivos.append(P[i])
        else:
            negativos.append(P[i])
    print("casos  positivos: ")
    print(positivos)
    print("casos  negativos: ")
    print(negativos)


if __name__ == "__main__":
    main()