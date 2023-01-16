from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader

from .models import ScrapedData

import requests 
from bs4 import BeautifulSoup as bs

# Create your views here.

def index(request):
    return HttpResponse("<h1> Welcome to Django </h1>")

def testpage(request):
    # return HttpResponse('<CENTER><H2> AN URL VIEW  TEST PAGE </H2></CENTER>')
    return render(request,'visualdb/inpform1.html')

# Function to Store Data in Database 
def store_scraped_data(scraped_prod_data):
    
    print(scraped_prod_data)

    obj_insert = ScrapedData()
    obj_insert.url_input        =  scraped_prod_data['prod_url']
    obj_insert.product_title    =  scraped_prod_data['product_name']
    obj_insert.product_price    =  scraped_prod_data['product_price']
    obj_insert.product_rating   =  scraped_prod_data['product_rating']
    obj_insert.product_image    =  scraped_prod_data['product_image']
    obj_insert.save()


# Function which uses Beautiful Soup to Scrape the following 
# Product Title Price Rating and Image 
def scrape_data_from_url(link):
    url_data = requests.get(link)
    soup = bs(url_data.text,features="html.parser")
    
    # print(soup.contents)
    product_name = soup.find('span',class_="B_NuCI")
    
    print("Product Name : " , product_name.text)

    # Category
    # _2whKao

    product_price = soup.find('div',class_="_30jeq3 _16Jk6d")
    print("Price : " , product_price.text)

    product_rating = soup.find('div',class_="_3LWZlK _3uSWvT")
    print("Rating : " , product_rating.text)
    
    # _2r_T1I _396QI4
    product_image = soup.find('img',class_="_2r_T1I _396QI4")
    print("Image: " , product_image['src'])

    
    scraped_prod_data={'prod_url':url_data.url,'product_name':product_name.text,'product_price':product_price.text,'product_rating':product_rating.text,'product_image':product_image['src']}
    # product_name = soup.find('div',class_="B_NuCI")
    # print("Product Name : " , product_name)

    
    store_scraped_data(scraped_prod_data)

    return scraped_prod_data


# Function to Display All Scraped Data From Database 
def disp_scraped_data(request):
    disp_data = ScrapedData.objects.all()
    return render (request,'visualdb/displayall.html',{'disp_data':disp_data})

def urlinput(request):
    if request.method=='GET':
        # template = loader.get_template('visualdb/inpform.html')

        return render(request,'visualdb/inpform.html')
        # return HttpResponse(template.render(request) ) 
    if request.method=='POST':
        url_data=request.POST['searchurl']
        print(url_data)

        scraped_data = scrape_data_from_url(url_data)        
        # Write the function for scraping the  web

        return render(request,'visualdb/inpform.html',{'scraped_data':scraped_data})
