from datetime import datetime

name = input("Enter your name: ")

hour = datetime.now().hour

if 5 <= hour < 12:
    greeting = "Good Morning"
elif 12 <= hour < 17:
    greeting = "Good Afternoon"
elif 17 <= hour < 21:
    greeting = "Good Evening"
else:
    greeting = "Good Night"

print(f"{greeting}, {name}! Have a great day! 😊")