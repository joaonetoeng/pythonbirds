class Pessoa:
    def __init__(self, *filhos, nome, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {self}'

if __name__ == '__main__':
    joao = Pessoa(nome="João")
    luciano = Pessoa(joao, nome="Luciano")
    for f in luciano.filhos:
        print(f.nome)
    # criando atributo dinamico .sobrenome de luciano
    luciano.sobrenome = 'Ramalho'
    print(luciano.__dict__)
    print(joao.__dict__)
    del luciano.sobrenome
    print(luciano.__dict__)
    print(joao.__dict__)


