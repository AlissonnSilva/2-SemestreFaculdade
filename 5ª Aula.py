from time import sleep
from random import randint
lista = []
pilha = list()
fila = []
while len(lista) < 10:
    n = randint(0,100)
    if n not in lista:
        lista.append(n)
print(f'A lista é composta pelos elementos: {lista}')
lista1 = lista[:3]
lista2 = lista[-3:]
print(f'Os três primeiros elementos são {lista1} e os três ultimos {lista2}')
print('-='*30)
while len(pilha) < 5:
    a = randint(0,100)
    if a not in pilha:
        pilha.append(a)
print(f'A pilha é composta pelos elementos {pilha}')
pilha1 = pilha[-1]
pilha2 = pilha[0]
print(f'O primeiro elemento da pilha é {pilha1} e o último {pilha2}')
print('-='*30)
print('Criando uma fila: ')
for c in range(0,5):
    fila.append(str(input(f'Digite o {c+1}º nome: ').strip()))
print(f'A Ordem da fila é {fila}')
print('-='*30)
print('       Checando se há elementos!')
print('-='*30)
if len(lista) == 0:
    print('A lista está vazia!')
else:
    print('Há elementos na lista!')
if len(pilha) == 0:
    print('A pilha está vazia!')
else:
    print('Há elementos na pilha!')
if len(fila) == 0:
    print('A fila está vazia!')
else:
    print('Há pessoas na fila!')
print('-='*30)
print('          Ordenando as estruturas e listando-as!')
print('-='*30)
lstord = sorted(lista)
print(f'A lista ordenada é : {lstord}')
pilhaord = sorted(pilha)
print(f'A pilha ordenada é : {pilhaord}')
filaord = sorted(fila)
print(f'A fila ordenada é : {filaord}')
print('-='*30)
print('          Removendo elementos da lista!')
print('-='*30)
for c in range(len(lista)):
    print(f'Removendo o elemento {lista[0]} da lista!')
    print('Removendo...')
    sleep(0.5)
    lista.pop(0)
    if len(lista) == 0:
        print('A lista agora está vazia!')
print('-='*30)
print('          Removendo elementos da pilha!')
print('-='*30)
for c in range(len(pilha)):
    print(f'Removendo o elemento {pilha[-1]} da pilha!')
    print('Removendo...')
    sleep(0.5)
    pilha.pop(-1)
    if len(pilha) == 0:
        print('A pilha agora está vazia!')
print('-='*30)
print('           Removendo pessoas da fila!')
print('-='*30)
for c in range(len(fila)):
    print(f'Retirando o(a) {fila[0]} da fila!')
    print('Removendo...')
    sleep(0.5)
    fila.pop(0)
    if len(fila) == 0:
        print('A fila agora está vazia!')


