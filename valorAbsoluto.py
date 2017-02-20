def valorAbsoluto(num):
    if num>=0:
        return num
    else:
        return valorAbsoluto(num*(-1))
num=int(input());
print(valorAbsoluto(num))
