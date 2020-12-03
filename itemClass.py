from bs4 import BeautifulSoup #library to scrape information from web pages
import requests #for http requests
import json #interact with json info
from datetime import datetime

class StockClass:
    def __init__(self, url, Headers):
        self.url = url
        self.Headers = Headers

        #send request to our URL
        webpage = requests.get(self.url, headers=self.Headers)

        #pass on the information from request to parse with BS4
        #lmxl is a parser from BS4 that breaksdown the content of webpage
        self.soup = BeautifulSoup(webpage.content, 'lxml')

    def get_name(self):
        #send request to our URL
        webpage = requests.get(self.url, headers=self.Headers)
        #pass on the information from request to parse with BS4
        #lmxl is a parser from BS4 that breaksdown the content of webpage
        new_soup = BeautifulSoup(webpage.content, 'lxml')
        #find item name from page. Product title wrapped in productTitle tags on webpage
        title = new_soup.find('span', attrs={'id' : 'productTitle'})
        #extract name as string
        title_value = title.string
        #clean up string of extra spaces
        title_string = title_value.strip()
        #function to check availability. Parameter is soup object defined above
        return title_string

    def get_availability(self):
        try:
            available = self.soup.find('div', attrs = {'id':'availability'})
            available = available.find('span').string.strip()
        except AttributeError:
            available = "Out of stock"
        return available

    #function to get price
    def get_price(self):
        try:
            price = self.soup.find('div', attrs = {'id':'price'})
            price = price.find('span').string.strip()
        except AttributeError:
            price = "Unavailable"
        return price
