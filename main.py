import json
from datetime import datetime

FILE = "data.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_transaction(data):
    print("\n--- Add Transaction ---")
    t_type = input("Type (income/expense): ").lower()
    amount = float(input("Amount: "))
    category = input("Category (food/rent/etc): ")
    
    transaction = {
        "type": t_type,
        "amount": amount,
        "category": category,
        "date": str(datetime.now())
    }
    
    data.append(transaction)
    save_data(data)
    print("Transaction saved!")

def view_summary(data):
    income = sum(t["amount"] for t in data if t["type"] == "income")
    expense = sum(t["amount"] for t in data if t["type"] == "expense")

    print("\n--- Summary ---")
    print("Total Income:", income)
    print("Total Expenses:", expense)
    print("Balance:", income - expense)

def view_all(data):
    print("\n--- All Transactions ---")
    for t in data:
        print(t)

def menu():
    print("\nPERSONAL FINANCE TRACKER")
    print("1. Add Transaction")
    print("2. View Summary")
    print("3. View All Transactions")
    print("4. Exit")

def main():
    data = load_data()

    while True:
        menu()
        choice = input("Select option: ")

        if choice == "1":
            add_transaction(data)
        elif choice == "2":
            view_summary(data)
        elif choice == "3":
            view_all(data)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

main()
