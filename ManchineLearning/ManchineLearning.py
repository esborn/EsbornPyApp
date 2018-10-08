
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Datafile= '.\Machine Learning A-Z\Part 1 - Data Preprocessing\Data_Preprocessing\Data.csv'

dataset= pd.read_csv(Datafile)
dataset.head()

#metrix of features

x= dataset.iloc[:,:-1].values

#depended variable
y = dataset.iloc[:,3].values

from  sklearn.preprocessing import Imputer 
imputer = Imputer(missing_values= 'NaN',strategy = 'mean', axis=0)
imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])
x
