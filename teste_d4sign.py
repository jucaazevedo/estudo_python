import requests
import json

def le_config():
    f = open("../config_servicos")
    c = f.read()
    d = json.loads(c)
    global g_token
    global g_cryptKey
    global g_url
    g_token = d["servicos"][0]["config"]["tokenAPI"]
    g_cryptKey = d["servicos"][0]["config"]["cryptKey"]
    g_url = d["servicos"][0]["config"]["url"]
    print("g_token = ", g_token)
    print("g_cryptKey = ", g_cryptKey)
    print("g_url = ", g_url)

def imprime_depois():
    print("imprime depois")
    print("g_token = ", g_token)
    print("g_cryptKey = ", g_cryptKey)
    print("g_url = ", g_url)

def imprime_dados_response(resp):
    print('=================================================')
    print(resp)

    print(resp.status_code)
    print(resp.url)
    print(resp.headers['content-type'])
    print(resp.encoding)
#    print(resp.text)
    print(resp.json())
    print('=================================================')

def consulta_cofre():

    url = '{}/safes?tokenAPI={}&cryptKey={}'
    url_request = url.format(g_url, g_token, g_cryptKey)
    print(url_request)

    resp = requests.get(url_request)
    imprime_dados_response(resp)

def consulta_todos_documentos():
    url = '{}/documents?tokenAPI={}&cryptKey={}'
    url_request = url.format(g_url, g_token, g_cryptKey)

    resp = requests.get(url_request)
    imprime_dados_response(resp)

def listar_signatarios_documento(id_doc):
    url = '{}/documents/{}/list?tokenAPI={}&cryptKey={}'
    url_request = url.format(g_url,id_doc, g_token, g_cryptKey)
    resp = requests.get(url_request)
    imprime_dados_response(resp)

def enviar_signatarios(id_doc):
    url = '{}/documents/{}/createlist?tokenAPI={}&cryptKey={}'
    url_request = url.format(g_url, id_doc, g_token, g_cryptKey)
    dados = '{"signers":[{"email":"jazevedo@simplesmenteuse.com","act":"1","foreign":"0","certificadoicpbr":"0","assinatura_presencial":"0"}]}'
    resp = requests.post(url_request, data=dados)
    imprime_dados_response(resp)

# execucao 

le_config()
imprime_depois()
consulta_cofre()
consulta_todos_documentos()
listar_signatarios_documento('9daed4d5-a76e-4664-ab97-d823f22870f3')
#enviar_signatarios('2fd0a2e3-b0e6-48ff-a380-7379a225805f')
listar_signatarios_documento('2fd0a2e3-b0e6-48ff-a380-7379a225805f') #urso
