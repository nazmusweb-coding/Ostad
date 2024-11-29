from save_data import save_account


def withdraw(account):
    amount = float(input("Enter the amount to withdraw: $"))

    if amount > 0:
        if amount <= account["balance"]:
            account["balance"] -= amount
            print(f"${amount} withdrawn successfully.")
            save_account(account)
        else:
            print("Error: Insufficient balance.")
    else:
        print("Error: Withdrawal amount must be greater than 0.")

    return account
