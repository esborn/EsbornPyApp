import pandas as pd
import numpy as np
#get data
JData = pd.read_csv('JIRA.csv')  
JData.columns = JData.columns.str.replace('Custom field \(','')
JData.columns = JData.columns.str.replace('\)','')
JData.columns = JData.columns.str.replace('\/','')


colsToDrop = ['Issue Type','Summary','Issue id']
JData.rename(columns={'Issue key':'Issue_key'},inplace=True)
JData.drop(colsToDrop, axis =1,inplace=True)

JData['Status'] = JData['Status'].astype('category')
JData['Country'] = JData['Country'].astype('category')
JData['Region'] = JData['Region'].astype('category')
JData['Assignee'] = JData['Assignee'].astype('category')
JData['Components'] = JData['Components'].astype('category')


rcounts = JData.Issue_key.notnull().astype(float)
JData['IssuesCount'] = rcounts
pd.pivot_table(JData,'IssuesCount',['Country','Region'],aggfunc='mean')
#To save DataFrame to disk
#JData.to_pickle('JData.pkl')

#To import DataFrame
#DataFrameVariable =  pd.read_pickle('DataFrameFile.pkl')


JData.columns
JData.dtypes
JData.head()
