import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.common.by import By


options = Options()
# options.add_argument('--headless') # oculta o navegador
# options.add_argument('window-size=400,800') # não funcionou, verificar
options.set_preference("app.update.enabled", False)

service = Service('geckodriver.exe')

navegador = webdriver.Firefox(service=service, options=options)

navegador.get('https://www.airbnb.com')

sleep(2)

input_place = navegador.find_element("tag name", "input")
input_place.send_keys('Brasília')
input_place.submit()

# Se fosse o caso de buscar uma tag filha:

# sleep(0.5)
# button_stay = navegador.find_element(By.CSS_SELECTOR, 'button > img')
# button_stay.click()

# Para clicar no último botão:

# buttons = navegador.find_elements(By.TAG_NAME, 'button')[-1]
# nextButton = buttons[-1]
# nextButton.click()

sleep(4) # para carregar tudo

# >>> falta implementar o clique na busca

page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')

print(site.prettify())
