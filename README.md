# Python Tech Quiz

A beginner-friendly command-line quiz that tests practical knowledge of Python, Git, and web fundamentals. It gives immediate explanations, tracks results by category, and calculates a final score—all using Python's standard library.

## Features

- Eight multiple-choice questions across three developer topics
- Input validation for names and answer choices
- Immediate answer feedback and short explanations
- Final percentage, encouragement, and category score breakdown
- No third-party dependencies

## Requirements

- Python 3.8 or newer

## Run in VS Code

1. Clone or download this repository and open its folder in VS Code.
2. Install the Microsoft Python extension if it is not already installed.
3. Open `main.py` and select a Python 3.8+ interpreter with **Python: Select Interpreter** from the Command Palette.
4. Open the integrated terminal (**Terminal > New Terminal**).
5. Run:

   ```bash
   python main.py
   ```

   On some Windows installations, use `py main.py` instead.
6. Enter your name, then type the letter of your answer for each question.

No package installation or virtual environment is required.

## Example output

The questions and score depend on your answers. A sample run might look like this:

```text
========================================
         PYTHON TECH QUIZ
========================================
Test your knowledge of Python, Git, and web basics.

Enter your name: Alex

Question 1/8 - Python
Which keyword is used to define a function in Python?
  A. func
  B. def
  C. function
  D. make
Your answer (A-D): B
Correct!
Why: Python functions are declared with the def keyword.

... remaining questions ...

========================================
Quiz complete, Alex!
Final score: 7/8 (88%)
Great job — you have a strong foundation.

Category results:
- Python: 3/4
- Git: 2/2
- Web: 2/2
========================================
```

## How it works

1. `QUESTIONS` stores each prompt, category, answer choices, correct letter, and explanation in a list of dictionaries.
2. `ask_name()` and `ask_answer()` use loops to re-prompt until the input is valid.
3. `run_quiz()` displays each question, checks the answer, and updates the overall and per-category scores.
4. `show_results()` calculates the percentage and prints a summary with a short performance message.
5. The `if __name__ == "__main__":` guard starts the quiz when you run `main.py` directly.

## Repository details

- **Suggested repository name:** `python-tech-quiz`
- **Description:** A beginner-friendly Python command-line quiz covering Python, Git, and web fundamentals, with instant feedback and category-based scoring.
- **Suggested commit message:** `Add interactive Python tech quiz`
