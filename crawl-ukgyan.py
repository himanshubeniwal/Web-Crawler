import requests
from bs4 import BeautifulSoup
def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://www.ukgyan.com/"
        source_code = requests.get(url)
        plain_text = source_code.text   # just get the code, no headers or anything
        soup = BeautifulSoup(plain_text) # BeautifulSoup objects can be sorted through easy
        count=0
        for link in soup.findAll('a'):
            href = link.get('href')
            title = link.string  # just the text, not the HTML
            print(title)
            print(count,href)
            count=count+1
            get_single_item_data(href)
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    # if you want to gather information from that page
    #for item_name in soup.findAll('a'):
        #print(item_name.string)
    # if you want to gather links for a web crawler
    count=0
    for link in soup.findAll('a'):
        href = link.get('href')
        print(count,href)
        count=count+1
trade_spider(10)