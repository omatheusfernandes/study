#Troque o sobrenome do individuo

nome = input('Primeiro nome: ')
sobrenome = input('Sobrenome: ')

while sobrenome != 'Siqueira' and sobrenome != 'siqueira':
    print('Seu nomé é {} {}!'.format(nome, sobrenome))
    sobrenome = input('Sobrenome: ')
else: 
    print('Nome aceito!')