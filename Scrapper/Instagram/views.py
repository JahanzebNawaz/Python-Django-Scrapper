from django.shortcuts import render
from django.http import HttpResponse
import requests, bs4
from bs4 import BeautifulSoup as bs
import re

# Create your views here.

def index(request):
    url = 'instagram/index.html'
    return render(request, url)


def scrape(request):
    url_temp = 'instagram/scrape.html'
    if request.method == "POST":
        url = request.POST['url']
        print(url)
        # scrape through url

        resp = requests.get(url)
        soup = bs(resp.text, 'html.parser')
        a = soup.findAll('img', {'class': 'FFVAD'})
        #  a = soup.findAll('div', {'class': 'item'})
        # c = soup.findAll('div', {'class': 'conversion-zone zone'})
        t_data = []

       
        for i in range(50):
            data = {}
            try:
                data['image'] = a[i].find('img')['src']
                # a[i].find('a', {'name': 'image'}).find('img')['data-regular-src']
            except:
                data['image'] = "http://placehold.it/200x150"
            
            t_data.append(data)

        return render(request, url_temp, {'data': t_data})

        

    # end of function
    return render(request, url_temp)

