#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com porcentagem de desconto inserida.

precoProduto = float(input('Preço do produto: R$'))
porcentagem = int(input('Insira a porcentagem de desconto: '))
novoPreco = precoProduto - (precoProduto*porcentagem/100)

print('O produto  de R${:.2f} valor com desconto de {}% é igual a R${:.2f}'.format(precoProduto, porcentagem, novoPreco))