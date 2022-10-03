import re
from urllib import request
import requests
from bs4 import BeautifulSoup
from lxml import etree

def allprod(producto):
    lista_titulos = []
    lista_url = []
    lista_precios = []
    siguiente = "https://listado.mercadolibre.com.mx/"+producto+"-reacondicionados_Desde_0_NoIndex_True"
    #siguiente = "https://listado.mercadolibre.com.mx/celulares-telefonia/celulares-smartphones/reacondicionado/celulares-reacondicionados_Desde_0_NoIndex_True"
    while True:
        r = requests.get(siguiente)
        if r.status_code==200:
            soup = BeautifulSoup(r.content, "html.parser")
            
            #titulos funciona
            titulos = soup.find_all("h2", attrs={"class":"ui-search-item__title"})
            titulos = [i.text for i in titulos ]
            lista_titulos.extend(titulos)
            
            #url xpath roto
            urls = soup.find_all("a", attrs = {"class": "ui-search-item__group__element shops__items-group-details ui-search-link"})
            #ui-search-item__group__element shops-custom-secondary-font ui-search-link  
            urls = [i.get("href") for i in urls]
            lista_url.extend(urls)
            
            #precios xpathroto
            dom = etree.HTML(str(soup))
            precios = dom.xpath('//li[@class="ui-search-layout__item shops__layout-item"]//div[@class="ui-search-result__content-columns shops__content-columns"]//div[@class="ui-search-result__content-column ui-search-result__content-column--left shops__content-columns-left"]//div[@class="ui-search-item__group ui-search-item__group--price shops__items-group"]//div[@class="ui-search-item__group__element ui-search-price__part-without-link shops__items-group-details"]//div[@class="ui-search-price ui-search-price--size-medium shops__price"]//div[@class="ui-search-price__second-line shops__price-second-line"]//span[@class="price-tag ui-search-price__part shops__price-part"]//span[@class="price-tag-amount"]//span[2]')
            #//li[@class="ui-search-layout__item shops__layout-item"]//div[@class="ui-search-result__content-columns shops__content-columns"]//div[@class="ui-search-result__content-column ui-search-result__content-column--left"]//div[@class="ui-search-item__group ui-search-item__group--price shops__items-group"]//div[@class="ui-search-item__group__element ui-search-price__part-without-link shops-custom-secondary-font"]//div[@class="ui-search-price ui-search-price--size-medium shops__price"]//div[@class="ui-search-price__second-line"]//span[@class="price-tag ui-search-price__part shops-custom-secondary-font"]//span[@class="price-tag-amount"]/span[2]
            precios = [i.text for i in precios]
            lista_precios.extend(precios)
            
            ini = soup.find_all("span", attrs = {"class":"andes-pagination__link"})[0].text
            ini = int(ini)
            can = soup.find("li",attrs={"class":"andes-pagination__page-count"})
            can = int(can.text.split(" ")[1])

        else:
            print("ERROR RESPUESTA")
            break
        print(ini, can)
        if ini == can:
            break
        siguiente = dom.xpath('//div[@class="ui-search-pagination shops__pagination-content"]//ul[@class="ui-search-pagination andes-pagination shops__pagination"]//li[@class="andes-pagination__button andes-pagination__button--next shops__pagination-button"]//a')[0].get("href")
    
    return lista_titulos, lista_url, lista_precios

def limprod(producto, limite):
    lista_titulos = []
    lista_url = []
    lista_precios = []
    siguiente = "https://listado.mercadolibre.com.mx/"+producto+"-reacondicionados_Desde_0_NoIndex_True"
    #siguiente = "https://listado.mercadolibre.com.mx/celulares-telefonia/celulares-smartphones/reacondicionado/celulares-reacondicionados_Desde_0_NoIndex_True"
    while True:
        r = requests.get(siguiente)
        if r.status_code==200:
            soup = BeautifulSoup(r.content, "html.parser")
            
            #titulos funciona
            titulos = soup.find_all("h2", attrs={"class":"ui-search-item__title"})
            titulos = [i.text for i in titulos ]
            lista_titulos.extend(titulos)
            
            #url xpath roto
            urls = soup.find_all("a", attrs = {"class": "ui-search-item__group__element shops__items-group-details ui-search-link"})
            #ui-search-item__group__element shops-custom-secondary-font ui-search-link  
            urls = [i.get("href") for i in urls]
            lista_url.extend(urls)
            
            #precios xpathroto
            dom = etree.HTML(str(soup))
            precios = dom.xpath('//li[@class="ui-search-layout__item shops__layout-item"]//div[@class="ui-search-result__content-columns shops__content-columns"]//div[@class="ui-search-result__content-column ui-search-result__content-column--left shops__content-columns-left"]//div[@class="ui-search-item__group ui-search-item__group--price shops__items-group"]//div[@class="ui-search-item__group__element ui-search-price__part-without-link shops__items-group-details"]//div[@class="ui-search-price ui-search-price--size-medium shops__price"]//div[@class="ui-search-price__second-line shops__price-second-line"]//span[@class="price-tag ui-search-price__part shops__price-part"]//span[@class="price-tag-amount"]//span[2]')
            #//li[@class="ui-search-layout__item shops__layout-item"]//div[@class="ui-search-result__content-columns shops__content-columns"]//div[@class="ui-search-result__content-column ui-search-result__content-column--left"]//div[@class="ui-search-item__group ui-search-item__group--price shops__items-group"]//div[@class="ui-search-item__group__element ui-search-price__part-without-link shops-custom-secondary-font"]//div[@class="ui-search-price ui-search-price--size-medium shops__price"]//div[@class="ui-search-price__second-line"]//span[@class="price-tag ui-search-price__part shops-custom-secondary-font"]//span[@class="price-tag-amount"]/span[2]
            precios = [i.text for i in precios]
            lista_precios.extend(precios)
            
            ini = soup.find_all("span", attrs = {"class":"andes-pagination__link"})[0].text
            ini = int(ini)
            can = soup.find("li",attrs={"class":"andes-pagination__page-count"})
            can = int(can.text.split(" ")[1])

        else:
            print("ERROR RESPUESTA")
            break
        print(ini, can)
        if len(lista_titulos)>=int(limite):
            return lista_titulos[:limite], lista_url[:limite], lista_precios[:limite]
        if ini == can:
            break
        siguiente = dom.xpath('//div[@class="ui-search-pagination shops__pagination-content"]//ul[@class="ui-search-pagination andes-pagination shops__pagination"]//li[@class="andes-pagination__button andes-pagination__button--next shops__pagination-button"]//a')[0].get("href")
    
    return lista_titulos, lista_url, lista_precios
