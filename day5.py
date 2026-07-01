# Exercise 1 - Basic Try/Except

try:
    age = int(input("Enter your age: "))
    print(f"your age is {age}")

except ValueError:
    print("Invalid input! Please enter an integer.")


# Exercise 2 — Division Safety

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2

except ValueError:
    print("Invalid input! Please enter integers only.")

except ZeroDivisionError:
    print("Cannot divide by Zero!")

else:
    print(f"{num1} ÷ {num2} = {result}")


# Exercise 3 — Keep Asking Until Valid

def main():
    age = get_int("Enter age: ")
    print(f"Your age is {age}")

def get_int(prompt):
    while True:
        try:
            age = int(input(prompt))

            if age <= 0:
                print("Age cannot be negative.")
                continue

            return age
        
        except ValueError:
            print("Invalid input! Please enter an integer.")

main()

# Exercise 4 — List Index Safety

fruits = ["Apple", "Banana", "Orange", "Mango"]

while True:
    try:
        index = int(input("Enter Index(0 - 3)"))
        print(f"fruit: {fruits[index]}")
        break

    except ValueError:
            print("Invalid input! Please enter an intgeger.")

    except IndexError:
            print("Invalid index! That index doesn't exist in the list.")


# Exercise 5 - Safe Calculator

while True: 
    try:
        num1 = int(input("Enter the first number: "))
        operator = input("Enter Operator(+ - * /): ")
        num2 = int(input("Enter the second number: "))

        if operator == "+":
            print(f"{num1} + {num2} = {num1 + num2}")

        elif operator == "-":
            print(f"{num1} - {num2} = {num1 - num2}")

        elif operator == "*":
            print(f"{num1} * {num2} = {num1 * num2}")

        elif operator == "/":
            print(f"{num1} ÷ {num2} = {num1 / num2}")

        else:
            print("Invalid Operator!")
            continue

    except ValueError:
        print("Invalid number! Please enter integers only.")

    except ZeroDivisionError:
        print("Cannot divid by zero!")

    again = input("Another Calculation? (y/n): ").lower()

    if again == "n":
        print("Goodbye!")
        break


# Exercise 6 - Safe Login With Retry Limit

def main():
    correct_username = "admin"
    correct_password = "python123"
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter Username: ")
        password = input("Enter Passowrd: ")

        if username == correct_username and password == correct_password:
            print("Access granted!")
            return

        else:
            attempts += 1
            remaining = max_attempts - attempts

            if remaining > 0:
                print(f"Wrong user name or password! {remaining} attempts left")

            else:
                print("Too many failed attempts. Account locked!")


main()

# Exercise 7 - Safe File Reading

try:
    with open("data.txt") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File doesn't exist! Creating it now..")

    with open("data.txt", "w") as file:
        file.write("hellw this is my first file!")

    print("File created!")

# MINI PROJECT - Crash-Proof Quiz App
# Day 5 Project - Using Exception Handling

# MINI PROJECT - Crash-Proof Quiz App
# Day 5 Project - Using Exception Handling

def get_valid_number(prompt, min_val, max_val):
    while True:
        try:
            num = int(input(prompt))
            if num < min_val or num > max_val:
                print(f"Please enter between {min_val} and {max_val}")
                continue
            return num
        except ValueError:
            print("That's not a number! Try again.")

def ask_question(question, options, correct_answer):
    print(f"\n{question}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    answer = get_valid_number("Your answer (1-4): ", 1, len(options))
    
    if answer == correct_answer:
        print("Correct! ✅")
        return True
    else:
        print(f"Wrong! Correct answer was {options[correct_answer-1]} ❌")
        return False

def main():
    print("================================")
    print("    CRASH-PROOF QUIZ APP 🧠     ")
    print("================================")
    
    score = 0
    total_questions = 3
    
    q1 = ask_question(
        "What is 10 + 5?",
        ["12", "15", "20", "25"],
        2
    )
    if q1:
        score += 1
    
    q2 = ask_question(
        "What is ValueError?",
        ["A type of fruit", "Wrong data type error", "A loop", "A function"],
        2
    )
    if q2:
        score += 1
    
    q3 = ask_question(
        "What does ZeroDivisionError mean?",
        ["Dividing by zero", "A typo", "Missing semicolon", "Wrong variable"],
        1
    )
    if q3:
        score += 1
    
    print("\n================================")
    print(f"Final Score: {score}/{total_questions}")
    
    if score == total_questions:
        print("Perfect score! You're a star! 🌟")
    elif score >= total_questions / 2:
        print("Good job! Keep learning!")
    else:
        print("Keep practicing! You'll improve!")
    print("================================")

main()

    
              

