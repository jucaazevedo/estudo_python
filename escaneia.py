def escaneia():
	import json
	f = open("AutomationAPISampleFlow.json")
	l = f.read()
	print(l)
	print("")
	j = json.loads(l)
	print(type(j))
	print(j['Defaults']['Application'])

escaneia()
