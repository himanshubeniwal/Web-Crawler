import requests
from bs4 import BeautifulSoup
def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://www.ebay.in/sch/Laptops/16159/i.html?_from=R40&_nkw=&LH_BIN=1&LH_ItemCondition=3&_pgn=" + str(page) + "&_skc=50&rt=nc"
        source_code = requests.get(url)
        plain_text = source_code.text   # just get the code, no headers or anything
        soup = BeautifulSoup(plain_text) # BeautifulSoup objects can be sorted through easy
        for link in soup.findAll('a', {'class': 'vip'}):
            href = link.get('href')
            title = link.string  # just the text, not the HTML
            print(title)
            print(href)
            #get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    # if you want to gather information from that page
    for item_name in soup.findAll('span', {'class': 'notranslate'}):
        print(item_name.string)
    # if you want to gather links for a web crawler
    for link in soup.findAll('a'):
        href = "http://www.ebay.in/" + link.get('href')
        print(href)
trade_spider(1)