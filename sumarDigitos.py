def sumarDigitos(numero):
    if numero>=10:
        return numero%10+sumarDigitos(int(numero/10))
    else:
        return numero
numero=int(input())
print(sumarDigitos(numero))
