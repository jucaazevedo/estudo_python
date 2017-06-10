def acha_palavra():
	for linha in open("words.txt"):
		anterior = ''
		contador = 0
		for letra in linha:
			if letra == anterior:
				anterior = ''
				contador += 1
			else:
				anterior = letra
		if contador == 3:
			print(linha)

acha_palavra()
