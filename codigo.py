def func1(nome):
	import requests
	import re
	import math
	import time
	import turtle
	import json

	lista = [10,201,30]
	lista.append(40)
	lista.extend([25,12])

	print(lista)
	lista.sort()
	print(lista)
	print(sum(lista))

	lista2 = [10,20,30,40,50,60]
	bo = lista2.pop(1)
	del lista2[3]
	lista2.remove(60)
	print('lista 2 =',lista2)

	if 'ABC'.isupper():
		print('maiusculas')

	uma_string = 'abacaxi'
	l1 = list(uma_string)

	lista3 = ['uma','frase','para','teste']
	delimiter = '-'
	t1= delimiter.join(lista3)
	print('t1 = ',t1)
	#json.dumps(data)
	#json.loads(data)
	x = ' palavra '
	print(x)
	print(x.strip())
	print(len(x))
	print(x.upper())
	if x[2:4] == "la":
		print("deu certo")

	a = re.search(".*","juca")
	aa = requests.get("http://www.uol.com.br")

	print ("tamanho de aa ",len(aa.text))
	with open(nome,"r") as file:
		for line in file:
			words = line.split() #default de split eh espaco
			print("words = ",words)
			print(words[0])
			print(len(words))
			print(len(words[0]))

def func2():
	if True:
		print(1)
	print(2)

def func3(): #testando identacao com espacos
 if True:
  print ('a')
  print('b')

def funcao_for_range(last):
	for i in range(1,int(last)):
		print(i)
	else:
		print(i+10)

func1("arq.txt")
func2()
func3()

funcao_for_range(input("numero:"))


