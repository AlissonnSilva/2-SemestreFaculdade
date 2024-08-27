def fibonacci(n):
    t1 = 1
    t2 = 1
    i = 2
    if n == 1:
        print('1')
    if n == 2:
        print('1 -> 1')
    if n > 2:
        print(f'{t1} -> {t2}',end='')
        while i < n:
            t3 = t1+t2
            print(f' -> {t3}', end='')
            t1 = t2
            t2 = t3
            i += 1

def fatorial(n):
    if n <=1:
        return 1
    else:
        return n * fatorial(n-1)

def fibonacci1(n):
    if n <=2:
        return 1
    else:
        return fibonacci1(n-2)+fibonacci1(n-1)
    
print(fatorial(5))