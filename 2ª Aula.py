"""def fatorial(a):
    if a == 0:
        return 1
    else:
        return a * fatorial(a-1)
b = int(input('Digite um numero: '))
print(f'O fatorial de {b} é igual a {fatorial(b)} ')"""
"""def fatorial_iterativo(a):
    if a == 0:
        return 1
    else:
        resultado = 1
    while a > 0:
        resultado *= a
        a-=1
    return resultado
b = int(input('Digite um numero: '))
fatorial_iterativo(b)
print(f'O fatorial de {b} é igual a {fatorial_iterativo(b)} ')"""
"""def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))"""
"""print('='*22)
print('Sequência de Fibonacci')
print('='*22)
n = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1,t2), end='')
c = 3
while c <= n:
    t3 = t1+t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c+=1
print(' -> FIM')
print('~'*30)"""
