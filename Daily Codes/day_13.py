#SET __ It doesnot take the duplicate Value i.e you cant add the duplicate value

a={1,2,3,1}
print(a)

b={"Himanshu",16, True}
print(b)

for value in a:
    print(value)
    
    
#UNION IN SET 

s1={1,2,3,4}
s2={3,5,6,7}

#UNION
print(s1.union(s2))


#UPDATE
s1.update(s2)
print(s1)
    
    
#INTERSECTION

s1.intersection_update(s2)


#SYMMETRIC DIFFERENCE ---> Except the Intersection all values Goes Here
a1={"Nepal", "India", "China","Pakistan"}
a2={"China","USA","India",}

a3=a1.symmetric_difference(a2)
print(a3)


#Difference  ------> t1-t2 as operation We do in The Set IRL

t1={1,2,3,4,5,6,7,8,9,}
t2={3,4,6,7}

t=t1.difference(t2)
print(t)

 # There Are Other Method Like Disjoint and SuperSet Here is the Example Of Moreee 
 
 
q1={1,2,3,4,5,6}
q2={99,88,77,66,666}

print(q1.isdisjoint(q2)) #-------> True Because  the Set IS Disjoint


#.remove Only Removes One Specific item

#set.remove(Item to remove)



#Clear Removes All The Elements

