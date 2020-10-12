import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt

data=pd.read_csv('Salary_Data.csv')  
X=data.iloc[:,:-1].values  
y=data.iloc[:,1].values  

#split dataset in train and testing set   
from sklearn.cross_validation import train_test_split  
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=10,random_state=0)  

from sklearn.linear_model import LinearRegression  
regressor=LinearRegression()  
regressor.fit(X_train,Y_train)  
y_pre=regressor.predict(X_test)  
