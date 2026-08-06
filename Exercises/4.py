questions = [
    "Who is the President of the United States?",
    "Which is the largest country on Earth?",
    "Who won the FIFA World Cup 2022?"
]

options = [
    [
        "1. Donald Trump",
        "2. Joe Biden",
        "3. Kamala Harris",
        "4. None of the above"
    ],
    [
        "1. India",
        "2. France",
        "3. Nepal",
        "4. Russia"
    ],
    [
        "1. Spain",
        "2. Argentina",
        "3. USA",
        "4. Mexico"
    ]
]

answers = [1, 4, 2]

score = 0

print("=" * 40)
print("        WELCOME TO THE QUIZ")
print("=" * 40)

for i in range(len(questions)):
    print(f"\nQuestion {i + 1}:")
    print(questions[i])

    for option in options[i]:
        print(option)

    while True:
        try:
            user_answer = int(input("Enter the answer: "))

            if 1 <= user_answer <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input! Enter a number.")

    if user_answer == answers[i]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
        print("Correct Answer:", options[i][answers[i] - 1])

print("\nQuiz Finished!")
print(f"Your Score: {score}/{len(questions)}")