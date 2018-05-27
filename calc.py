def add(x,y):
   return(x+y)
def sub(x,y):
   return(x-y)
def mul(x,y):
   return(x*y)
def div(x,y):
   return(x/y)
def sqr(x):
   return(x**2)
def sqrt(x):
   return(x**0.5)

def main():
      while True:
      
         menu='''
SELECT AN OPERATION
------------------
1.Add
2.Subtract
3.Multiply
4.Divide
5.Square
6.Square Root'''
         print(menu)
         

         try:
            ch=int(input("Enter a choice from 1-6 "))
            if ch==5 or ch==6:
               
               x=int(input('Enter number '))
               if ch==5:
                  
                  print(sqr(x))
               else:
                  print(sqrt(x))
            
            elif ch==1:
               print("Enter the 2 numbers ")
               x=int(input("Enter the number "))
               y=int(input("Enter the next number "))
               z=add(x,y)
               print(z)
            elif ch==2:
               print("Enter the 2 numbers ")
               x=int(input("Enter the number "))
               y=int(input("Enter the next number "))
               z=sub(x,y)
               print(z)
               
            
            elif ch==3:
               print("Enter the 2 numbers ")
               x=int(input("Enter the number "))
               y=int(input("Enter the next number "))
               z=mul(x,y)
               print(z)

            elif ch==4:
               print("Enter the 2 numbers ")
               x=int(input("Enter the number "))
               y=int(input("Enter the next number "))
               z=div(x,y)
               print(z)

            else:
               print('Invalid input')
         except TypeError:
               print("Please Enter valid input")
         except ValueError:
               print("Please integer only")
         except ZeroDivisionError:
               print("Division by 0 Error ")
      
                       
main()        


