import requests
import json

def obter_lista_de_artigos():
    url = "https://newsapi.org/v2/top-headlines"
    parametros = {
        "country": "us",
        "apiKey": "ea394d1cdc334ef3b1840d9acb0b3765"  
    }

    resposta = requests.get(url, params=parametros)
    dados = resposta.json()

    if resposta.status_code == 200 and dados['status'] == 'ok':
        artigos = dados['articles']
        for artigo in artigos:
            autor = artigo['author']
            titulo = artigo['title']
            descricao = artigo['description']
            print(f"Autor: {autor}")
            print(f"Título: {titulo}")
            print(f"Descrição: {descricao}")
            print("--------------------")
    else:
        print("Falha ao obter a lista de artigos.")

obter_lista_de_artigos()
