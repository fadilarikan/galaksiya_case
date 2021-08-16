
from rest_framework.generics import ListAPIView

from galaksiya_app.api.serializers import ProductSerializer
from galaksiya_app.models import Product
from rest_framework import filters
from bs4 import BeautifulSoup
import requests

"""class ProductAddAPI():
    webpage_base = requests.get('https://www.koton.com/tr/kadin/giyim/dis-giyim/kaban/c/M01-C02-N01-AK104-K100071')
    sp2 = BeautifulSoup(webpage_base.content, "html.parser")
    for k in sp2.findAll('a', {'class': 'prc-name'}):
        webpage = requests.get("https://www.koton.com" + k.get('href'))
        sp = BeautifulSoup(webpage.content, "html.parser")
        title = sp.title.string
        Product.objects.create(title=title)
        print(title)
        id = "https://www.koton.com" + k.get('href')
        Product.objects.create(id=id)
        price = sp.find("span", "normalPrice").string
        print(price)
        image_uri = []
        for i in sp.findAll('img'):
            if i.get('alt-src') != None:
                Product.objects.create(image_uri=i.get('alt-src'))"""
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

