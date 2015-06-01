import random
import urllib.request
def download_image(url):
    name = random.randrange(1, 1000)
    fullname = str(name)+".jpg"
    urllib.request.urlretrieve(url, fullname)

download_image("http://www.thinkstockphotos.com/CMS/StaticContent/Hero/TS_AnonHP_462882495_01.jpg")
