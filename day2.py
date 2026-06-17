# Exercise 1 - Simple if

number = int(input("Enter a number? "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 2 - Multiple Conditions

grade = int(input("Enter your grade: "))

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# Exercise 3 - Password Checker

correct_password = "python123"
password = input("Enter a password: ")

if password == correct_password:
    print("Access Granted")
else:
    print("Access Denied")

# Exercise 4 — Number Checker

number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is Positive")
elif number < 0:
    print(f"{number} is Negative")
else:
    print("Zero")

# Exercise 5 - Find Biggest Number

num1 = int(input("enter a 1st number: "))
num2 = int(input("enter a 2nd numbere: "))
num3 = int(input("Enter a 3rd number: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the biggest number")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the biggest number")
else:
    print(f"{num3} is the biggest number")


num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
operator = input("Enter an Operator(+, -, *, /): ")

if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid operator")

# Exercise 6 - Simple Login System

print("===== LOGIN SYSTEM =====")

correct_username = "admin"
correct_password = "python123"

username = input("enter a Username: ")
password = input("enter a Password: ")

if username == correct_username and password == correct_password:
    print("Login Successful!")
    print(f"Welcome, {username}")
else:
    print("Login Failed!")
    print("Wrong Password or Username")

print("===========================")

# Exercise 7 - Developer Quiz

print("========== DEVELOPER QUIZE ==========")
print("Answer Yes or No")
print("")

print("Answer Yes or No")
print("")

Q1 = input("Do you code every single day? ").lower()
Q2 = input("Do you push to GitHub daily? ").lower()
Q3 = input("Do you study English daily? ").lower()

if Q1 == "yes" and Q2 == "yes" and Q3 == "yes":
    print("")
    print("You will get a job in 6 months!")
    print("Keep going! 🚀")
else:
    print("Start doing ALL three daily!")
    print("Your job depends on it!")

print("=====================================")

# MINI PROJECT - Simple ATM
# Day 2 Project

print("")
print("Welcome to my ATM")
print("")

# Balance check
balance = 1000

print(f"Current Balance ${balance}")
print("")

# Ask What they want
print("What would you like to do?")
print("1. Check balance")
print("2. Deposite money")
print("3. Withdraw money")
print("")

choice = input("Enter a choice (1, 2 or 3): ")
print("")

if choice == "1":
    print(f"Your balance is : ${balance}")

elif choice == "2":
    amount = int(input("How much to deposite? $"))
    if amount > 0:
        balance += amount
        print(f"Deposite ${amount}")
        print(f"New balance: ${balance}")
    else:
        print("Invalid amount!")

elif choice == "3":
    amount = int(input("How much to withdraw? $"))
    if amount > balance:
        print("Not enough money!")
        print(f"Your balance is only ${balance}")
    elif amount <= 0:
        print("Invalid amount!")
    else:
        balance -= amount
        print(f"Withdraw ${balance}")
        print(f"New balance: {balance}")

else:
    print("Invalid choice!")

print("")
print("Thank you for using ATM!")
print("")