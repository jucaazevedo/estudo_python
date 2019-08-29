import requests

#r = requests.get('https://api.github.com/user', auth=('user', 'pass'))


#url = 'https://api.github.com/some/endpoint'
#headers = {'user-agent': 'my-app/0.0.1'}

#r = requests.get(url, headers=headers)

#r = requests.post('https://httpbin.org/post', data = {'key':'value'})

dados = { "signatureFileName": "assinatura.p7s", "documentFileName": "assinatura.p7s", "detailsLevel": 1, "generateReport": False, "extractOriginalContent": False }

token = '5535b442be894fdcba4c1ad06e260b23'

headers = {'token': token }

r = requests.post('https://api-sbx.portaldeassinaturas.com.br/api/v2/SignatureVerifier/verifySignature', headers=headers, data=dados)

#parametros={'idList' : '1357'}
#r = requests.get('http://localhost:31415/situacao', params=parametros)

print(r.status_code)
print(r.url)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())

