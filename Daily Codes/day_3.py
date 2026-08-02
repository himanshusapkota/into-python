#String Slicing
name="Himanshu"
print(name[0:5])

#How to find the length of the String? 

# We can find it by using the length function
 
 #Example Code
 
     
a="Himanshu"
print(len(a))

fruit="apple"
len1=len(fruit)

print("Apple is" , len1 , "letter word.")



a="GOOONING"
print(a[1:4])




#STRING METHODS



g="hackclub"
gff=g.upper()
print(gff.lower())


#rstrip : It is Used to remove any desired character from the string

#Example Code:

vv="Himanshu!!!!!!!!!!!!!!!!!!!!!!!!!"
print(vv.rstrip("!"))

#OUTPUT : Himanshu

#rstrip doesnot remove the leading character for example in !!Himanshu It doesnot Remove !! which is a head


#REPLACE: IT IS USED TO REPLACE ANY CHARACTERS 

#EXAMPLE CODE:

abc="Ram is a good boy"
print(abc.replace("good" , "bad"))

#In a single Word

add="Love"
print(add.replace("ve" , "fi"))


dev="Ram is the developer of Linux."
print(dev.replace("Ram" , "Linnus"))

#Split: Split is the function used to split the String W.R.T anything
hj="Ram Hari Sita Gita"
print(hj.split(" "))



# Capitalize: It is used to make capital to the first letter of an string but the rest of other String will be in lowercase Even if All the character are in Uppercase

wq="HIMANSHU"
print(wq.capitalize())

#Another Example
blogHead="welcome to blogheram.com"
print(blogHead.capitalize())

#It only makes the W capital Not Other  Character

