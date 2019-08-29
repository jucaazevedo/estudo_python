import requests

token = 'live_70f4d6f07cadc3c1c390c994ee5fe31781a0fae559962f007799990969053c64'
cryptKey = "live_crypt_wAFD0RfRdpayOn9YOrTwoUCTcoxlQt3h"

def imprime_dados_response(resp):
    print('=================================================')
    print(resp)

    print(resp.status_code)
    print(resp.url)
    print(resp.headers['content-type'])
    print(resp.encoding)
    print(resp.text)
    print(resp.json())
    print('=================================================')

def consulta_cofre():

    url = 'https://secure.d4sign.com.br/api/v1/safes?tokenAPI={}&cryptKey={}'
    url_request = url.format(token, cryptKey)
    print(url_request)

    resp = requests.get(url_request)
    imprime_dados_response(resp)

def consulta_todos_documentos():
    url = 'https://secure.d4sign.com.br/api/v1/documents?tokenAPI={}&cryptKey={}'
    url_request = url.format(token, cryptKey)

    resp = requests.get(url_request)
    imprime_dados_response(resp)

def listar_signatarios_documento(id_doc):
    url = 'https://secure.d4sign.com.br/api/v1/documents/{}/list?tokenAPI={}&cryptKey={}'
    url_request = url.format(id_doc, token, cryptKey)
    resp = requests.get(url_request)
    imprime_dados_response(resp)

# execucao 

consulta_cofre()
consulta_todos_documentos()
listar_signatarios_documento('9daed4d5-a76e-4664-ab97-d823f22870f3')
