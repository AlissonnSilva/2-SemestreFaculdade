def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

termos = 10
for c in range(1, termos+1):
    print(fibonacci(c), end=' -> ')
print('fim')

numero_da_sequencia = 7
iterador = 1
while (iterador <= numero_da_sequencia):
    resultado = fibonacci(iterador)
    iterador += 1
    print(resultado, end=' -> ')
print('fim')

"""lista = list()
lista.append(1)
lista.append(1)
termos = 20000
print('=-'*15)
print('     SEQUÊNCIA FIBONACCI')
print('=-'*15)
for c in range(1, termos-1):
    lista.append(lista[-1]+lista[-2])
print(lista)"""




"""def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


lista = []
termos = 10
for c in range(1, termos+1):
    lista.append(fibonacci(c))
print(lista)"""
