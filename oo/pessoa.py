class Pessoa:
    def __init__(self, nome, idade=26):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'Olá {self}'

if __name__ == '__main__':
    p1 = Pessoa("Luciano", 40)
    p2 = Pessoa("João")
    print(Pessoa.cumprimentar(p1))
    print(p1.cumprimentar())
    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    p1.nome = 'Renzo'
    print(p1.nome)


