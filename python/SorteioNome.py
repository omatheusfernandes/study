#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

nome1 = str(input('Digite um nome: '))
nome2 = str(input('Digite um nome: '))
nome3 = str(input('Digite um nome: '))
nome4 = str(input('Digite um nome: '))

lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)

print('O nome sorteado foi: {}'.format(escolhido))
