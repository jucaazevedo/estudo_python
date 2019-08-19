def testa_for_elses():
	a = [10, 20, 30]
	for i in a:
		if i==21:
			break
		print(i)
	else:
		print("saiu 1")
	
	a = []
	for i in a:
		print(i)
	else:
		print("saiu 2")


testa_for_elses()
