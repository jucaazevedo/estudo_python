def escaneia():
	import json
	f = open("AutomationAPISampleFlow.json")
	l = f.read()
	print("texto:")
	print(l)
	print("")
	j = json.loads(l)
	print(type(j))
	print("dictionary::")
	print(j)
	print(j['Defaults']['Application'])

escaneia()
