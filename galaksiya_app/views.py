
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

#ürün isimleri ve linkleri
#from galaksiya_app.api.serializers import ProductSerializer
#from galaksiya_app.models import Product
from galaksiya_app.models import Product
def index(request):
    webpage_base = requests.get('https://www.koton.com/tr/kadin/giyim/dis-giyim/kaban/c/M01-C02-N01-AK104-K100071')
    sp2 = BeautifulSoup(webpage_base.content, "html.parser")
    webpage2 = " "
    for k in sp2.findAll('a', {'class': 'prc-name'}):
        webpage = requests.get("https://www.koton.com" + k.get('href'))
        webpage2=webpage
        sp = BeautifulSoup(webpage.content, "html.parser")

        #title
        title = sp.title.string
        title = title.strip()
        title = title.replace("| Koton", "")
        print(title)

        #id
        id = "https://www.koton.com" + k.get('href')

        #price
        price = []
        discount = False
        if sp.find('span','normalPrice') != None:
            normalPrice = sp.find('span','normalPrice').string
            normalPrice = normalPrice.strip()
            price.append(normalPrice)
        else:
            normalPrice = sp.find("s").string
            normalPrice = normalPrice.strip()
            price.append(normalPrice)

            newPrice = sp.find("span", "newPrice").string
            newPrice = newPrice.strip()
            price.append(newPrice)
            discount = True

        #image uri
        image_uri = []
        for i in sp.findAll('img'):
            if i.get('alt-src') != None:
                image_uri.append(i.get('alt-src'))

        #product category
        product_cat = []
        product_category = " "
        i=sp.find('div', {'class': 'col-xs-12 breadcrumb'})
        for j in i.findAll('li'):
            for k in j.findAll('a', href=True):
                if k.text == "Anasayfa":
                    continue
                else:
                    product_cat.append(k.text)
                product_category = '-'.join(map(str, product_cat))

        #color
        color = sp.find("span", "title").string
        color = color.replace("Renk: ", "")
        color = color.strip()

        #size
        size_arr = []
        size = " "
        for i in sp.find_all('div', {'class': 'size clearfix'}):
            for j in i.findAll('li'):
                for k in j.findAll('a', href=True):
                    size_arr.append(k.text)
                size = ' - '.join(map(str, size_arr))

        #stok durumu

        inStock = True
        if sp.find('div','outOfStock') != None:
            inStock= False
        # duplicate kontrolü
        product_count = Product.objects.filter(title=title).count()
        if product_count == 0:
            Product.objects.create(prod_id=id, title=title, image_uri=image_uri, productCategory=product_category,color =color,
                               size=size, price=price, discount=discount,inStock=inStock)

        for k in sp.findAll('a', {'class': 'colorVariant'}):
            webpage = requests.get("https://www.koton.com" + k.get('href'))
            if webpage2==webpage:
                break
            sp = BeautifulSoup(webpage.content, "html.parser")

            # title
            title = sp.title.string
            title = title.strip()
            title = title.replace("| Koton", "")
            print(title)

            # id
            id = "https://www.koton.com" + k.get('href')

            # price
            price = []
            discount = False
            if sp.find('span', 'normalPrice') != None:
                normalPrice = sp.find('span', 'normalPrice').string
                normalPrice = normalPrice.strip()
                price.append(normalPrice)
            else:
                normalPrice = sp.find("s").string
                normalPrice = normalPrice.strip()
                price.append(normalPrice)

                newPrice = sp.find("span", "newPrice").string
                newPrice = newPrice.strip()
                price.append(newPrice)
                discount = True

            # image uri
            image_uri = []
            for i in sp.findAll('img'):
                if i.get('alt-src') != None:
                    image_uri.append(i.get('alt-src'))

            # product category
            product_cat = []
            product_category = " "
            i = sp.find('div', {'class': 'col-xs-12 breadcrumb'})
            for j in i.findAll('li'):
                for k in j.findAll('a', href=True):
                    if k.text == "Anasayfa":
                        continue
                    else:
                        product_cat.append(k.text)
                    product_category = '-'.join(map(str, product_cat))

            # color
            color = sp.find("span", "title").string
            color = color.replace("Renk: ", "")
            color = color.strip()

            # size
            size_arr = []
            size = " "
            for i in sp.find_all('div', {'class': 'size clearfix'}):
                for j in i.findAll('li'):
                    for k in j.findAll('a', href=True):
                        size_arr.append(k.text)
                    size = ' - '.join(map(str, size_arr))

            # stok durumu
            inStock = True
            if sp.find('div', 'outOfStock') != None:
                inStock = False
        # duplicate kontrolü
            product_count = Product.objects.filter(title=title).count()
            if product_count == 0:
                Product.objects.create(prod_id=id, title=title, image_uri=image_uri, productCategory=product_category,color =color,
                                size=size, price=price, discount=discount,inStock=inStock)

#sonunda return değeri olmadığı için burasının çalışması bittiğinde kod hata veriyor. Herhangi bir değer kaybı yok.
