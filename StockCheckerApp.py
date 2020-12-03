import json  # interact with json info
from datetime import datetime
import requests  # for http requests
from bs4 import BeautifulSoup  # library to scrape information from web pages
from itemClass import StockClass
from colorama import Fore, Style #for coloring text
import time #to space out requests



#use for printing time stamps later
timenow = datetime.now()
current_time = timenow.strftime("%H:%M:%S")

#instantiate itemClass object with url path as only parameter
item1 = StockClass("https://www.amazon.com/AMD-Ryzen-5600X-12-Thread-Processor/dp/B08166SLDF/ref=cm_cr_arp_d_product_top?ie=UTF8")
item2 = StockClass("https://www.amazon.com/AMD-Ryzen-5800X-16-Thread-Processor/dp/B0815XFSGK/ref=sr_1_15?dchild=1&keywords=5800x+amd&qid=1607031546&s=electronics&sr=1-15")
item3 = StockClass("https://www.amazon.com/dp/B08164VTWH/?tag=wccftech0a9-20")

#store itemClass objects in a list to iterate through later
itemList = {item1, item2, item3}

while True:
    for items in itemList:
        print(Fore.RED + "Item: " + Style.RESET_ALL + items.get_name())
        print(Fore.RED + "Price: " + Style.RESET_ALL + items.get_price())
        print(Fore.RED + "Availability: " + Style.RESET_ALL + items.get_availability())
        print(Fore.RED + "Time: " + Style.RESET_ALL + current_time)
        print("Checking next item \n")
        time.sleep(5) #wait between requests in order to not over request website

"""
print(Fore.RED + "Store: Amazon" + Style.RESET_ALL+ "\nItem: "  + item1.get_name())
print("Price: " + item1.get_price() + "\nAvailability: " + item1.get_availability() + "\nTime: " + current_time + "\n")
print("Store: Amazon\nItem: " + item2.get_name() + "\nPrice: " + item2.get_price() + "\nAvailability: " + item2.get_availability() + "\nTime: " + current_time + "\n")
print("Store: Amazon\nItem: " + item3.get_name() + "\nPrice: " + item3.get_price() + "\nAvailability: " + item3.get_availability() + "\nTime: " + current_time + "\n")
"""