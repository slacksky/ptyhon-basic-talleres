

def produccion_semanal(Nvacas):
    Kgmant=4 * Nvacas
    Kgqueso=(4/3) * Nvacas
    return Kgmant, Kgqueso

def vacas_requeridas(Kgmant, Kgqueso):
    import math

    vacasmant=math.ceil(Kgmant/4)
    vacasqueso=math.ceil(Kgqueso*(3/4))
    if vacasmant>=vacasqueso:
        Nvacas=vacasmant
    else:
        Nvacas=vacasqueso

    #Kgs_Vaca=16/3
    #KgTotal=Kgmant+Kgmant
    #Nvacas=math.ceil(KgTotal/Kgs_Vaca) 
    
    return Nvacas