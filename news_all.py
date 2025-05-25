# Web Scraping com Python - Walisson Silva
# https://www.youtube.com/playlist?list=PLg3ZPsW_sghSkRacynznQeEs-vminyTQk

import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da notícia

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:

    # Título

    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

    print(f'Título: {titulo.text}')
    print(f'Link: {titulo['href']}')

    # Subtitulo

    subtitulo = noticia.find('a', attrs={'class': 'bstn-relatedtext'})

    if(subtitulo):
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
        print(subtitulo.text)
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Titulo,', 'Subtitulo', 'Link'])

news.to_excel('news.xlsx', index=False)