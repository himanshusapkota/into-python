#Tuples and Tuples are immutable that is the data cant be changed

a=(1,) # If I will not give comma after 1 then the type will be printed as int
print(a)
print(type(a))

country=("Nepal" , "USA" , "Norway" , "India" )

if "Nepal" in country:
    print("Nepal Is Present")


    #OPERATION ON TUPLES

# IF we want to change some items in tuple we have to convert it into the list and later after changing something in that list we can change the list into the tuple again. Here is the Polished Example:

num=(1,2,3,4,5,6,7,8)    
temp=list(num)
temp.append(9)
num=tuple(temp)
print(num)


#concatination of tuples

name1=("Ram","Hari")
name2=("Sita","Geeta" ,"Sita" , "Geeta")

name=name1+name2
print(name)


#The count method is used to count occurance of any data
print(name.count("Sita"))

