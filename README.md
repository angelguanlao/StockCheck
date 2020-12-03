# StockCheck
Python Console Application to check whether item is in stock
Currently only works on Amazon products

#Getting Started
**Prerequisits**
Download BeautifulSoup4 in Python if you already don't have it
Install using pip
```
py -m pip install bs4
```

**Installation**
Clone the repository
```
git clone https://github.com/angelguanlao/StockCheck
```

#Usage
The application has the main StockCheckerApp which you instantiate an item you want to monitor using the StockClass from itemClass.

Example
```
#item_name = StockClass('Pass URL in quotes here')
shoe_example = StockClass('www.shoeshopshop.com/shop/cool-shoes-3')
```
There is a itemList list which you put your instantiated StockClass objects into so the program can loop through those items
```
itemList = [shoe_example, shoe_two, show_three]
```
The rest of the program will call functions to grab the item name, price, and availability with time stamps and will run continuously until closed.
