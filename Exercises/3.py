#Simple Calculator In Python That ADDS SUBTRACT MULTIPLY AND DIVIDE 2 NUMBER

print("||--------------------------------------------||")
print("||--------------Basic Calculator--------------||")
print("||--------------------------------------------||")

a=int(input("Enter the First Number  :"))
b=int(input("Enter the Second Number :"))

print("Choose:")
print("1 for Addition,\n")
print("2 for Subtraction,\n")
print("3 for Multiplication,\n")
print("4 for Division,\n")

choice=int(input("Enter You Choice:"))

def addition():
    sum=a+b;
    print("The Sum of",a,"and",b,"is",sum)
    
def subtraction():
    sub=a-b;
    print("The Difference of",a,"and",b,"is",sub)    
        
def multi():
    mul=a*b;
    print("The Product of",a,"and",b,"is",mul)      

def divide():
    div=(a/b)
    print("The Division of",b,"from",b,"is",div) 


match choice:
    case 1:
        addition()
        
    case 2:
       subtraction() 
    
    case 3:
        multi()
        
    case 4:
                divide()
        
    
    case _:
        print("Invalid Choice") 
    
    