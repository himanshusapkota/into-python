#Number Guessing Game 
#The Number will called Using The random Function and You Have to Guess The Number.
#The Number will between 1 to 100 You Guess it


import random

answer=random.randint(1,100)

print("||---------------------------------||")
print("||-----Number Guessing Game--------||")
print("||---------------------------------||")

print("Enter The Number Between 1 to 100")

while True:
    guess=int(input("Enter Your Guess : "))
    
    if guess<answer:
        print("Too Low Dwag")
        
    elif guess>answer:
        print("To High Dwag")    

    else:
        print("Congrats Dwag You Guessed it Right")
        break


