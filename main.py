"""A beginner-friendly command-line quiz about Python and developer tools."""


QUESTIONS = [
    {
        "category": "Python",
        "question": "Which keyword is used to define a function in Python?",
        "options": {"A": "func", "B": "def", "C": "function", "D": "make"},
        "answer": "B",
        "explanation": "Python functions are declared with the def keyword.",
    },
    {
        "category": "Python",
        "question": "Which data type stores True or False?",
        "options": {"A": "str", "B": "list", "C": "bool", "D": "dict"},
        "answer": "C",
        "explanation": "bool is Python's Boolean type.",
    },
    {
        "category": "Python",
        "question": "What does len(['a', 'b', 'c']) return?",
        "options": {"A": "2", "B": "3", "C": "4", "D": "It causes an error"},
        "answer": "B",
        "explanation": "The list contains three items, so len returns 3.",
    },
    {
        "category": "Git",
        "question": "Which Git command records staged changes in a commit?",
        "options": {
            "A": "git save",
            "B": "git push",
            "C": "git commit",
            "D": "git record",
        },
        "answer": "C",
        "explanation": "git commit creates a commit from staged changes.",
    },
    {
        "category": "Git",
        "question": "Which command shows the current working tree status?",
        "options": {
            "A": "git status",
            "B": "git start",
            "C": "git check",
            "D": "git branch",
        },
        "answer": "A",
        "explanation": "git status reports changed, staged, and untracked files.",
    },
    {
        "category": "Web",
        "question": "What does HTTP 404 usually mean?",
        "options": {
            "A": "Request succeeded",
            "B": "Page not found",
            "C": "Server is starting",
            "D": "Access is allowed",
        },
        "answer": "B",
        "explanation": "A 404 status means the requested resource was not found.",
    },
    {
        "category": "Web",
        "question": "Which format is commonly used to exchange structured web data?",
        "options": {"A": "JSON", "B": "MP3", "C": "PNG", "D": "ZIP"},
        "answer": "A",
        "explanation": "JSON is a common text format for structured data.",
    },
    {
        "category": "Python",
        "question": "Which symbol starts a single-line comment in Python?",
        "options": {"A": "//", "B": "<!--", "C": "#", "D": "--"},
        "answer": "C",
        "explanation": "A hash symbol (#) starts a Python single-line comment.",
    },
]


def ask_name():
    """Keep asking until the player enters a name containing non-space text."""
    while True:
        player_name = input("Enter your name: ").strip()
        if player_name:
            return player_name
        print("Please enter at least one character.")


def ask_answer(options):
    """Return a valid answer choice, accepting either lowercase or uppercase."""
    valid_choices = options.keys()
    while True:
        answer = input("Your answer (A-D): ").strip().upper()
        if answer in valid_choices:
            return answer
        print("Please enter one of the listed letters.")


def show_results(player_name, score, category_scores):
    """Display the final score, a short message, and category breakdown."""
    total_questions = len(QUESTIONS)
    percentage = score / total_questions * 100

    print("\n" + "=" * 40)
    print(f"Quiz complete, {player_name}!")
    print(f"Final score: {score}/{total_questions} ({percentage:.0f}%)")

    if percentage == 100:
        print("Excellent work - a perfect score!")
    elif percentage >= 70:
        print("Great job — you have a strong foundation.")
    elif percentage >= 40:
        print("Nice effort — keep practicing and try again.")
    else:
        print("Good start — review the topics and give it another try.")

    print("\nCategory results:")
    for category, results in category_scores.items():
        correct, total = results
        print(f"- {category}: {correct}/{total}")
    print("=" * 40)


def run_quiz():
    """Run each question, give feedback, and summarize the player's results."""
    print("=" * 40)
    print("         PYTHON TECH QUIZ")
    print("=" * 40)
    print("Test your knowledge of Python, Git, and web basics.\n")

    player_name = ask_name()
    score = 0
    category_scores = {}

    for question_number, question in enumerate(QUESTIONS, start=1):
        category = question["category"]
        if category not in category_scores:
            category_scores[category] = [0, 0]
        category_scores[category][1] += 1

        print(f"\nQuestion {question_number}/{len(QUESTIONS)} - {category}")
        print(question["question"])
        for choice, option in question["options"].items():
            print(f"  {choice}. {option}")

        answer = ask_answer(question["options"])
        if answer == question["answer"]:
            score += 1
            category_scores[category][0] += 1
            print("Correct!")
        else:
            correct_option = question["options"][question["answer"]]
            print(f"Not quite. The correct answer is {question['answer']}. {correct_option}")

        print(f"Why: {question['explanation']}")

    show_results(player_name, score, category_scores)


if __name__ == "__main__":
    run_quiz()
