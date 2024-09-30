from time import sleep
class Classe:
    def __init__ (self,memoriaram,cpu,so,on,off):
        self.memoriaram = memoriaram
        self.cpu = cpu
        self.so = so
        self.on = on
        self.off = off
    def ligar(self):
        print(f'NOME: {self.memoriaram} | STATUS: {self.on}',end='...')
        print()
        sleep(1)
        print(f'NOME: {self.cpu} | STATUS: {self.on}',end='...')
        print()
        sleep(1)
        print(f'NOME: {self.so} | STATUS: {self.on}',end='...')
        print()
        sleep(1)
    def desligar(self):
        print(f'NOME: {self.memoriaram} STATUS: {self.off}',end='...')
        print()
        sleep(1)
        print(f'NOME: {self.cpu} STATUS: {self.off}',end='...')
        print()
        sleep(1)
        print(f'NOME: {self.so} STATUS: {self.off}',end='...')
        print()
        sleep(1)
    def sobre(self):
        print(f'SOBRE:{classe1.memoriaram},{classe1.cpu},{classe1.so}')
classe1 = Classe('Memoria RAM 36Gb','CPU i9','Sistema Operacional(SO) Linux mint','LIGANDO','DESLIGANDO')
classe1.ligar()
classe1.desligar()
classe1.sobre()
