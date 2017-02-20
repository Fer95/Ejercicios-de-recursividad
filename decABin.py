def decABin(a):
    if a ==0
        return ""
    else:
        return decABin(a//2)+str(a%2)
    
a=int(print("Ingrese el numero decimal:"))
print("El numero en binario es:",decABin(a))
