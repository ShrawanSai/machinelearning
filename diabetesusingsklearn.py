# import the necessary stuff

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets
from sklearn.metrics import mean_squared_error,r2_score,accuracy_score

# load database
diabetes= datasets.load_diabetes()

#print(diabetes)

# creating splits for test and train
diabetes_x=diabetes.data[:,np.newaxis,2]
#print(diabetes_x)

diabetes_x_train=diabetes_x[:-20]
diabetes_x_test=diabetes_x[-20:]

#print( diabetes_x_test)

diabetes_y_train=diabetes.target[:-20]
diabetes_y_test=diabetes.target[-20:]

#print(diabetes_y_test)

#create model

regr=linear_model.LinearRegression()

#train

regr.fit(diabetes_x_train,diabetes_y_train)

# testing

diabetes_y_predict= regr.predict(diabetes_x_test)

#calculate errors

mse= mean_squared_error(diabetes_y_test,diabetes_y_predict)

print(mse)

#plotting on graphs
plt.scatter(diabetes_x_test,diabetes_y_test,color='black')
plt.plot(diabetes_x_test,diabetes_y_predict,color='blue',linewidth='3')

plt.xticks(())
plt.yticks(())
plt.show()
