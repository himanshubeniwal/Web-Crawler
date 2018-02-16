#Program for Web Crawler
#importing Modules to use :
import requests
from bs4 import BeautifulSoup
def trade_spider(max_pages):   #max pages for Different number of pages
    page = 1                    #intializing the page value to start from 1.
    while page <= max_pages:
        url = "http://www.ebay.in"   #Enter Link to be Crawl
        source_code = requests.get(url)   #Requesting the URl and Saving in Source_Code
        plain_text = source_code.text   # just get the code, no headers or anything
        soup = BeautifulSoup(plain_text) # BeautifulSoup objects can be sorted through easy
        letter=0
        for link in soup.findAll('a',{'class':'rt'}):  #Define Class to look on Webpage and Crawling should be on this class
            href = link.get('href')   #getting link
            title = link.string  # just the text, not the HTML
            print(letter,'- Main Title : ',title)
            letter=letter+1
            print('Link for Main Title to be Crawl : ',href)
            get_single_item_data(href)    #function to Crawl more Inner Level link
        page += 1
def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    # if you want to gather information from that page
    count=0
    for item_name in soup.findAll('a'):
        print(count," : text : ",item_name.string)
        count=count+1
    # if you want to gather links for a web crawler
    count=0
    for link in soup.findAll('a'):
        href =link.get('href')
        print(count," : Visiting Link: ",href)
        count=count+1

trade_spider(1)