import urllib
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
url = "http://www.greaterkashmir.com"

urls= [url]
visited = [url]
while len(urls) > 0:
    htmltext = requests.get(urls[0])
    urls.pop(0)
    plaintext = htmltext.text
    soup= BeautifulSoup(plaintext)
    for link in soup.findAll('a'):
        hr = link.get('href')
        hree = urllib.parse.urljoin(url, hr)
        hre = "http://www.greaterkashmir.com" + str(hr)
        title = link.string
        print(title)
        print(hree)
