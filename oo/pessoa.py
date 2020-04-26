class Pessoa:
    olhos = 2
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
    luciano.sobrenome = 'Ramalho'
    print(luciano.__dict__)
    print(joao.__dict__)
    print(luciano.olhos)
    print(joao.olhos)
    print(Pessoa.olhos)
    print(id(Pessoa.olhos), id(joao.olhos), id(luciano.olhos))
    print(id(joao.nome), id(luciano.nome))


