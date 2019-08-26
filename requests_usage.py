import requests

#r = requests.get('https://api.github.com/user', auth=('user', 'pass'))


#url = 'https://api.github.com/some/endpoint'
#headers = {'user-agent': 'my-app/0.0.1'}

#r = requests.get(url, headers=headers)

#r = requests.post('https://httpbin.org/post', data = {'key':'value'})

parametros={'idList' : '1'}
r = requests.get('http://localhost:31415/situacao', params=parametros)

print(r.status_code)
print(r.url)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())
