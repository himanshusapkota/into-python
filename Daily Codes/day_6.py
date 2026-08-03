#Function

def avg(a,b):
    ave=(a+b)/2
    print("The Average is " , ave)
    
avg(1,6)    



def sum(*numbers):
    sum1=0
    for i in numbers:
        sum1=sum1+i
    print("Sum is:", sum1)
        
sum(1,3,4,5,6,7,7,)        

