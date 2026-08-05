
# ==========================================
# PROJECT: To-do Task Manager
# Date: Wednesday, August 5, 2026
#
# Description:
# A command-line application to manage daily
# tasks. Users can add, complete, delete,
# view tasks, and display task statistics.
#
# Features:
# - Add Task
# - Show Tasks
# - Complete Task
# - Delete Task
# - Task Statistics
# ==========================================

tasks = {}

def add_task(task):
    task = task.strip() # Remove white spaces 

    if not task:
        print("Task Cannot Be Empty!")
        return
    task_id = len(tasks) + 1

    tasks[task_id] = {
        "task": task,
        "completed": False
    }
    print("Task Added!")

def show_tasks():
    if not tasks:
        print("No tasks found!")
        return

    for task_id, info in tasks.items():
        if info["completed"]:
            status = "Completed!"
        else:
            status = "Pending!"

        print(f"{task_id}. {info['task']} - {status}")

def complete_task(task_id):
    if task_id not in tasks:
        print("No task found!")
        return
    
    tasks[task_id]["completed"] = True
    print("Task Completed")

def delete_task(task_id):
    if task_id not in tasks:
        print("No task found!")
        return

    del tasks[task_id]
    print("Task deleted!")

def task_statistics():
    print("--- Statistics ---")
    total_tasks = len(tasks)
    completed_task = 0
    for task_id, info in tasks.items():
        if info["completed"]:
            completed_task += 1

    pending_tasks  = total_tasks - completed_task

    if total_tasks == 0:
        completion_rate = 0
    else:
        completion_rate = (completed_task / total_tasks) * 100

    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_task}")
    print(f"Pending Tasks: {pending_tasks}")
    print(f"Completion Rate: {completion_rate:.1f}%")

def main():
    print("\n=============================")
    print("              Menu             ")
    print("===============================")
    while True:    
        print("\n1. Add Task")
        print("2. Show Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Statistics")
        print("6. Exit")

        choice = input("Choose: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Task ID: "))
                complete_task(task_id)
            except ValueError:
                print("please enter a valid numbers!")

        elif choice == "4":
            task_id = int(input("Task ID: "))
            delete_task(task_id)

        elif choice == "5":
            task_statistics()

        elif choice == "6":
            print("Goodbyee!")
            break
        else:
            print("Invalid Choice!")

main()

# Personal Expense Tracker
# Date: Wednesday August 5, 2026

expenses = []
income = []

def add_expense():
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    if amount <= 0:
        print("amount must be positive!")
        return

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")

def show_expenses():
    print("\n--- My Expenses ---")
    if not expenses:
        print("No expenses yet!")
        return

    for expense in expenses:
        print(f"{expense['category']}: ${expense['amount']:.2f}")

def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total

def add_income():
    source = input("enter income source: ")
    amount = float(input("enter amount: "))

    if amount <= 0:
        print("Amount must be positive!")
        return

    money = {
        "source": source,
        "amount": amount
    }

    income.append(money)
    print("Income added successfully!")

def show_income():
    print("\n--- My Income ---")

    if not income:
        print("No Income Yet!")
        return

    for money in income:
        print(f"{money['source']}: ${money['amount']:.2f}")

def calculate_income_total():
    total = 0

    for money in income:
        total += money["amount"]

    return total

def calculate_balance():

    income_total = calculate_income_total()

    expense_total = calculate_total()

    balance = income_total - expense_total

    return balance

            
def main():

    print("========================")
    print(" PERSONAL BUDGET TRACKER ")
    print("========================")

    while True:

        print("\n=== MENU ===")

        print("1. Add Expense")
        print("2. Add Income")
        print("3. View Expenses")
        print("4. View Income")
        print("5. View Balance")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            add_income()

        elif choice == "3":
            show_expenses()

        elif choice == "4":
            show_income()

        elif choice == "5":
            balance = calculate_balance()
            print(f"Current Balance: ${balance}")

        elif choice == "6":
            print("Goodbye! Save money 💰")
            break

        else:
            print("Invalid choice!")

main()

# MAIN PROJECT — Task Manager
# Date: Wednesday August 5, 2026
# Uses EVERYTHING from Day 1:
# variables, conditions, loops,
# functions, try/except,
# lists, dictionaries, string methods

from datetime import date

tasks = []
task_id = 1

def add_task(title, priority="medium",
             category="general"):
    global task_id

    if not title.strip():
        print("❌ Title cannot be empty!")
        return

    valid_priorities = ["low", "medium", "high"]
    if priority.lower() not in valid_priorities:
        print(f"❌ Priority must be: "
              f"{', '.join(valid_priorities)}")
        return

    task = {
        "id": task_id,
        "title": title.strip().capitalize(),
        "priority": priority.lower(),
        "category": category.strip().title(),
        "status": "pending",
        "created": str(date.today()),
        "completed": None
    }

    tasks.append(task)
    task_id += 1
    print(f"✅ Task #{task['id']} added!")

def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "completed":
                print("⚠️ Already completed!")
                return
            task["status"] = "completed"
            task["completed"] = str(date.today())
            print(f"✅ Task #{task_id} completed!")
            return
    print(f"❌ Task #{task_id} not found!")

def delete_task(task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            removed = tasks.pop(i)
            print(f"✅ Deleted: '{removed['title']}'")
            return
    print(f"❌ Task #{task_id} not found!")

def show_tasks(filter_status=None,
               filter_priority=None):
    filtered = tasks.copy()

    if filter_status:
        filtered = [t for t in filtered
                   if t["status"] == filter_status]

    if filter_priority:
        filtered = [t for t in filtered
                   if t["priority"] == filter_priority]

    if not filtered:
        print("No tasks found!")
        return

    # Sort by priority
    priority_order = {"high": 0,
                      "medium": 1, "low": 2}
    filtered.sort(
        key=lambda t: priority_order[t["priority"]])

    print(f"\n{'ID':<5}{'Title':<25}"
          f"{'Priority':<10}{'Status':<12}"
          f"{'Category'}")
    print("-" * 65)

    for task in filtered:
        status_icon = "✅" if task["status"] \
                      == "completed" else "⏳"
        priority_icon = {
            "high": "🔴",
            "medium": "🟡",
            "low": "🟢"
        }[task["priority"]]

        print(f"#{task['id']:<4}"
              f"{task['title']:<25}"
              f"{priority_icon} {task['priority']:<8}"
              f"{status_icon} {task['status']:<10}"
              f"{task['category']}")

def show_statistics():
    print("\n=== TASK STATISTICS 📊 ===")
    total = len(tasks)
    completed = sum(1 for t in tasks
                   if t["status"] == "completed")
    pending = total - completed

    high = sum(1 for t in tasks
               if t["priority"] == "high"
               and t["status"] == "pending")

    print(f"Total tasks    : {total}")
    print(f"Completed      : {completed}")
    print(f"Pending        : {pending}")
    print(f"High priority  : {high} pending")

    if total > 0:
        rate = (completed / total) * 100
        print(f"Completion rate: {rate:.1f}%")

def get_id_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Enter a valid ID number!")

def main():
    print("================================")
    print("      TASK MANAGER CLI ✅        ")
    print(f"      {date.today()}             ")
    print("================================")

    # Add sample tasks
    add_task("Learn Flask basics",
             "high", "coding")
    add_task("Practice English",
             "high", "english")
    add_task("Push to GitHub",
             "high", "coding")
    add_task("Read about PostgreSQL",
             "medium", "coding")
    add_task("Create Upwork account",
             "medium", "freelance")
    add_task("Set up Wise account",
             "low", "freelance")

    while True:
        print("\n=== MENU ===")
        pending = sum(1 for t in tasks
                     if t["status"] == "pending")
        print(f"Pending tasks: {pending}")
        print("")
        print("1. Show all tasks")
        print("2. Show pending only")
        print("3. Show completed only")
        print("4. Show high priority")
        print("5. Add new task")
        print("6. Complete a task")
        print("7. Delete a task")
        print("8. Statistics")
        print("9. Exit")

        choice = input("\nChoose (1-9): ").strip()

        if choice == "1":
            show_tasks()
        elif choice == "2":
            show_tasks(filter_status="pending")
        elif choice == "3":
            show_tasks(filter_status="completed")
        elif choice == "4":
            show_tasks(filter_priority="high")
        elif choice == "5":
            title = input("Task title: ")
            print("Priority: low / medium / high")
            priority = input("Priority: ").strip()
            category = input("Category: ").strip()
            add_task(title, priority, category)
        elif choice == "6":
            show_tasks(filter_status="pending")
            task_id = get_id_input("Task ID: ")
            complete_task(task_id)
        elif choice == "7":
            show_tasks()
            task_id = get_id_input("Task ID: ")
            delete_task(task_id)
        elif choice == "8":
            show_statistics()
        elif choice == "9":
            print("\n✅ Stay productive Buddha!")
            print("Remote job is coming! 💪")
            break
        else:
            print("❌ Invalid! Choose 1-9")

main()