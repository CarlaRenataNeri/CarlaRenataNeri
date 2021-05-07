def numero_quadrado(numero):
	quadrado = numero * numero
	return quadrado

def calcular_imc(peso, altura):
	altura_quadrada = numero_quadrado(altura)
	imc = peso / altura_quadrada
	return imc

def classificar(imc):
	if imc < 18.5:
		print('magreza')
	elif imc >= 18.5 and imc < 25:
		print('normal')
	elif imc >= 25 and imc < 30:
		print('sobrepeso')
  elif imc >= 30 and imc < 40:
		print('obesidade')
  else:
    print('obesidade grave')

peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))
meu_imc = calcular_imc(peso, altura)
classificar(meu_imc)
