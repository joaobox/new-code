# -*- coding: utf-8 -*-

""" calculadora 
"""
print("_calculadora_")

fechar = False

while sair == False:

	num1 = input("Digite o primeiro numero: ")
	num1 = int(num1)
	operador = input("Digite o operador: ")
	num2 = input("Digite o segundo numero: ")
	num2 = int(num2)

	# soma
	if operador == "+":
	    operacao = num1 + num2

	# subitração
	if operador == "-":
	    operacao = num1 - num2

	#divisão
	if operador == "/":
		operacao = num1 / num2

	#mutiolicação
	if operador == "*":
		operacao = num1 * num2

	print("resultado")
	print("operação")

	teste = ("Resultado: ")
	print(operacao)

	teste = input("Deseja sair (n/y): ")
	if teste == "s":
		fechar = True
