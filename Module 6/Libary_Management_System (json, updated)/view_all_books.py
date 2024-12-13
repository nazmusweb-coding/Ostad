import json

def view_all_books(all_books):
    with open("all_books.json", "r") as fp:
        all_books = json.load(fp)

        if all_books != []:
            for book in all_books:
                print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']} | Book Added At: {book['bookAddedAt']} | Book Last Updated At: {book['bookLastUpdatedAt']}")
        else:
            print("No Book found.")

def view_all_lent_books(all_books):
    with open("all_lent_books.json", "r") as fp:
        all_books = json.load(fp)

        if all_books != []:
            for book in all_books:
                print(f"Title: {book['title']} | Author: {book['author']} | Borrower Name: {book['borrower_name']} | Borrower Phone No: {book['borrower_phone']} | Lent Date: {book['lend_date']} | Return Due Date: {book['return_due_date']}")
        else:
            print("No Book found.")