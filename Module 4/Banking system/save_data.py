def save_account(account):
    with open("account.csv", "w") as file:
        file.write(f"{account['user_name']}, {account['balance']}\n")
