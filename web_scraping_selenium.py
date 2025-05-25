# Documentação: https://selenium-python.readthedocs.io/

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from time import sleep

options = Options()
options.set_preference("app.update.enabled", False)

service = Service('geckodriver.exe')

navegador = webdriver.Firefox(service=service)

navegador.get('https://www.walissonsilva.com/blog')

sleep(3)

elemento = navegador.find_element("tag name", "input")

elemento.send_keys('data')