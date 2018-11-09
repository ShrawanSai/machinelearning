# import the necessary stuff
import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error,r2_score,accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing,cross_validation


path_training_data=os.getcwd()+'/YearPredictionMSD.txt'
data=pd.read_csv(('YearPredictionMSD.txt'),header=0,delimiter=",",quoting=3)
data.dropna(inplace=True)
#print(data)

#to reset indices
data.reset_index(drop=True,inplace=True)


y=np.array(data['2001'])
X=np.array(data.drop(['2001'],1))
#print(y)

Xtrain,Xtest,ytrain,ytest=cross_validation.train_test_split(X,y,test_size=0.2)

regr=linear_model.LinearRegression()

print(type(Xtrain))


regr.fit(Xtrain,ytrain)

# testing

ypredict= regr.predict(Xtest)

mse= mean_squared_error(ytest,ypredict)

print(mse)
