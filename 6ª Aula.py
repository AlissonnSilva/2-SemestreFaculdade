"""Façam em Python faça um dicionário e em seguida:
Adicione 10 números
Liste os 10 números
Liste os 3 primeiros e os 3 últimos
Faça um segundo dicionário
Adicione 5 nomes
Liste-os
Em um novo dicionário, Faça:
Chaves: Nomes de pessoas
Valor: Número aleatório
Imprima o dicionário mostrando chaves e valores"""
from random import randint
dicionario = {'numeros': [], 'lista3p': [], 'lista3u': []}
while len(dicionario['numeros']) < 10:
    a = randint(0, 100)
    if a not in dicionario['numeros']:
        dicionario['numeros'].append(a)
print(dicionario['numeros'])
dicionario['lista3p'].append(dicionario['numeros'][:3])
print(f'Os três primeiros valores são {dicionario["lista3p"]}')
dicionario['lista3u'].append(dicionario['numeros'][-3:])
print(f'Os três ultimos valores são {dicionario["lista3u"]}')
dicionario2 = {'nomes': []}
for c in range(0, 5):
    dicionario2['nomes'].append(
        str(input(f'Insira o nome da {c+1}ª pessoa: ')))
print(f'Os nomes digitados foram: {dicionario2["nomes"]}')
dicionario3 = {'Chaves': dicionario2['nomes'], 'Valor': dicionario['numeros']}
print(f'Terceiro dicionario: {dicionario3}')
