def detector_v(V, P):
    detec=True
    for i in range(len(P)):
        
        if P[i] in V:
            detec=detec and True
        else:
            detec=detec and False
    return detec
        

            
    


