def func_json():
	import json
	#json.dumps(data)
	#json.loads(data)

def func_dict():
	a = dict()
	a['primeira'] = 10
	print(a)

	b = {1:10, 2:"Juca", "quatro":"4"}
	print(b)
	print(type(b))

def func_lista():
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

def func_imports():
	import math
	import time
	import turtle

def func_string():
	if 'ABC'.isupper():
		print('maiusculas')

	uma_string = 'abacaxi'
	l1 = list(uma_string)

	lista3 = ['uma','frase','para','teste']
	delimiter = '-'
	t1= delimiter.join(lista3)
	print('t1 = ',t1)

	x = ' palavra '
	print(x)
	print(x.strip())
	print(len(x))
	print(x.upper())
	if x[2:4] == "la":
		print("deu certo")

def func_re():
	import re
	a = re.search(".*","juca")

def func_requests():
	import requests
	aa = requests.get("http://www.uol.com.br")

	print ("tamanho de aa ",len(aa.text))

def func_arquivo(nome):
	with open(nome,"r") as file:
		for line in file:
			words = line.split() #default de split eh espaco
			print("words = ",words)
			print(words[0])
			print(len(words))
			print(len(words[0]))


def funcao_for_range(last):
	print(type(last))
	for i in range(0,int(last)):
		print(i)
	else:
		print("depois do loop do for = ",i)

func_arquivo("arq.txt")


func_dict()
func_json()
func_lista()
func_imports()
func_re()
func_requests()

funcao_for_range(input("numero:"))
