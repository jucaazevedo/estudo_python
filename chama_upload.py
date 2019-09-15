    f = open("../config_servicos_demo_jucaof")
    c = f.read()
    d = json.loads(c)
    g_token = d["servicos"][0]["config"]["tokenAPI"]
    g_cryptKey = d["servicos"][0]["config"]["cryptKey"]
    g_url = d["servicos"][0]["config"]["url"]
    g_cofre = d["servicos"][0]["config"]["cofre"]

    url = '{}/documents/{}/uploadbinary?tokenAPI={}&cryptKey={}'
    url_request = url.format(g_url, g_cofre, g_token, g_cryptKey)
    dados = '{{"base64_binary_file" : "{docz}", "mime_type" : "application/pdf", "name" : "pdf_peq.pdf"}}'
    dados_envio = dados.format(docz=docbase64)
    print("dados_envio = ", dados_envio)
    resp = requests.post(url_request, data=dados_envio)
    imprime_dados_response(resp)
    ret_id_doc = resp.json['uuid']
    return ret_id_doc
