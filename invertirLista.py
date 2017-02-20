def invertir(lista,lista2):
    if lista==[]:
        return lista
    else:
        lista2=invertir(lista[:-1],lista2)[0]
        return lista2
lista=[1,2,3,4,5,6]
lista2=[]
print(invertir(lista,lista2))
    
