def func1(nome):
	import requests
	aa = requests.get("http://www.uol.com.br")

	print ("tamanho de aa ",len(aa.text))
	with open(nome,"r") as file:
	for line in file:
		words = line.split()
		print("words = ",words)
		print(words[0])
		print(len(words))
		print(len(words[0]))

func1("arq.txt")


