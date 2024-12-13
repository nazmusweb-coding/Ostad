import save_all_books
from datetime import datetime, timedelta

def lent_books(all_books, all_lent_books):
    search_book = input("Enter Book Title to lend: ")
    for book in all_books:
        if book["title"].lower() == search_book.lower():
            borrower_name = input("Enter Your Name: ")
            borrower_phone = input("Enter Your Phone no: ")

            # Check if the user has already borrowed the same book by the same writer
            already_borrowed = any(
                lent_books["title"].lower() == search_book.lower() and
                lent_books["author"].lower() == book["author"].lower() and
                lent_books["borrower_name"].lower() == borrower_name.lower()
                for lent_books in all_lent_books
            )

            if already_borrowed:
                print("You have already borrowed this book from the same writer.")
                return
            elif book["quantity"] <= 0:
                print("There are not enough books available to lend.")
                return

            # Generate lending details
            lend_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            return_due_date = (datetime.now() + timedelta(days=40)).strftime("%d-%m-%Y %H:%M:%S")

            # Add the lending record
            all_lent_books.append({
                "title": book["title"],
                "author": book["author"],
                "borrower_name": borrower_name,
                "borrower_phone": borrower_phone,
                "lend_date": lend_date,
                "return_due_date": return_due_date
            })

            # Reduce the stock in all_books
            book["quantity"] -= 1
            book["bookLastUpdatedAt"] = lend_date
            print(f"Book '{book['title']}' by {book['author']} has been lent to {borrower_name}. Due date: {return_due_date}.")

            # Save updates to files
            save_all_books.save_all_books(all_books)
            save_all_books.save_lent_books(all_lent_books)
            return all_lent_books

    print("Book not found or out of stock.")
