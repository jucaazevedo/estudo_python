def func1(nome):
	import requests
	import re
	import math
	import time
	import turtle
	import json

	#json.dumps(data)

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
	for i in range(1,last):
		print(i)
	else:
		print(i+10)

funcao_for_range(raw_input("numero:"))

func1("arq.txt")
func2()
func3()


