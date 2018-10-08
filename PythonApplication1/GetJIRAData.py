import pandas as pd
import os 
import shutil

shutil.move('C:\\Users\\E.Mugu\\Downloads\\Last Quarter 2017 To Feb 2018  (JIRA).csv','.\JIRA (2).csv')

JIRA1 = pd.read_csv('JIRA.csv')
JIRA2 = pd.read_csv('JIRA (2).csv')
JIRA_columns =['Issue Type', 'Issue key', 'Issue id', 'Summary', 'Status', 'Country',
       'Region', 'Components', 'Labels','Created','Assignee']

JIRA1.columns = JIRA1.columns.str.replace('Custom field \(','')
JIRA1.columns = JIRA1.columns.str.replace('\)','')
JIRA1.columns = JIRA1.columns.str.replace('\/','')
JIRA1=  JIRA1[JIRA_columns]

JIRA1.columns

JIRA1.shape



JIRA2.columns = JIRA2.columns.str.replace('Custom field \(','')
JIRA2.columns = JIRA2.columns.str.replace('\)','')
JIRA2.columns = JIRA2.columns.str.replace('\/','')
JIRA2=  JIRA2[JIRA_columns]
JIRA2.columns
JIRA2.shape

JIRA3 = pd.concat([JIRA1,JIRA2])
JIRA3.shape


JIRA3.duplicated().sum()
JIRA3.drop_duplicates(subset = JIRA_columns ,keep = 'first', inplace=True)
JIRA3.duplicated().sum()
JIRA3.to_csv('JIRA.csv')

shutil.copy('.\JIRA.csv', 'C:\\Users\\E.Mugu\\OneDrive - Save the Children International\\')
shutil.copy('.\JIRA.csv', 'C:\\Users\\E.Mugu\\SharePoint\\Global Applications Services - JIRA\\')
