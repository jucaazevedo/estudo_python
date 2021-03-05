import random

x = random.randint(1,10)
y = random.randint(1,10)

print ("Quanto é ", x , " * ", y)

resultado = x * y

resposta = int(input())

if (resposta == resultado):
	print("Você acertou")
else:
	print("Você errou")
