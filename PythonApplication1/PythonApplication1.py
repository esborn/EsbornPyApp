import requests 
import urllib.request
import pandas as pd 

reqs = requests.get('http://www.rich.co.ke/rcdata/nsestocks.php')
#reqs.text[:1000]
from bs4 import BeautifulSoup
soup = BeautifulSoup(reqs.text,'html.parser')

table = soup.find_all('table',attrs={'bgcolor':'#ffffff'})
newtable =  table
for results in newtable:
    print(results.text)
