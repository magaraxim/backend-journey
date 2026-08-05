# # String Practice

# sentence = "I am a backend developer from Nepal"

# # Split into words
# words = sentence.split()
# print(f"Words: {words}")
# print(f"Words Count: {len(words)}")

# # Join words back
# joined = " ".join(words)
# print(f"Joined: {joined}")

# # Find + replace
# new = sentence.replace("Nepal", "🇳🇵 Nepal")
# print(f"New: {new}")

# # Check contains
# pi = 3.14159265
# print(f"pi (2 decimal): {pi:.2f}")
# print(f"pi (4 decimal): {pi:.4f}")

# # Padding
# name = "Ashim"
# print(f"{'name':<15}: {name}")
# print(f"{'Country':<15}: Nepal")
# print(f"{'Goal':<15}: Backend Dev")


# # List Practice

# numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]

# print(f"Original : {numbers}")
# print(f"Sorted   : {sorted(numbers)}")
# print(f"Reversed : {sorted(numbers, reverse=True)}")
# print(f"Max      : {max(numbers)}")
# print(f"Min      : {min(numbers)}")
# print(f"Average  : {sum(numbers)/len(numbers):.1f}")

# # Filter with list comprehension
# evens = [n for n in numbers if n % 2 == 0]
# odds = [n for n in numbers if n % 2 != 0]
# big = [n for n in numbers if n > 5]

# print(f"\nEvens  : {evens}")
# print(f"Odds   : {odds}")
# print(f"Over 5 : {big}")

# # Nested list
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print("\nMatrix: ")
# for row in matrix:
#     for num in row:
#         print(f"{num:3}", end="")
#     print()

# for row in reversed(matrix):
#     for num in reversed(row):
#         print(num, end=" ")
#     print()

# # Dictionary Practice

# # Student grades
# students = {
#     "Buddha": [95, 88, 92],
#     "Priya": [78, 85, 90],
#     "Raj": [65, 72, 68],
#     "Sita": [91, 94, 88]
# }

# print("\n--- Grade Report ---")
# for name, grades in students.items():
#     avg = sum(grades) / len(grades)
#     if avg >= 90:
#         grade = "A"
#     elif avg >= 80:
#         grade = "B"
#     elif avg >= 70:
#         grade = "C"
#     elif avg >= 60:
#         grade = "D"
#     else:
#         grade = "F"

#     print(f"{name:<10}: {avg:.1f} {grade}")

# # Find top students
# top = max(students,
#           key=lambda n: sum(students[n])/len(students[n]))
# print(f"\nTop Student: {top}")

# Advanced Functions

# Default parameters
def create_profile(name, age,
                   country="Nepla",
                   role="Developer"):
    return{
        "name": name,
        "age": age,
        "country": country,
        "role": role
    }

p1 = create_profile("Ashim", 19)
p2 = create_profile("John", 28,
                    "USA", "Manager")

print(p1)
print(p2)

# * args - multiple arguments
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3))
print(add_all(1, 2, 3, 4, 5))

# ** Kwargs - keyword argements
def show_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

show_info(name="Ashim",
          age=19,
          country="Nepal")

# Lambda functions
square = lambda x: x **2
double = lambda x: x * 2
add = lambda a, b: a + b

print(square(5))
print(double(7))
print(add(5, 6))

# Map + filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0,
                    numbers))

print(f"Squared : {squared}")
print(f"Evens   : {evens}")

# Error Handling Advanced

# Custom exception
class InvalidAgeError(Exception):
    pass

class InvalidGradeError(Exception):
    pass

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be integer!")
    if age < 0 or age > 120:
        raise InvalidAgeError(
            f"Age {age} is not realistic!")
    return True

def validate_grade(grade):
    if not isinstance(grade, (int, float)):
        raise TypeError("Grade must be number!")
    if grade < 0 or grade > 100:
        raise InvalidGradeError(
            f"Grade {grade} is out of range!")
    return True

# Test custom exceptions
test_ages = [25, -5, 150, "old", 19]
for age in test_ages:
    try:
        validate_age(age)
        print(f"Age {age} is valid!")
    except TypeError as e:
        print(f"TypeError: {e}")
    except InvalidAgeError as e:
        print(f"InvalidAge: {e}")

# Finally block
def read_data(filename):
    file = None
    try:
        file = open(filename, "r")
        return file.read()
    except FileNotFoundError:
        return "file not found!"
    finally:
        print("Always runs - cleanup!")
        if file:
            file.close()

result = read_data("test.txt")
print(result)
        