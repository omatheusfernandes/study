#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o salário? R$'))
novoSalario = salario + (salario * 15/100)

print('O novo salário é: R${:.2f}'.format(novoSalario))