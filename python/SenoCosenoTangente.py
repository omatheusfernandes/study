#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Insira o valor do ângulo desejado: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Ângulo: {}° \nSeno: {:.2f}° \nCosseno: {:.2f}° \nTangente de {:.2f}°'.format(angulo, seno, cosseno, tangente))