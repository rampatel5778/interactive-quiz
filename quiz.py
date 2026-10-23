
questions = [
    {
        "question": "1. What is the data type of 10?",
        "answer": "int"
    },
    {
        "question": "2. Which keyword defines a function?",
        "answer": "def"
    },
    {
        "question": "3. Which loop can iterate over a list?",
        "answer": "for"
    },
    {
        "question": "4. Which brackets are used for a Python list?",
        "answer": "square brackets"
    },
    {
        "question": "5. Which keyword sends a result back from a function?",
        "answer": "return"
    }
]

while True:
    score = 0
    correct = 0
    incorrect = 0

    print("\n==============================")
    print("      PYTHON KNOWLEDGE QUIZ")
    print("==============================")

    for item in questions:
        print("\n" + item["question"])
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == item["answer"]:
            print("Correct!")
            score += 1
            correct += 1
        else:
            print("Incorrect!")
            print("Correct answer:", item["answer"])
            incorrect += 1

    total = len(questions)
    percentage = (score / total) * 100

    print("\n==============================")
    print("        QUIZ COMPLETED")
    print("==============================")
    print("Score:", score, "out of", total)
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)
    print("Percentage:", str(int(percentage)) + "%")

    with open("quiz_results.txt", "a") as file:
        file.write(
            "Score: " + str(score) + "/" + str(total)
            + " | Percentage: " + str(int(percentage))
            + "%\n"
        )

    print("Result saved successfully!")

    play_again = input(
        "\nWould you like to play again? (yes/no): "
    ).strip().lower()

    if play_again != "yes":
        print("Thank you for playing!")
        break
