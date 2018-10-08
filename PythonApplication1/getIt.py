import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.ebay.com/'
req = requests.get(url)

soup = BeautifulSoup(req.text,'html.parser')


results= soup.find_all('div',attrs={'class':'sku -gallery'})
len(results)