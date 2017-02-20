def potencia(n,m):
    if m==0:
        return 1
    if m<0:
        return 1/potencia(n,m*(-1))
    if m>0:
        return potencia(n,m-1)*n
n=int(input());
m=int(input());
print(potencia(n,m))
