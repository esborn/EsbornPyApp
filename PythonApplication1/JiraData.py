
import pandas as pd

#new columns
# to replace all spaces 
# 

JiraCols = ['IssueType', 'Issuekey', 'Issueid', 'Summary', 'Status',
       'Country', 'Region', 'Components',
       'Component1', 'Component2', 'Component3', 'Component4',
       'Labels', 'Labels.1', 'Created', 'Assignee']
dropCols = ['Component1', 'Component2', 'Component3', 'Component4','Labels.1']
#import data 

stocksdata = pd.read_csv('C:\\Users\\E.Mugu\\Downloads\\JIRA.csv', names=JiraCols , header=0)


stocksdata.drop( ['Component1', 'Component2', 'Component3', 'Component4','Labels','Labels.1'],axis=1,inplace=True)
#stocksdata.columns


stocksdata.to_csv('JIRA.csv')

