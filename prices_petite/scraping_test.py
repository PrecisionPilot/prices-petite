from bs4 import BeautifulSoup
import requests

#the query is whatever the user wants to search for
query = "brooms"

#you have to do this for every computer
HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

#this is the shopping page implemted in Bing that shows specifically the query item from low to high price automatically
item_page_url = "https://www.bing.com/shop?q=" + query + "&FORM=SHOPTB&SortBy=Price&IsAscending=True"

#getting info from the shopping page
page = requests.get(item_page_url, headers=HEADERS)
soup = BeautifulSoup(page.content, "html.parser")

#list of prices for each corresponding product
price_list = soup.findAll("div", attrs={'class': 'pd-price br-standardPrice promoted'})
#list of the urls for each corresponding product 
url_list = soup.findAll("a", attrs={'class': 'br-offLink' })

#prints the urls 
for url in url_list:
    print(url.get('href'), end="\n\n")

#prints the prices
for price in price_list:
    print(price)

