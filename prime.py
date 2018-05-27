def prime(n):
   z=3
   for i in range(2,n//2+1):
      if n%i==0:
         z=0
         break
   else:
      z=1
   return z


def main():
   while True:
      try:
         
         n=int(input("Enter no.: "))
         if n!=1:
            
            x=prime(n)
            if x==1:
               print('Prime')
            elif x==0:
               print('Not Prime')
         else:
            print('Neither Prime nor Composite')
      except ValueError:
         print('Invalid input')
main()
      
