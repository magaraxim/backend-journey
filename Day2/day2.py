# DAY 2 - LIBARIES FAST REVIEW
# Date: Thursday August 6, 2026

import random
import math
import string
import statistics
from datetime import date, datetime

print("=" * 40)
print("           LIBARIES REVIEW                ")
print("=" * 40)

#=============================================
# 1. RANDOM
#=============================================
print("\n--- Random ---")
print(random.randint(1, 100))
print(random.choice(["Python", "Flask",
                     "PostgreSQL"]))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

students = random.sample(
    ["Ashim", "Bob", "Diana",
     "Alice", "john"], 3)
print(f"Students: {students}")

print(f"Random Uniform: {random.uniform(0, 1):.4f}")

#=============================================
# 2. MATH
#=============================================
print("\n--- Math ---")
print(f"Pi         : {math.pi:.4f}")
print(f"Sqrt(144)  : {math.sqrt(144)}")
print(f"Floor(4.1) : {math.floor(4.9)}")
print(f"Ceil(4.1)  : {math.ceil(4.1)}")
print(f"2^10       : {int(math.pow(2, 10))}")
print(f"abs(-5)    : {abs(-5)}")

#=============================================
# 3. STRING
#=============================================
print("\n--- String ---")
print(f"Letters         : {string.ascii_letters}")
print(f"Digits          : {string.digits}")
print(f"Punctuation     : {string.punctuation}")

# Generate Random Password
password = ''.join(
    random.choices(
        string.ascii_letters +
        string.digits,
        k=10
    )
)
print(f"Random Password : {password}")

#=============================================
# 4. STATISTICS
#=============================================
print("\n--- Statistics ---")
scores = [78, 92, 85, 67, 95]

print(f"Scores : {scores}")
print(f"Mean   : {statistics.mean(scores):.1f}")
print(f"Median : {statistics.median(scores)}")
print(f"Max    : {max(scores)}")
print(f"Min    : {min(scores)}")
print(f"Range  : {max(scores) - min(scores)}")

#=============================================
# 5. DATETIME
#=============================================
print("\n--- Datetime ---")
today = date.today()
now = datetime.now()

print(f"Today   : {today}")
print(f"Year    : {today.year}")
print(f"Month   : {today.month}")
print(f"Day     : {today.day}")
print(f"Time    : {now.strftime('%H:%M:%S')}")
print(f"Full    : {now.strftime('%B %d, %Y')}")
print(f"Weekday : {now.strftime('%A')}")

# Random - deeper practice

import random

# Weighted choice (some items more likely)
items = ["common", "rare", "epic", "legendary"]
weights = [60, 30, 10, 3]

print("--- Item Drop ---")
drops = []

for _ in range(10):
    drop = random.choices(items,
                          weights=weights)[0]
    drops.append(drop)
    print(f"You got : {drops}")

print(f"\nDrop Summary: ")
for item in items:
    count = drops.count(item)
    print(f"{item} : {count}x")

# Shuffle and deal cards
suits = ["♠", "♥", "♦", "♣"]
values = ["2","3","4","5","6","7",
          "8","9","10","J","Q","K","A"]

deck = []

for s in suits:
    for v in values:
        deck.append(f"{v}{s}")

random.shuffle(deck)

print("\n--- Card Game ---")
print(f"Deck size : {len(deck)}")
print(f"Your Hand : {deck[:5]}")
print(f"My Hand   : {deck[5:10]}")

# Math - practical uses
import math

print("\n--- Practical Math ---")

# Circle Calculators
# Fourmula: Area = πr2
# Fourmula: C=2πr
radius = float(input("Enter circle radius: "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"Area : {area:.2f}")
print(f"Circumference: {circumference:.2f}")

# Percentage Calculator
total = float(input("\nTotal amount: "))
percentage = float(input("Percentage: "))
result = (percentage / 100) * total
print(f"{percentage}% of {total} = {result}")

# Distance between two points

x1, y1 = 0, 0
x2, y2 = 3, 4
distance = math.sqrt(
    (x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance: {distance:.2f}")

# Compund interest
# Formual: A=P(1+r)t
principal = 1000
rate = 0.05
years = 10
amount = principal * math.pow(
    1 + rate, years)

print(f"\nCompound interest: ")
print(f"Principal: ${principal}")
print(f"After {years} years: ${amount:.2f}")

# Datetime - practical uses

from datetime import date, datetime, timedelta

print("--- Datetime Practical ---")

today = date.today()
now = datetime.now()

# Days until goal
goal_date = date(2027, 2, 1)
days_left = (goal_date - today).days
print(f"Days until skilled developer : {days_left} days")
print(f"Month approx: {days_left//30}")

# Days until freelance
freelance_date = date(2026, 10, 1)
freelance_days = (
    freelance_date - today
).days
print(f"Days until freelance: {freelance_days}")

# Time formatting
print(f"\nFormatted times: ")
print(f"Short: {now.strftime('%d/%m/%Y')}")
print(f"Long: {now.strftime('%B %d, %Y')}")
print(f"Time: {now.strftime('%I:%M: %p')}")
print(f"Full : {now.strftime('%A, %B %d, %Y at %H:%M')}")


# Add/subtract days
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
last_week = today - timedelta(weeks=1)

print(f"\nToday   : {today}")
print(f"Tomorrow  : {tomorrow}")
print(f"Next Week : {next_week}")
print(f"Last Week : {last_week}")

# Study streak calculator
start_date = date(2026, 8, 5)
days_studied = (
    today - start_date
).days +1
print(f"\nStudy streak: {days_studied} days!")

# String + Random - Password Generator

import random
import string

def generate_password(
        length=12,
        use_upper=True,
        use_digits=True,
        use_symbols=True
):
    chars = string.ascii_lowercase

    required = []
    if use_upper:
        chars += string.ascii_uppercase
        required.append(
            random.choice(string.ascii_uppercase)
        )
    if use_digits:
        chars += string.digits
        required.append(
            random.choice(string.digits)
        )
    if use_symbols:
        chars += "!@#$%^&*"
        required.append(
            random.choice("!@#$%^&*")
        )

        remaining = length - len(required)
        password = required + [
            random.choice(chars)
            for _ in range(remaining)]

        random.shuffle(password)
        return ''.join(password)

def check_strength(password):
    score = 0
    if len(password) >= 12: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*" for c in password): score += 1

    if score == 4: return "Very Strong"
    elif score == 3: return "Strong"
    elif score == 2: return "Medium"
    else: return "Weak"

print("--- Password Generator ---")
print("\nGenerating 5 Password: ")
for i in range(5):
    pwp = generate_password(16)
    strength = check_strength(pwp)
    print(f"{i+1}. {pwp}")
    print(f"Strength: {strength}")
    print()    
