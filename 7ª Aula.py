# 1 - Faça uma função que receba um dicionário e um número N. Apresentar os primeiros N itens
#  e os últimos N itens do dicionário
# 2 - Faça uma função que troca as chaves e os valores de lugar
#  (Exemplo "chave" : "Valor" vira -> "Valor" : "chave")
# 3 - Criar um programa que analisa as notas de vários alunos.
# Dado um dicionário onde as chaves são os nomes dos alunos e os valores são listas
#  com suas respectivas notas em diferentes disciplinas, o programa deve calcular e exibir:
# 3a - A média de cada aluno.
# 3b - A nota mais alta e mais baixa de cada aluno.
# 3c - O aluno com a maior média e o aluno com a menor média.
"""from random import randint
dicionario = {
    'numeros': []
}
def função(dici, n):
    print(dici['numeros'])
    print(f'Os {n} primeiros números são: ')
    for c in dici['numeros'][:n]:
        print(c, end=' ')
    print(f'\nOs {n} ultimos números são: ')
    for c in dici['numeros'][-n:]:
        print(c, end=' ')
while len(dicionario['numeros']) < 10:
    n = randint(0, 100)
    if n not in dicionario['numeros']:
        dicionario['numeros'].append(n)
numero = int(input('Quantos numeros deseja ver: '))
função(dicionario, numero)"""

# 2 - Faça uma função que troca as chaves e os valores de lugar
#  (Exemplo "chave" : "Valor" vira -> "Valor" : "chave")
"""dicionario2 = {
    'chave': 'valor'
}

def trocar(dici):
    dici2 = {v: k for k ,v in dici.items()}
    return dici2
dici_invertido = trocar(dicionario2)
#normal
print(dicionario2)
#invertido
print(dici_invertido)"""


# 3 - Criar um programa que analisa as notas de vários alunos.
# Dado um dicionário onde as chaves são os nomes dos alunos e os valores são listas
#  com suas respectivas notas em diferentes disciplinas, o programa deve calcular e exibir:
# 3a - A média de cada aluno.
# 3b - A nota mais alta e mais baixa de cada aluno.
# 3c - O aluno com a maior média e o aluno com a menor média.

dicionario3 = dict()
notas = list()
medias = list()
soma = 0
media = 0
while True:
    chave = str(input('Nome: '))
    notas.append(int(input('Nota em Robótica: ')))
    notas.append(int(input('Nota em Matematica: ')))
    notas.append(int(input('Nota em Programação: ')))
    dicionario3 = {chave: notas}
    esc = str(input('Deseja adicionar mais algum aluno? [S/N]  ')).upper()[0]
    if esc == 'N':
        break




    

    


