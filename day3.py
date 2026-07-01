# Exercise 1 - Basic For Loop

for i in range(5):
    print(f"This is number {i}")

print("Loop finished!")

# Exercise 2 - Count 1 to 10

for i in range(1, 11):
    print(i)

# Exercise 3 - Multiplication Table

number = int(input("Enter a number: "))

print(f"Multiplication table of {number}")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

# Exercise 4 - Sum of Numbers

total = 0
for i in range(1, 11):
    total = total + i

print(f"Sum of 1 to 10 is: {total}")

# Exercise 5 - Basic While Loop

count = 1
while count <= 5:
    print(f"Count is {count}")
    count = count + 1

print("Loop finished!")

# Exercise 6 - Password Retry System

correct_password = "python123"
password = ""

while password != correct_password:
    password = input("Enter password: ")
    if password != correct_password:
        print("Wrong password! Try again.")

print("Access granted! Welcome!")

# Exercise 7 - Number Guessing Game

secret_number = 7
guess = 0

print("Guess the number between 1-10")

while guess != secret_number:
    guess = int(input("Your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You win!")

# MINI PROJECT - Advanced Number Guessing Game
# Day 3 Project

import random

print("================================")
print("    NUMBER GUESSING GAME 🎮     ")
print("================================")

secret_number = random.randint(1, 50)
attempts = 0
max_attempts = 7
guessed = False

print("I'm thinking of a number between 1-50")
print(f"You have {max_attempts} attempts")
print("")

while attempts < max_attempts and not guessed:
    guess = int(input("Your guess: "))
    attempts = attempts + 1
    
    if guess == secret_number:
        guessed = True
        print(f"🎉 Correct! You won in {attempts} attempts!")
    elif guess < secret_number:
        remaining = max_attempts - attempts
        print(f"Too low! {remaining} attempts left")
    else:
        remaining = max_attempts - attempts
        print(f"Too high! {remaining} attempts left")

if not guessed:
    print("")
    print(f"Game over! The number was {secret_number}")

print("================================")
print("       Thanks for playing!       ")
print("================================")