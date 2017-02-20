def factorial(num):
    if num==0:
        return 1
    else:
        return factorial(num-1)*num
num=int(input());
print(factorial(num))
