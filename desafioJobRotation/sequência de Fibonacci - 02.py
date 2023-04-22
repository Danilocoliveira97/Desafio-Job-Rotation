def fibonacci(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

lista=list()
n = int(input("Número para calculo de fibonnaci : "))
n2=n
print(" Sequência Fibonacci : ")
for n in range(0, n):
    print(fibonacci(n))
    lista.append(fibonacci(n))


if n2 in lista:
    print(f'O número {n2} faz parte da Sequência')
else:
    print(f'O número {n2} não faz parte da Sequência')