accounts = {
    "Alex": {
        "pin": "1234",
        "balance": 1500,
        "history": []
    },
    "Emma": {
        "pin": "5678",
        "balance": 2500,
        "history": []
    },
    "John": {
        "pin": "1111",
        "balance": 1000,
        "history": []
    }
}



def get_valid_number(prompt):
    while True:
        try:
            amount = float(input(prompt))

            if amount <= 0:
                print("Amount must be greater then 0.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")

def create_account():

    while True:
        username = input("Choose a username: ")

        if username in accounts:
            print("Username already exists!")
            continue

        break

    while True:
        pin = input("Create a 4-digit PIN: ")

        if len(pin) != 4 or not pin.isdigit():
            print("PIN must be exactly 4 digits!")
            continue

        break

    balance = get_valid_number("Initial Deposit: $")

    accounts[username] = {
        "pin": pin,
        "balance": balance,
        "history": ["Account Created"]
    }

    print("\nAccount created successfully!")
    print(f"Welcome, {username}!")

def login():
    while True:
        username = input("Username: ")
        pin = input("PIN: ")

        if username not in accounts:
            print("User not found!")
            continue

        if pin != accounts[username]["pin"]:
            print("Wrong PIN!")
            continue

        print("Loing Successful!")
        return username



def check_balance(username):
    print(f"Current Balance: ${accounts[username]["balance"]}")

def deposit(username):

    amount = get_valid_number("Deposit Amount: $")

    accounts[username]["balance"] += amount

    print("Deposit Successful!")
    accounts[username]["history"].append(f"Deposit Amount: ${amount}")
    print(f"New Balance: ${accounts[username]['balance']:.2f}")


def withdraw(username):
    amount = get_valid_number("Withdraw Amount: $")

    if amount > accounts[username]["balance"]:
        print("Insufficient Funds!")
        return

    accounts[username]["balance"] -= amount

    print("Withdraw SuccessFull")
    accounts[username]["history"].append(f"Withdraw Amount ${amount}")
    print(f"New Balance: ${accounts[username]['balance']}")

def change_pin(username):
    current_pin = input("Enter Current PIN: ")

    if current_pin != accounts[username]["pin"]:
        print("Incorrect Current PIN!")
        return

    while True:
        new_pin = input("Enter new 4-digit PIN: ").strip()

        if len(new_pin) != 4 or not new_pin.isdigit():
            print("PIN msut be exactly 4 digits.")
            continue

        confirm_pin = input("Confrim new PIN: ").strip()

        if confirm_pin != new_pin:
            print("PINs do not match!")
            continue
        break

    accounts[username]["pin"] = new_pin
    accounts[username]["history"].append(
        "PIN Changed"
    )
    print("PIN changed successfully!")


def account_details(username):
    print("\nAccount Details")

    print(f"Username: {username}")
    print(f"Balance: {accounts[username]['balance']}")
    print(f"PIN: {'*' * len(accounts[username]['pin'])}")

def transfer(username):
    while True:

        receiver = input("Transfer to: ").strip()

        if receiver not in accounts:
            print("User not found!")
            return

        if receiver == username:
            print("You cannot treansder money to yourself!")
            return

        amount = get_valid_number("Transfer Amount: ")

        if amount > accounts[username]["balance"]:
            print("Insufficient funds!")
            continue
        break

    accounts[username]["balance"] -= amount
    accounts[receiver]["balance"] += amount

    print("\nTransfer Successful!")
    accounts[username]["history"].append(
    f"Transferred: ${amount} to {receiver}"
    )
    accounts[receiver]["history"].append(
    f"Received: ${amount} from {username}"
    )
    print(f"Successfully transferred ${amount} to {receiver}")
    print(f"Your Balance: ${accounts[username]["balance"]}")


def transaction_history(username):

    print("\nTransaction History")

    history = accounts[username]["history"]

    if len(history) == 0:
        print("No Transactions found.")
        return

    for i, transaction in enumerate(history, start=1):
        print(f"{i}. {transaction}")

def account_summary(username):

    print("Account Summary")

    print(f"Username: {username}")
    print(f"Current Balance: ${accounts[username]['balance']:.2f}")
    print(f"PIN: {'*' * len(accounts[username]['pin'])}")

    total_transactions = len(accounts[username]["history"])
    print(f"Transactions: {total_transactions}")

    if total_transactions == 0:
        print("Last Transaction: None")
    else:
        print(f"Last Transaction: {accounts[username]['history'][-1]}")

print("")


def main():

    while True:

        print("\n====== BANK SYSTEM ======")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            username = login()
            menu(username)

        elif choice == "2":
            create_account()

        elif choice == "3":
            print("Thank you for using our bank!")
            break

        else:
            print("Invalid choice!")


def menu(username):

    while True:
        print("\n Bank Menu")
        print(f"Loggin in as: {username}")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Account Details")
        print("6. Transfer")
        print("7. Transaction History")
        print("8. Account Summary")
        print("9. Logout")

        choice = input("\nEnter Choice: ")

        if choice == "1":
            check_balance(username)

        elif choice == "2":
            deposit(username)

        elif choice == "3":
            withdraw(username)

        elif choice == "4":
            change_pin(username)

        elif choice == "5":
            account_details(username)

        elif choice == "6":
            transfer(username)

        elif choice == "7":
            transaction_history(username)

        elif choice == "8":
            account_summary(username)

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice.")


    username = login()
    menu(username)

main()