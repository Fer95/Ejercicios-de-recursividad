def multiplicar(n,m):
    if m==0:
        return 0
    if m>0:
        return multiplicar(n,m-1)+n
    if m<0:
        return multiplicar(n,m+1)-n
n=int(input());
m=int(input());
print(multiplicar(n,m))
