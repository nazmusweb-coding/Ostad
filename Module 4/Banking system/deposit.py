from save_data import save_account


def deposit(account):
    amount = float(input("Enter the amount to deposit: $"))

    if amount > 0:
        account["balance"] += amount
        print(f"${amount} deposited successfully.")
        save_account(account)
    else:
        print("Error: Deposit amount must be greater than 0.")

    return account
