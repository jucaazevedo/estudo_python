dados = '{{"base64_binary_file" : "{ali}", "mime_type" = "application/pdf", "name" : "pdf_peq.pdf"}}'
juca = "juca1"
dados_envio = dados.format(ali=juca)
print(dados_envio)

dados = '{{"base64_binary_file" : "{docz}", "mime_type" = "application/pdf", "name" : "pdf_peq.pdf"}}'
dados_envio = dados.format(docz=juca)
print(dados_envio)
