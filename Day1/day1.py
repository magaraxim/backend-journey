# Day 1 - Python Basics Review
# Date: Wedensday August 5, 2026
# Name: Buddha -- Nepal 

#=============================================
# 1. VARIABLES + DATA TYPES
#=============================================
name = "Ashim"
age = 19
country = "Nepal"
goal = "Backend Devloper"
is_ambitious = True
hourly_rate = 15.50
favorite_game = "Chess"
favorite_color = "red"

print("==============================")
print("         My Profile           ")
print("==============================")
print(f"Name           : {name}")
print(f"Age            : {age}")
print(f"Country        : {country}")
print(f"Ambitious      : {is_ambitious}")
print(f"Rate           : {hourly_rate}")
print(f"Favorite Game  : {favorite_game}")
print(f"Favorite Color : {favorite_color}")

#=============================================
# 2. STRING METHODS
#=============================================
message = "   hello from nepal   "
print("\n--- String Methods ---")
print(message.strip())          # remove white spaces
print(message.strip().lower())  # Lowercase
print(message.strip().upper())  # Uppercase
print(message.strip().title())  # Title Case
print(message.strip().replace("nepal", "Nepla"))
print(len(message.strip()))     # length

# Check string
word = "Python"
print(f"\n{word} is alpha  : {word.isalpha()}")
print(f"{word} is digit    : {word.isdigit()}")
print(f"Start with P       : {word.startswith('P')}")
print(f"Ends with n        : {word.endswith('n')}")

#=============================================
# 3. CONDITION
#=============================================
print("\n--- Conditions ---")
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")

# Operators reminder:
# >= greater than or equal ✅
# => does NOT exist ❌
# <= less than or equal
# == equal to
# != not equal to
# and — both must be true
# or  — one must be true
# not — reverses boolean

#=============================================
# 4. FOR LOOP
#=============================================
print("\n--- For Loop ---")
skills = ["Python", "Flask",
          "PostgreSQL", "Docker"]

for skill in skills:
    print(f"-> {skill}")

# With enumerate
print("\nNumbered: ")
for i, skill in enumerate(skills, start=1):
    print(f"{i}. {skill}")

# Range
print("\nCounting 1-10: ")
for i in range(1, 11):
    print(i, end=" ")
print()

# List Comprehension
squares = [i**2 for i in range(1, 6)]
print(f"\nSquares: {squares}")

#=============================================
# 5. WHILE LOOP
#=============================================
print("\n--- While Loop ---")
count = 5
while count >= 0:
    if count == 0:
        print("Launch!")
    else:
        print(f"{count}...")
    count -= 1

#=============================================
# 6. FUNCTIONS
#=============================================
print("\n--- Functions ---")

def greet(name, country="Nepal"):
    return f"Hello {name} from {country}"

def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Cannot divid by Zero!"
        return a / b
    return "Unkown Operation!"

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
print(greet("Ashim"))
print(greet("Priya", "India"))
print(calculate(10, 5, "add"))
print(calculate(10, 5, "divide"))
print(calculate(10, 0, "divide"))
print(get_grade(85))

#=============================================
# TRY/EXCEPT - ALL 3 PATTERNS
#=============================================
print("\n--- Try/Except ---")

# Pattern 1 - Basic
try:
    num = int(input("Enter Number: "))
    print(f"You Entered: {num}")
except ValueError:
    print("Not a number")

# Pattern 2 - Multiple exceptions
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter sceond number: "))
    print(f"Division: {a/b:}")
except ValueError:
    print("Numbers Only!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Pattern 3 - While Tre + try
def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid! Try again!")

def main():
    number = get_number("Enter valid number: ")
    print(f"You entered: {number}")

main()

#=============================================
# 8. LISTS
print("\n--- Lists ---")
fruits = ["apple", "banana", "orange"]

# Add
fruits.append("mango")
print(f"After append: {fruits}")

# Remove
fruits.remove("banana")
print(f"After remove: {fruits}")

# Short
fruits.sort()
print(f"After sort: {fruits}")

# Check membership
print(f"Has apple: {'apple' in fruits}")
print(f"Length: {len(fruits)}")

# Slice
print(f"First 2: {fruits[:2]}")
print(f"Last 2 : {fruits[-2:]}")

#=============================================
# 9. DICTIONARIES
#=============================================
print("\n--- Dictionaries ---")
person = {
    "name": "Buddha",
    "age": 19,
    "country": "Nepal",
    "skills": ["Python", "Flask"],
    "employed": False
}

# Access
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Add + update
person["goal"] = "Backend Devoloper"
person["age"] = 20
print(f"Updated age: {person['age']}")
print(f"Goal: {person['goal']}")

# Loop through
print("\nAll info: ")
for key, value in person.items():
    print(f"{key}: {value}")


# Check key exists
print(f"\nHas 'name': {'name' in person}")
print(f"Has 'salary': {'salary' in person}")

# Get with default
salary = person.get("salary", "Not set yet")
print(f"Salary: {salary}")

