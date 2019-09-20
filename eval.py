a = '{"chave1":1, "chave2":2}'

j = eval(a)

print(type(j))

a = '["saida", "entrada"]'

j = eval(a)

print(type(j))

a = '("saida", "entrada")'

j = eval(a)

print(type(j))
