# -----------------------------------------------------------------------------
# Created:     08.07.2018
# Copyright:   (c) Esborn m 2018
# Licence:     AGPLv3
#
# Sample script for parsing HTML tables
# -----------------------------------------------------------------------------

import urllib.request
import pandas as pd
from pprint import pprint
from html_table_parser import HTMLTableParser


def url_get_contents(url):
    """ Opens a website and read its binary contents (HTTP Response Body) """
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()


def main():
    url = 'http://www.rich.co.ke/rcdata/nsestocks.php'
    xhtml = url_get_contents(url).decode('utf-8')

    p = HTMLTableParser()
    p.feed(xhtml)
    #pprint(p.tables[14])
    df = pd.DataFrame(p.tables[14])
    df.to_csv('stocks.csv',index=False,encoding='utf-8')
   
    
if __name__ == '__main__':
    main()



