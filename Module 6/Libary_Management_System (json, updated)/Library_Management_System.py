import add_books
import view_all_books
import restore_books_file
import update_books
import remove_books
import lend_books
import return_books

all_books =[]
all_lent_books =[]


while True:
    print(f"\nWelcome to our Library Management System! Please select below menu ID")
    print("Menu ID=0. Exit.")
    print("Menu ID=1. Add Books.")
    print("Menu ID=2. Update your Book.")
    print("Menu ID=3. Remove a Select Book.")
    print("Menu ID=4. View All Books.")
    print("Menu ID=5. View All Lent Books.")
    print("Menu ID=6. Book Lend.")
    print("Menu ID=7. Book Return.")

    all_books = restore_books_file.restore_all_books(all_books)
    all_lent_books = restore_books_file.restore_lent_books(all_lent_books)

    menu = input(f"\nSelect any Number: ")

    if menu == "1":
       all_books = add_books.add_books(all_books)

    elif menu == "2":
        update_books = update_books.update_books(all_books)

    elif menu == "3":
        remove_books = remove_books.remove_books(all_books)

    elif menu == "4":
        view_all_books.view_all_books(all_books)

    elif menu == "5":
        view_all_books.view_all_lent_books(all_lent_books)

    elif menu == "6":
        all_lent_books = lend_books.lent_books(all_books, all_lent_books)

    elif menu == "7":
        return_books.return_books(all_books, all_lent_books)


    elif menu == "0":
        print(f"\nThanks for using our Library Management System!")
        break
        
    else:
        print("Please Select a Valid Number")





