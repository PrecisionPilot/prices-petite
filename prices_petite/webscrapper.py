from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml

HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
BASE_URL = "https://www.bing.com/shop?q="
QUERY_PARAMETERS = "&FORM=SHOPTB&SortBy=Price&IsAscending=True"

def hyperlink_text(value):
    # target _blank to open new window
    return '<a target="_blank" href="{}">{}</a>'.format(value, value)



def search_web_prices(user_query):
    user_query = user_query.replace(" ", "+")
    item_page_url = BASE_URL + user_query + QUERY_PARAMETERS
    web_page = requests.get(item_page_url, headers=HEADERS)
    soup = BeautifulSoup(web_page.content, "lxml")
    item_list = soup.findAll("li", attrs={'class': 'br-item'})
    url_list = soup.findAll("a", attrs={'target': '_blank'})

    dictionary = {"Vendor": [], "Price": [], "Description": [], "Url": []}

    for i in range(len(item_list)):
        item = item_list[i]
        url = url_list[i]
        vendor = item.find("span", attrs={'class': 'br-sellersCite'})
        price = item.find("div", attrs={'class': 'pd-price br-standardPrice promoted'})
        description = item.find('div', attrs={'class','br-pdItemName'})
        url_link = url["href"]

        if (not vendor is None) and (not price is None) and (not description is None) and (not url_link is None) and len(url_link) > 60:
            dictionary["Vendor"].append(vendor.getText())
            dictionary["Price"].append(price.getText())
            dictionary["Description"].append(description.getText())
            dictionary["Url"].append(url_link)

    df = pd.DataFrame().from_dict(dictionary)
    df = df.dropna()

#    df.style.format({'Url': hyperlink_text})

    return df


