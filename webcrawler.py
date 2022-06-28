
from urllib.request import urljoin
from bs4 import BeautifulSoup
import requests
from urllib.request import urlparse
from model import ProcessData
import time



input_url = "https://stackoverflow.com/questions/43797457/i-want-to-get-text-from-anchor-tag-using-selenium-python-i-want-print-text-hello"
depth = 2

crawler_log = open("Logs/crawler_log.txt","w")


def level_crawler(input_url):
    temp_urls = set()
    current_url_domain = urlparse(input_url).netloc

    
    beautiful_soup_object = BeautifulSoup(
        requests.get(input_url).content, "lxml")

    
    for anchor in beautiful_soup_object.findAll("a"):
        href = anchor.attrs.get("href")
        if(href != "" or href != None):
            href = urljoin(input_url, href)
            href_parsed = urlparse(href)
            href = href_parsed.scheme
            href += "://"
            href += href_parsed.netloc
            href += href_parsed.path
            final_parsed_href = urlparse(href)
            is_valid = bool(final_parsed_href.scheme) and bool(final_parsed_href.netloc)
            if is_valid:
                crawler_log.write(str(href)+") "+str(ProcessData(href))+"\n")
                temp_urls.add(href)
         
        
    return temp_urls    
                

if(depth == 0):
    print("Intern - {}".format(input_url))

elif(depth == 1):
    level_crawler(input_url)

else:
    queue = []
    queue.append(input_url)
    for j in range(depth):
        for count in range(len(queue)):
            url = queue.pop(0)
            urls = level_crawler(url)
            for i in urls:
                queue.append(i)
