
import pandas as pd

stocksdata = pd.read_csv('stocks.csv')
cols={'1':'stocks','2':'PREV','3':'NOW','4':'%','6':'VOL'}
stocksdata.rename(columns = cols,inplace=True)
stocks= stocksdata.drop(stocksdata.index[0:3])
stocks = stocks.drop('0',axis=1)
stocks = stocks.drop('5',axis=1)
stocks = stocks.drop('7',axis=1)
stocks.to_csv('stocks3.csv')
stocks.head()
