def invertir(lista):
    if lista==[]:
        return lista
    else:
        return [lista[-1]]+invertir(lista[:-1])
lista=[1,2,3,4,5,6]
print(invertir(lista))
    
