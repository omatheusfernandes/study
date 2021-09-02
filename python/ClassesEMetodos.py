# Class
# Syntaxe

#Marca, Memória Ram, Placa de Vídeo

class Computador:
    def __init__(self):
        self.marca = 'Asus'
        self.memoria_ram = '8gb'
        self.placa_de_video = 'NVidia'
    pass

computador01 = Computador()
print(computador01.marca)

computador02 = Computador()
print(computador02.memoria_ram)

computador03 = Computador()
print(computador03.placa_de_video)