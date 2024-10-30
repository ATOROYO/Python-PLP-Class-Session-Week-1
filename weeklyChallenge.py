# Personalized greeting app
user_name = "David Atoroyo Sika"
favorite_color = "Black"
print(f"Hello {user_name}! Your favorite color, {favorite_color}, is awesome")

# Simple Quiz game
def display_score(score, total_questions):
    print(f"\nYour final score is {score}/{total_questions}!")
    if score == total_questions:
        print("Perfect score! You're a quiz master! 🎉")
    elif score >= total_questions // 2:
        print("Nice job! You did well! 👍")
    else:
        print("Keep trying! Practice makes perfect! 😅")

def play_quiz():
    questions = [
        {
            "question": "What is the keyword used to define a function in Python?",
            "options": ["A. func", "B. def", "C. function", "D. define"],
            "answer": "B"
        },
        {
            "question": "Who played the Joker in 'The Dark Knight'?",
            "options": ["A. Jack Nicholson", "B. Heath Ledger", "C. Jared Leto", "D. Joaquin Phoenix"],
            "answer": "B"
        },
        {
            "question": "What does the acronym OOP stand for?",
            "options": ["A. Object-Oriented Programming", "B. Outer Object Programming", "C. Only One Program", "D. Object-Oriented Python"],
            "answer": "A"
        },
        {
            "question": "In which year was the movie 'Inception' released?",
            "options": ["A. 2008", "B. 2010", "C. 2012", "D. 2014"],
            "answer": "B"
        },
        {
            "question": "What is the output of print(2 ** 3) in Python?",
            "options": ["A. 5", "B. 6", "C. 8", "D. 9"],
            "answer": "C"
        }
    ]

    score = 0
    total_questions = len(questions)

    for idx, question in enumerate(questions):
        print(f"\nQuestion {idx + 1}: {question['question']}")
        for option in question["options"]:
            print(option)

        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        if answer == question["answer"]:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong. The correct answer was {question['answer']}.")

    display_score(score, total_questions)

# Main game loop
while True:
    play_quiz()
    replay = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if replay != "yes":
        print("Thanks for playing! Goodbye!")
        break
