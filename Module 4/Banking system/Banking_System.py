import deposit
import withdraw
import view_balance
import save_data
import load_data

# Load existing data
account = load_data.load_account()

while True:
    print(f"\nWelcome to the Banking Management System! Please select an option:")
    print("Menu ID=0. Exit.")
    print("Menu ID=1. Deposit Money.")
    print("Menu ID=2. Withdraw Money.")
    print("Menu ID=3. Check Balance.")

    menu = input("\nSelect any Number: ")

    if menu == "1":
        account = deposit.deposit(account)

    elif menu == "2":
        account = withdraw.withdraw(account)

    elif menu == "3":
        view_balance.view_balance(account)

    elif menu == "0":
        print(f"\nThanks for using our Banking Management System!")
        save_data.save_account(account)  # Save data when exiting
        break

    else:
        print("Please select a valid number.")
