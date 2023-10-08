from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml

HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
BASE_URL = "https://www.bing.com/shop?q="
QUERY_PARAMETERS = "&FORM=SHOPTB&SortBy=Price&IsAscending=True"
def search_web_prices(user_query):
    user_query = user_query.replace(" ", "+")
    item_page_url = BASE_URL + user_query + QUERY_PARAMETERS
    web_page = requests.get(item_page_url, headers=HEADERS)
    soup = BeautifulSoup(web_page.content, "lxml")
    item_list = soup.findAll("li", attrs={'class': 'br-item'})

    dictionary = {"Vendor": [], "Price": [], "Description": []}

    for item in item_list:
        vendor = item.find("span", attrs={'class': 'br-sellersCite'})
        price = item.find("div", attrs={'class': 'pd-price br-standardPrice promoted'})
        description = item.find('div', attrs={'class','br-pdItemName'})

        if (not vendor is None) and (not price is None) and (not description is None):
            dictionary["Vendor"].append(vendor.getText())
            dictionary["Price"].append(price.getText())
            dictionary["Description"].append(description.getText())

#        dictionary["url_list"].append()
#        dictionary["price_list"].append(str(item.find("div", attrs={'class': 'pd-price br-standardPrice promoted'}).getText()))
#        dictionary["product_name_list"].append(str(item.find('div', attrs={'class','br-pdItemName'}).getText()))

    df = pd.DataFrame().from_dict(dictionary)
    df = df.dropna()
    df = df.astype({"Vendor": "string"})
    df = df.astype({"Price": "string"})
    df = df.astype({"Description": "string"})
    return df


new_dataframe = search_web_prices("broom stick")
print(new_dataframe)
print(new_dataframe.dtypes)
