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


# Declaração das constantes do problema
NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao(object):
    rotacao_a_direcita_dict = {NORTE:LESTE, LESTE:SUL, SUL:OESTE, OESTE:NORTE }

    def __init__(self, valor='Norte'):
        self.valor = valor

    def girar_a_esquerda(self):
        # Como o eu implementei
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
        # Como o Renzo implementou
        self.valor = self.rotacao_a_direcita_dict[self.valor]

motor = Motor()
direcao = Direcao()
carro_do_renzo = Carro(motor, direcao)
carro_do_renzo.girar_a_direita()
carro_do_renzo.girar_a_direita()
print(carro_do_renzo.calcular_direcao())