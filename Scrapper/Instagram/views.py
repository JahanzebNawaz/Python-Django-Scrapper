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
        """
        Method to get requested URL from input form and scrape data from instagram
        """
        url_temp = 'app/scrape.html'

        # file = open("insta.txt", "w")

        # if request.method == 'POST':

        #         # print('in loop')
        #         get_url = request.POST['url']
        #         print(get_url)
        #         # url_response = requests.get(get_url)
        #         # soup = bs(url_response.text, 'html5lib')
                
        #         # file.write(soup)
        #         # file.close()
                
        #         return render(request, url_temp, {'work': 'THIS WORKED'})
        context = 'notworking'
        return render(request, url_temp, context)

    



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

