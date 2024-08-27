#funções:
import time
a = int(input('Digite um número: '))
def incrementador(numero):
    numero+=1
    numero2 = numero+2
    num = int(input('Digite um número para criar uma sequencia a partir do primeiro numero digitado: (apenas numeros maiores que o primeiro) '))
    time.sleep(0.5)
    for b in range(numero, num+1):
        print(b)
    return numero, numero2  #faz com que o resultado seja salvo no nome da função
#incrementador(a) #joga o input na função
novo_numero, numero2= incrementador(a)
print('chamando a função: ')
print(f'O novo numero é {novo_numero} \ne a soma com 2 é {numero2}')

