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
    for k in sp2.findAll('a', {'class': 'prc-name'}):
        webpage = requests.get("https://www.koton.com" + k.get('href'))
        sp = BeautifulSoup(webpage.content, "html.parser")

        #title
        title = sp.title.string
        title = title.strip()
        title = title.replace("| Koton", "")
        print(title)

        #id
        id = "https://www.koton.com" + k.get('href')

        #price(indirimsiz ürünlerin)
        """price = sp.find("span", "normalPrice").string
        print(price)"""

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
        print(product_category)

        #color
        color = sp.find("span", "title").string
        color = color.replace("Renk: ", "")
        color = color.strip()
        print(color)

        #size
        size_arr = []
        size = " "
        for i in sp.find_all('div', {'class': 'size clearfix'}):
            for j in i.findAll('li'):
                for k in j.findAll('a', href=True):
                    size_arr.append(k.text)
                size = ' -'.join(map(str, size_arr))
        print(size)

        #duplicate kontrolü
        product_count = Product.objects.filter(title=title).count()
        if product_count == 0:
            Product.objects.create(prod_id=id, title=title, image_uri=image_uri,productCategory = product_category)

