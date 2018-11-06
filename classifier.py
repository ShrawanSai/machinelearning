import numpy as np
import pandas as pd
from sklearn import preprocessing,cross_validation,neighbors,svm
from sklearn.neural_network import MLPClassifier


df=pd.read_csv('zoo.data.txt')
#print(df)
a=df.drop(['animal'],1,inplace=True)

y=np.array(df['type'])
X=np.array(df.drop(['type'],1))
#print(X)
#print(y)
   
acc=0
for i in range(25):

   #print(df)
   Xtrain,Xtest,ytrain,ytest=cross_validation.train_test_split(X,y,test_size=0.2)
   #print(ytest)
   clss=MLPClassifier()
   clss.fit(Xtrain,ytrain)

   accuracy=clss.score(Xtest,ytest)
   acc+=accuracy

print(acc/25)

example_measures = np.array([[1,0,0,1,0,0,0,1,1,1,0,0,4,2,0,0],[0,0,1,0,0,2,1,1,1,0,1,1,0,1,0,1],[0,1,1,0,1,1,1,0,1,1,0,0,2,1,0,0]])
example_measures = example_measures.reshape(len(example_measures), -1)
prediction = clss.predict(example_measures)
print(prediction)

