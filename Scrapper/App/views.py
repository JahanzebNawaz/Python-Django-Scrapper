from django.shortcuts import render
from django.http import HttpResponse
import requests, bs4
from bs4 import BeautifulSoup as bs
import re

# Create your views here.

def index(request):
        url = 'app/index.html'
        return render(request, url)



def scrape(request):
        url_temp = 'app/scrape.html'
        if request.method == 'POST':
                get_url = request.POST['url']
                get_req = requests.get(get_url)

                soup = bs(get_req.text, 'html.parser')
                print(soup.prettify())
                return render(request, url_temp)
        return render(request, url_temp)

    



# def scrape(request):
#     url_temp = 'instagram/scrape.html'
#     if request.method == "POST":
#         url = request.POST['url'] 
#         req = requests.get(url)

#         soup = bs(req.text, 'html.parser')
#         # soup = soup.prettify()
#         link = soup.findAll('meta')
#         print(link)
        
        # ancor = soup.findAll('div', {'class': 'RR-M-'})
        # print(ancor)
        
        
        
        # scrape through url


        # resp = requests.get(url)
        # soup = bs(resp.text, 'html.parser')
        # a = soup.findAll('img', {'class': 'FFVAD'})

        #  a = soup.findAll('div', {'class': 'item'})
        # c = soup.findAll('div', {'class': 'conversion-zone zone'})
        # t_data = []
        

       
        # for i in range(50):
        #     data = {}
        #     try:
        #         data['image'] = a[i].find('img')['src']
        #         # a[i].find('a', {'name': 'image'}).find('img')['data-regular-src']
        #     except:
        #         data['image'] = "http://placehold.it/200x150"
            
        #     t_data.append(data)
        # {'data': t_data}
    #     return render(request, url_temp )

        

    # # end of function
    # return render(request, url_temp)

