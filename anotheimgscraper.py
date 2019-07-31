import bs4 as bs
import requests
import urllib.request


class SoftwaretestingImages:
    def make_soup(url):
        thepage = urllib.request.urlopen(url)
        soupdata = bs.BeautifulSoup(thepage, "html.parser")
        return soupdata
        soup = make_soup('https://www.guru99.com/automated-testing-tools.html')
        for img in soup.findAll('img'):
            print(img.get('src'))