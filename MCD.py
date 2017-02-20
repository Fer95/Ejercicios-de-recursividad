def mcd(a,b):
    if b==0:
        return a
    else:
        return mcd(b,a%b)
a= int(input("Ingrese el primer número"))
b= int (input("ingrese el segundo número"))
print ("El MCD ES :",mcd(a,b))
