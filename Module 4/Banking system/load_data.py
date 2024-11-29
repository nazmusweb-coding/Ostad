import os

def load_account():
    if os.path.exists("account.csv"):
        with open("account.csv", "r") as file:
            data = file.readline().strip().split(", ")
            user_name = data[0]
            balance = float(data[1])
            return {"user_name": user_name, "balance": balance}
    else:
        # Default user info
        print("No account data found. Creating a new account...")
        user_name = input("Enter your name: ")
        return {"user_name": user_name, "balance": 1000.00}  # Initial balance set to $1000
