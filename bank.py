import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn import preprocessing,cross_validation
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier

path_training_data=os.getcwd()+'bank-additional-full.csv'

data=pd.read_csv(('bank-additional-full.csv'),header=0,delimiter=";",quoting=3)


data.dropna(inplace=True)
#to reset indices
data.reset_index(drop=True,inplace=True)
#print(data.info())
xx=data.columns
xx.tolist()



#MAPPING


#default
def mapping(dict1,list1,x):
   #print(x)
   list1=data[x].unique()
   #print(list1)
   dict1={}
   for i in range(len(list1)):
      

      dict1.update({list1[i]:i})

   data[x]=data[x].map(dict1)



listabc=[]
dictt={}


mapping(listabc,dictt,'"job"')
mapping(listabc,dictt,'"marital"')
mapping(listabc,dictt,'"education"')
mapping(listabc,dictt,'"default"')
mapping(listabc,dictt,'"housing"')
mapping(listabc,dictt,'"loan"')
mapping(listabc,dictt,'"contact"')
mapping(listabc,dictt,'"month"')
mapping(listabc,dictt,'"day_of_week"')
mapping(listabc,dictt,'"poutcome"')
mapping(listabc,dictt,'"y"')


#print(data.info())





#splitting


y=np.array(data['"y"'])
X=np.array(data.drop(['"y"'],1))
#print(y)

Xtrain,Xtest,ytrain,ytest=cross_validation.train_test_split(X,y,test_size=0.2)
#clss=svm.SVC()
#clss= KNeighborsClassifier(n_neighbors=3)
clss=MLPClassifier()
clss.fit(Xtrain,ytrain)

accuracy=clss.score(Xtest,ytest)

print(accuracy)





