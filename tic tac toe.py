def leftdiagnol(A):
   if A[0][0]==A[1][1]==A[2][2]:
      if A[0][0]==1 or A[0][0]==2:
         return(A[0][0])
   else:
      return(-1)
def rightdiagnol(A):
   if A[2][0]==A[1][1]==A[0][2]:
      if A[0][2]==1 or A[0][2]==2:
         return(A[0][2])
   else:
      return(-1)
def rowchk(A):
   for row1 in range(3):
      if A[row1][0]==A[row1][1]==A[row1][2]:
         if A[row1][2]==1 or A[row1][2]==2:
            print(A[row1][2])
            return A[row1][2]
      else:
         return(-1)
def colchk(A):
   for col in range(3):
      if A[0][col]==A[1][col]==A[2][col]:
         if A[2][col]==1 or A[2][col]==2:
            return A[2][col]
      return(-1)
def valid(t):
   c1,c2=0,0
   for i in t:
      if i==1:
         c1+=1
      elif i==2:
         c2+=1
   if c1>1:
      return c1
   elif c2>1:
      return c2
def main():
   A=[[0 for row in range(3)]for col in range(3)]
   for row in range(3):
      for col in range(3):

         while True:
            try:
               x=int(input())
               if x==1 or x==2 or x==0:
                  A[row][col]=x
                  break
               else:
                  print('invalid input')
            except:
               print('Invalid input')
   l1=leftdiagnol(A)
   #print(l)
   r=rightdiagnol(A)
   #print(l,r)
   k=rowchk(A)
   l=colchk(A)
   t=[l1,r,k,l]
   #print(t)
   p=max(t)
   for row in range(3):
      for col in range(3):
         print (A[row][col],end=' ')
      print()   
   if 1 in t and 2 in t:
      print('Game not possible')

   elif valid(t)>1:
      print('Game not possible')
         
      
   else:
      if p==2:
         print('Player 2 wins')
      elif p==1:
         print('Player 1 wins')
      else:
         print('Draw')
      

         
   #print(A)
   
main()
