import save_all_books
from datetime import datetime

def return_books(all_books, all_lent_books):
    borrower_name = input("Enter Your Name: ")
    borrower_phone = input("Enter Your Phone no: ")

    # Filter books borrowed by the user
    user_books = [book for book in all_lent_books if book["borrower_name"].lower() == borrower_name.lower() and book["borrower_phone"] == borrower_phone]

    if not user_books:
        print("No books found for this user.")
        return

    print("Your borrowed books:")
    for idx, book in enumerate(user_books, start=1):
        print(f"{idx}. {book['title']} by {book['author']} (Due Date: {book['return_date']})")

    return_choice = int(input("Enter the number of the book you want to return: "))

    if 1 <= return_choice <= len(user_books):
        return_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        book_to_return = user_books[return_choice - 1]

        # Remove the book from lent_books
        all_lent_books.remove(book_to_return)

        # Update stock in all_books
        for book in all_books:
            if book["title"].lower() == book_to_return["title"].lower() and book["author"].lower() == book_to_return["author"].lower():
                book["quantity"] += 1
                book["bookLastUpdatedAt"] = return_date
                break

        print(f"Book '{book_to_return['title']}' by {book_to_return['author']} has been returned.")

        # Save updates to files
        save_all_books.save_all_books(all_books)
        save_all_books.save_lent_books(all_lent_books)
    else:
        print("Invalid choice.")