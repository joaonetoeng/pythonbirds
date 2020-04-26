class Carro(object):
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

class Motor(object):
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade < 2:
            self.velocidade = 0
        else:
            self.velocidade -= 2

class Direcao(object):
    def __init__(self, valor='Norte'):
        self.valor = valor

    def girar_a_esquerda(self):
        if self.valor == 'Norte':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Norte'
        else:
            print('Indique uma direção válida. Ex.: Norte, Sul, Leste ou Oeste')

    def girar_a_direita(self):
        if self.valor == 'Norte':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Norte'
        else:
            print('Indique uma direção válida. Ex.: Norte, Sul, Leste ou Oeste')

'''
motor = Motor()
direcao = Direcao()
carro = Carro(motor, direcao)
'''