#Faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necessária para pintá-la, 
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Qual a altura? '))
largura = float(input('Qual a largura? '))
area = altura*largura
qtdTinta = area/2 

print('As medidas da parede é igual a {}x{} e a área é igual a {}m² e a quantidade de tinta é {} litros'.format(altura, largura, area,qtdTinta))
