class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá meu nom é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nomes_e_atributos_de_calsse(cls):
        return f'{cls}, olhos = {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe_Pessoa = super().cumprimentar()
        return f'{cumprimentar_da_classe_Pessoa} . Aperto de mão.'

if __name__ == '__main__':
    joao = Homem(nome="João")
    luciano = Homem(joao, nome="Luciano")
    for f in luciano.filhos:
        print(f.nome)
    print(luciano.cumprimentar())

