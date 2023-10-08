from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml

#the query is whatever the user wants to search for
query = "broom sticks".replace(" ", "+")

#you have to do this for every computer
HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

#this is the shopping page implemted in Bing that shows specifically the query item from low to high price automatically
item_page_url = "https://www.bing.com/shop?q=" + query + "&FORM=SHOPTB&SortBy=Price&IsAscending=True"

#getting info from the shopping page
page = requests.get(item_page_url, headers=HEADERS)
soup = BeautifulSoup(page.content, "lxml")

#creates a list, tracking all items
item_list = soup.findAll("li", attrs={'class': 'br-item'})

dict = {"url_list":["asd"], "price_list":["asdf"], "product_name_list":["asdf"]}

for item in item_list:

        dict["url_list"].append(item.find("span", attrs={'class': 'br-sellersCite'}).getText())
        dict["price_list"].append(item.find("div", attrs={'class': 'pd-price br-standardPrice promoted'}))
        dict["product_name_list"].append(item.find('div', attrs={'class','br-pdItemName'}).getText())

print(dict)

df = pd.DataFrame(dict)

print(df)



