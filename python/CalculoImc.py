#Calcular IMC com base em altura e peso

peso = float(input('Qual o peso atual? '))
altura = float(input('Qual sua altura em centimetros? '))
conversaoAltura = altura/100
imc = peso/(conversaoAltura*conversaoAltura)
imcIdeal = 24.9

if imc <= imcIdeal:
    print('Você está no peso ideal!')
else:
    print('Você está acima do peso e o seu IMC é igual a {}'.format(imc))