def binADec(a,cont):
    if a<1:
        return 0
    else:
        cont+=1
        return ((int((a%10)*2))^cont)+binADec((a/10),cont)
print("Ingrese el numero binario:")    
a=int(input())
print("El numero en decimal es:",binADec(a,0))
