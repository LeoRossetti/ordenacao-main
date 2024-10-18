lista = [2,1,5,7,3]



for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[j] > lista[i]:
            lista[j], lista[i] = lista[i], lista[j]
    

print(lista)
    
    
    
    
    # '''if lista[i] > lista[i+1]:

    #     lista[:i], lista[i+1:] = lista[i+1:], lista[:i]
    # print(lista)'''



