import requests
import json

def le_config():
    f = open("../config_servicos_certisign")
    c = f.read()
    d = json.loads(c)
    global g_token, g_cryptKey, g_url, g_cofre, g_doc_base64
    g_token = d["servicos"][0]["config"]["tokenAPI"]
    g_url = d["servicos"][0]["config"]["url"]
    g_doc_base64 = b'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'
    print("g_token = ", g_token)
    print("g_url = ", g_url)
    print("g_doc_base64 = ", type(g_doc_base64))
    print("g_doc_base64 = ", g_doc_base64)

def imprime_depois():
    print("imprime depois")
    print("g_token = ", g_token)
    print("g_url = ", g_url)

def imprime_dados_response(resp):
    print('=================================================')
    print(resp)

    print(resp.status_code)
    print(resp.url)
    print(resp.headers['content-type'])
    print(resp.encoding)
#    print(resp.text) 
# text eh atributo e json() eh metodo
    print(resp.json())
    print('=================================================')


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

def upload_arquivo(docbase64):
    url = '{}/document/upload'
    url_request = url.format(g_url)
    dados = {"fileName" : "pdf_peq.pdf"}
    dados["bytes"] = docbase64
    headers = {'Content-type': 'application/json'}
    headers["Token"] = g_token
    resp = requests.post(url_request, data=dados, headers=headers)
    imprime_dados_response(resp)
    ret_id_doc = resp.json()['uploadId']
    return ret_id_doc

def enviar_arquivo_para_assinatura(id_doc):
    url = '{}/document/create'
    url_request = url.format(g_url)
    dados = '{"document":{"name":"pdf_pequeno_renomeado.pdf","upload":{"id":"{}","name":"pdf_pequeno_renomeado.pdf"}},"electronicSigners":[{"name":"jazevedo","email":"jazevedo@simplesmenteuse.com"}]}'
    dados.format(id_doc)
    headers = {'Content-type': 'application/json'}
    headers["Token"] = g_token
    resp = requests.post(url_request, data=dados, headers=headers)
    imprime_dados_response(resp)

def cadastrar_webhook(id_doc):
    url = '{}/documents/{}/webhooks?tokenAPI={}&cryptKey={}'
    url_request = url.format(g_url, id_doc, g_token, g_cryptKey)
#    dados = '{"url" : "https://suse.requestcatcher.com"}'
    dados = '{"url" : "http://d01.office1.simplesmenteuse.com.br/SuseToolsBatch/d4SignWebService"}'
    headers = {'Content-type': 'application/json'}
    resp = requests.post(url_request, data=dados, headers=headers)
    imprime_dados_response(resp)

# execucao 

le_config()
#imprime_depois()

ret_id_arq = upload_arquivo(g_doc_base64)
enviar_arquivo_para_assinatura(ret_id_arq)

#consulta_todos_documentos()
#listar_signatarios_documento('9daed4d5-a76e-4664-ab97-d823f22870f3')
#listar_signatarios_documento('2fd0a2e3-b0e6-48ff-a380-7379a225805f') #urso


