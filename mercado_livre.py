# Obtendo produtos do Mercado Livre a partir de uma busca realizada pelo usuário

import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []

url_base ='https://lista.mercadolivre.com.br/'

produto = input('Qual produto você deseja? ')

response = requests.get(url_base + produto)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card poly-card poly-card--grid-card poly-card--large poly-card--MOT andes-card--flat andes-card--padding-0 andes-card--animated'})

for produto in produtos:
    titulo = produto.find('a', attrs={'class': 'poly-component__title'})
    link = titulo['href']
    preco = produto.find('span', attrs='andes-money-amount__fraction')

    lista_produtos.append([titulo.text, link, preco.text])

    print(f'Título: {titulo.text}')
    print(f'Link: {link}')
    print(f'Preco: {preco.text}\n')

# print(produto.prettify())

# Exportando os dados obtidos

df = pd.DataFrame(lista_produtos, columns=['Titulo', 'Link', 'Preco'])
df.to_csv('lista_produtos.csv', index=False)
