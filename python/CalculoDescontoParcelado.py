#Calcular preço de um produto para a vista e a prazo
#A prazo, adicionar R$6,00 ao mes
#A vista, 5% de desconto

precoProduto = float(input('Qual o preço do produto? R$'))
meses = int(input('Quantos meses? '))
calculoAVista = precoProduto - (precoProduto * 5/100)
calculoParcelado = precoProduto + (0.28*meses)

print('A vista: R${:.2f} \nParcelado: R${:.2f}'.format(calculoAVista, calculoParcelado))