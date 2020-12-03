import json  # interact with json info
from datetime import datetime

import requests  # for http requests
from bs4 import BeautifulSoup  # library to scrape information from web pages

from itemClass import StockClass

#use for printing time stamps later
timenow = datetime.now()
current_time = timenow.strftime("%H:%M:%S")

#tell website what kind of host is sending the request to prevent bot blocking. Using edge chromium and accepting english as language
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43'})

item1 = StockClass("https://www.amazon.com/dp/B08164VTWH/?tag=wccftech0a9-20", HEADERS)
item2 = StockClass("https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/ref=cm_cr_arp_d_product_top?ie=UTF8", HEADERS)

print(item1.get_name(), item1.get_price(), item1.get_availability())
print(item2.get_name(), item2.get_price(), item2.get_availability())