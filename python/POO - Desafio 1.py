# #Desafio 1
# Criar classe 'Carro' com, no mínimo, 3 propriedades e métodos

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligarCarro(self):
        print('Estou ligando')
    
    def entrarNoCarro(self):
        print('Estou entrando')

    def darMarcha(self):
        print('Marcha')

    def exibirInfos(self):
        print(self.marca, self.modelo, self.ano)

carro1 = Carro('Ford', 'Ka', '2003')
carro1.ligarCarro()
carro1.entrarNoCarro()
carro1.exibirInfos()