import numpy as np

def nonlin(x,deriv=False):
   if deriv==False:
      return(x*(1-x))
   return(1/(1+np.exp(-x)))

X= np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])

y=np.array([[0],[1],[1],[0]])

X=np.c_[np.ones(len(X)), X]

np.random.seed()


syn0=2*np.random.random((len(X[0]),len(X))) -1

syn1 = 2*np.random.random((len(X),len(X))) - 1

syn2 = 2*np.random.random((len(X),len(X))) - 1

syn3 = 2*np.random.random((len(X),1)) - 1


for j in range(80000):
    l0 = X 
    l1 = nonlin(np.dot(l0,syn0)) #first layer
    l2 = nonlin(np.dot(l1,syn1)) #second layer
    l3 = nonlin(np.dot(l2,syn2)) #third layer
    l4=  nonlin(np.dot(l2,syn2)) #fourth layer
    l4_error = y - l4 
    if (j% 10000) == 0: 
        print ("Error:" + str(np.mean(np.abs(l4_error))))

    l4_delta = l4_error*nonlin(l4,deriv=True)
    print(syn3)

    l3_error = l4_delta.dot(syn3.T)
    l3_delta = l3_error*nonlin(l3,deriv=True)
    
    l2_error = l3_delta.dot(syn2.T) 
    l2_delta = l2_error*nonlin(l2,deriv=True)
    
    l1_error = l2_delta.dot(syn1.T) 
    l1_delta = l1_error * nonlin(l1,deriv=True)
    
    syn0 += l0.T.dot(l1_delta)
    syn1 += l1.T.dot(l2_delta)  
    syn2 += l2.T.dot(l3_delta)
    syn3 += l2.T.dot(l4_delta)
    
    
print (l4)
