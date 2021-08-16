
# bu dosya, webten verileri kazırken kullanılmak için deneme amaçlı kuruldu.

from bs4 import BeautifulSoup
import requests

#ürün isimleri ve linkleri
#from galaksiya_app.api.serializers import ProductSerializer
#from galaksiya_app.models import Product
from galaksiya_app.models import Product

webpage_base = requests.get('https://www.koton.com/tr/kadin/giyim/dis-giyim/kaban/c/M01-C02-N01-AK104-K100071')
sp2 = BeautifulSoup(webpage_base.content, "html.parser")
for k in sp2.findAll('a', {'class': 'prc-name'}):
    webpage= requests.get("https://www.koton.com" + k.get('href'))
    sp = BeautifulSoup(webpage.content, "html.parser")
    title = sp.title.string
    print(title)
    print("https://www.koton.com"+k.get('href'))
    id = "https://www.koton.com"+k.get('href')
    """price = sp.find("span", "normalPrice").string
    print(price)"""
    image_uri = []
    for i in sp.findAll('img'):
        if i.get('alt-src') != None:
            print(i.get('alt-src'))

"""webpage = requests.get('https://www.koton.com/tr/kadin-suni-kurk-detayli-kaban/p/1KAK06624EW001?productPosition=0&listName=Kad%C4%B1n%20Kaban%20Modelleri#tab-1')
sp = BeautifulSoup(webpage.content, "html.parser")

#print(sp.text)
#id,description, datePublished
title = sp.title.string
price= sp.find("span","normalPrice").string
product_detail_title = sp.findAll("p","alt-text")

#ürün detayının alınması
product_detail = []
for i in  sp.find_all('p',{'class': 'alt-text'}):
    product_detail.append(i.text)

#image uri alınması
image_uri=[]
for i in sp.findAll('img'):
    if i.get('alt-src')!= None:
        print(i.get('alt-src'))

#product category
product_category = []
for i in sp.find_all('div',{'class': 'col-xs-12 breadcrumb'}):
    for j in i.findAll('li'):
        for k in j.findAll('a',href = True):
            print(k.text)


#renk
color = sp.find("span","title").string

#size
for i in sp.find_all('div',{'class': 'size clearfix'}):
    for j in i.findAll('li'):
        for k in j.findAll('a',href = True):
            print(k.text)"""
