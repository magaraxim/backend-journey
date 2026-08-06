# Number Analysis Tool
# Uses: random, math, statistics
# Date: Thursday August 6, 2026

import random
import math
import statistics

def get_numbers_from_user():
    print("\n--- Enter Numbers ---")
    print("type numbers one by one")
    print("Type 'done' when finsished")
    print("Need at least 5 numbers")

    numbers = []

    while True:
        entry = input(f"Number {len(numbers)+1}: ").strip()

        if entry.lower() == "done":
            if len(numbers) < 5:
                print(f"Need at least 5 numbers! You have {len(numbers)}")
                continue
            break

        try:
            num = float(entry)
            numbers.append(num)
            print(f"Added (total: {len(numbers)})")
        except ValueError:
            print("Not a number! Try again.")

    return numbers

def generate_random_numbers(count=10,
                            min_val=1,
                            max_val=100
):
    numbers = []
    for _ in range(count):
        num = random.randint(min_val, max_val)
        numbers.append(num)

    return numbers

def analyze(numbers):
    sorted_nums = sorted(numbers)
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    total = sum(numbers)
    count = len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    range_val = maximum - minimum

    positive = [n for n in numbers if n > 0]
    negative = [n for n in numbers if n < 0]
    even_nums = [n for n in numbers 
                 if n % 2 == 0 and n == int(n)]
    odd_nums = [n for n in numbers
                if n % 2 != 0 and n == int(n)]

    return {
        "count": count,
        "total": total,
        "meain": mean,
        "median": median,
        "sorted": sorted_nums,
        "range": range_val,
        "positive": len(positive),
        "evens": len(even_nums),
        "odds": len(odd_nums),
        "negative": len(negative),
        "main_sqrt": math.sqrt(abs(mean))

    }

def display_result(numbers, result):
    print("\n" + "=" * 40)
    print("            Analysis result              ")
    print("=" * 40)
    print(f"Numbers : {numbers}")
    print(f"Sorted: {numbers['sorted']}")
    print(f"\nBasic Stats: ")
    print(f"Count: {numbers['count']}")
    print(f"Total: {numbers['tota']:.2f}")
    print(f"Mean: {numbers['mean']:.2f}")
    print(f"Median: {numbers['median']}")
    print(f"Max: {numbers['max']}")
    print(f"Min: {numbers['min']}")
    print(f"Range: {numbers['range']:.2f}")
    print("\nNumbers Type: ")
    print(f"Positive: {numbers['positive']}")
    print(f"Negative: {numbers['negative']}")
    print(f"Odds: {numbers['odds']}")
    print(f"Evens: {numbers['evens']}")


def main():
    print("=================================")
    print("      NUMBER ANALYSIS TOOL       ")
    print("=================================")

    numbers = None

    while True:
        print("\n--- Menu ---")
        print("1. Enter my own numbers")
        print("2. Generate random numbers")
        print("3. Analyze current numbers")
        print("4. Exit")

        choice = input("\nChoose (1-4): ").strip()

        if choice == "1":
            numbers = get_numbers_from_user()
            print(f"got {len(numbers)} numbers!")

        elif choice == "2":
            while True:
                try:
                    count = int(input("How many numbers(5-20): "))
                    if count < 5 or count > 20:
                        print("Must be 5-20!")
                        continue
                    break
                except ValueError:
                    print("Enter a number!")

            numbers = generate_random_numbers(count)
            print(f"Generated: {numbers}")

        elif choice == "3":
            if not numbers:
                print("No numbers yet!")
                print("Choose option 1 or 2 first!")
            else:
                results = analyze(numbers)
                display_result(numbers, results)

        elif choice == "4":
            print("\nGoodbyee!")
            break

        else:
            print("Invalid! choose 1-4")

main()


# Datetime Tracker
# Date: Thursday August 6, 2026

from datetime import date, datetime, timedelta

def days_between(start, end):
    return (end - start).days

def format_date(d):
    return d.strftime("%B %d, %Y (%A)")

def main():
    print("================================")
    print("    JOURNEY TRACKER 📅          ")
    print("================================")

    today = date.today()
    now = datetime.now()

    # Important dates
    start_date = date(2026, 8, 5)
    freelance_date = date(2026, 10, 1)
    job_date = date(2027, 2, 1)

    print(f"\n📅 TODAY: {format_date(today)}")
    print(f"🕐 TIME : {now.strftime('%H:%M:%S')}")

    print(f"\n=== YOUR JOURNEY ===")
    days_coding = days_between(
        start_date, today) + 1
    days_freelance = days_between(
        today, freelance_date)
    days_job = days_between(today, job_date)

    print(f"Days coding     : {days_coding} 🔥")
    print(f"Until freelance : {days_freelance} days")
    print(f"Until remote job: {days_job} days")
    print(f"Months to job   : ~{days_job//30}")

    print(f"\n=== MILESTONES ===")
    milestones = [
        (date(2026, 8, 5), "🚀 Journey started"),
        (date(2026, 9, 1), "🌐 Flask + APIs"),
        (date(2026, 10, 1), "💼 Freelance starts"),
        (date(2026, 11, 1), "🔍 Job hunting"),
        (date(2027, 2, 1), "🎉 Remote job target"),
    ]

    for milestone_date, name in milestones:
        diff = days_between(today, milestone_date)
        if diff < 0:
            status = "✅ Done!"
        elif diff == 0:
            status = "🎯 TODAY!"
        else:
            status = f"In {diff} days"
        print(f"  {name}")
        print(f"    {milestone_date} — {status}")

    print(f"\n=== STUDY SCHEDULE ===")
    for i in range(7):
        day = today + timedelta(days=i)
        day_name = day.strftime("%A")
        if day_name == "Sunday":
            plan = "Rest day 😴"
        else:
            plan = "Full study day 💪"
        print(f"  {day.strftime('%b %d')} "
              f"({day_name:<10}): {plan}")

main()

# MAIN PROJECT — Complete Utility Toolkit
# Date: Thursday August 6, 2026
# Uses ALL libraries + everything from Day 1

import random
import math
import string
import statistics
from datetime import date, datetime, timedelta

def password_generator():
    print("\n=== PASSWORD GENERATOR 🔐 ===")

    while True:
        try:
            length = int(input("Length (8-32): "))
            if length < 8 or length > 32:
                print("Must be 8-32!")
                continue
            break
        except ValueError:
            print("Enter a number!")

    use_sym = input(
        "Include symbols? (yes/no): ").lower()

    chars = (string.ascii_letters +
             string.digits)
    if use_sym == "yes":
        chars += "!@#$%^&*"

    passwords = []
    for _ in range(5):
        pwd = ''.join(
            random.choices(chars, k=length))
        passwords.append(pwd)

    print("\nGenerated passwords:")
    for i, pwd in enumerate(passwords, 1):
        print(f"  {i}. {pwd}")

def number_stats():
    print("\n=== NUMBER STATISTICS 📊 ===")
    print("Enter numbers separated by spaces:")

    while True:
        try:
            raw = input("Numbers: ").strip()
            nums = [float(x)
                    for x in raw.split()]
            if len(nums) < 2:
                print("Enter at least 2 numbers!")
                continue
            break
        except ValueError:
            print("Only numbers please!")

    print(f"\nResults:")
    print(f"Count  : {len(nums)}")
    print(f"Sum    : {sum(nums):.2f}")
    print(f"Mean   : {statistics.mean(nums):.2f}")
    print(f"Median : {statistics.median(nums):.2f}")
    print(f"Max    : {max(nums):.2f}")
    print(f"Min    : {min(nums):.2f}")
    print(f"Range  : {max(nums)-min(nums):.2f}")

def lucky_draw():
    print("\n=== LUCKY DRAW 🎰 ===")
    print("Enter names (one per line)")
    print("Type 'done' when finished")

    names = []
    while True:
        name = input("Name: ").strip()
        if name.lower() == "done":
            if len(names) < 2:
                print("Need at least 2!")
                continue
            break
        if name:
            names.append(name)
            print(f"  Added: {name} ✅")

    while True:
        try:
            winners = int(input(
                f"How many winners (1-{len(names)}): "))
            if winners < 1 or winners > len(names):
                print("Invalid number!")
                continue
            break
        except ValueError:
            print("Enter a number!")

    selected = random.sample(names, winners)
    now = datetime.now()

    print(f"\n🎉 WINNER(S) at "
          f"{now.strftime('%H:%M:%S')}:")
    for i, winner in enumerate(selected, 1):
        print(f"  {i}. {winner} 🏆")

def date_calculator():
    print("\n=== DATE CALCULATOR 📅 ===")
    today = date.today()
    print(f"Today: {today.strftime('%B %d, %Y')}")

    print("\n1. Days between two dates")
    print("2. Add days to today")
    print("3. Days until a date")

    while True:
        try:
            choice = int(input("Choose (1-3): "))
            if choice not in [1, 2, 3]:
                print("Choose 1-3!")
                continue
            break
        except ValueError:
            print("Enter a number!")

    if choice == 1:
        try:
            d1 = input("Start date (YYYY-MM-DD): ")
            d2 = input("End date (YYYY-MM-DD): ")
            start = date.fromisoformat(d1)
            end = date.fromisoformat(d2)
            diff = abs((end - start).days)
            print(f"Days between: {diff}")
        except ValueError:
            print("Invalid date format!")

    elif choice == 2:
        try:
            days = int(input("Add how many days: "))
            result = today + timedelta(days=days)
            print(f"Result: "
                  f"{result.strftime('%B %d, %Y')}")
        except ValueError:
            print("Enter a number!")

    elif choice == 3:
        try:
            d = input("Target date (YYYY-MM-DD): ")
            target = date.fromisoformat(d)
            diff = (target - today).days
            if diff > 0:
                print(f"Days until: {diff}")
            elif diff == 0:
                print("That's today!")
            else:
                print(f"That was {abs(diff)} days ago")
        except ValueError:
            print("Invalid date format!")

def math_toolkit():
    print("\n=== MATH TOOLKIT 🧮 ===")
    print("1. Circle calculator")
    print("2. Percentage calculator")
    print("3. Power calculator")
    print("4. Square root")

    while True:
        try:
            choice = int(input("Choose (1-4): "))
            if choice not in [1, 2, 3, 4]:
                print("Choose 1-4!")
                continue
            break
        except ValueError:
            print("Enter a number!")

    if choice == 1:
        r = float(input("Radius: "))
        print(f"Area: {math.pi * r**2:.2f}")
        print(f"Circumference: {2*math.pi*r:.2f}")

    elif choice == 2:
        total = float(input("Total amount: "))
        pct = float(input("Percentage: "))
        print(f"Result: {(pct/100)*total:.2f}")

    elif choice == 3:
        base = float(input("Base: "))
        exp = float(input("Exponent: "))
        print(f"Result: {math.pow(base, exp):.2f}")

    elif choice == 4:
        num = float(input("Number: "))
        if num < 0:
            print("Cannot sqrt negative!")
        else:
            print(f"√{num} = {math.sqrt(num):.4f}")

def main():
    print("================================")
    print("   COMPLETE UTILITY TOOLKIT 🛠️  ")
    print(f"   {datetime.now().strftime('%B %d, %Y')}")
    print("   Nepal 🇳🇵 → World 🌍")
    print("================================")

    tools = {
        "1": ("Password Generator 🔐",
               password_generator),
        "2": ("Number Statistics 📊",
               number_stats),
        "3": ("Lucky Draw 🎰",
               lucky_draw),
        "4": ("Date Calculator 📅",
               date_calculator),
        "5": ("Math Toolkit 🧮",
               math_toolkit),
    }

    while True:
        print("\n=== TOOLS MENU ===")
        for key, (name, _) in tools.items():
            print(f"{key}. {name}")
        print("6. Exit")

        choice = input("\nChoose tool: ").strip()

        if choice in tools:
            _, func = tools[choice]
            try:
                func()
            except Exception as e:
                print(f"❌ Error: {e}")
        elif choice == "6":
            print("\n✅ Goodbye Buddha!")
            print("Keep building! 💪")
            break
        else:
            print("❌ Invalid choice!")

main()






        

    



            

    
