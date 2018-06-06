import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


xs=np.array([1,2,3,4,5],dtype=np.float64)
ys=np.array([5,4,6,5,6],dtype=np.float64)


def best_fit_slope_and_intercept(xs,ys):
   m= (( mean(xs)*mean(ys) - mean(xs*ys) ) /
       ( (mean(xs)*mean(xs)) - mean(xs*xs)))
   b= mean(ys) - m*mean(xs)


   return m,b


def squared_error(y_line,y_orig):
   return sum((y_line-y_orig)*(y_line-y_orig))


def r_squared(y_line,y_orig):
   mean_y= [mean(y_orig) for y in y_orig]
   squared_error_regression_line=squared_error(y_orig,y_line)
   squared_error_mean_line=squared_error(mean_y,y_orig)
   r2=1-(squared_error_regression_line/squared_error_mean_line)
   return r2
   

m,b= best_fit_slope_and_intercept(xs,ys)

regression_line_ys=[(m*x+b) for x in xs]
r2=r_squared(regression_line_ys,ys)
print(r2)


#plotting
plt.plot(xs,regression_line_ys)
plt.scatter(xs,ys)
plt.show()



#print(regression_line_ys)
#print(m,b)


   
