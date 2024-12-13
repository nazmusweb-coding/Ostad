import json

def save_all_books(all_books):
    with open("all_books.json", "w") as fp:
        json.dump(all_books, fp, indent=4)

def save_lent_books(lent_books):
    with open("all_lent_books.json", "w") as fp:
        json.dump(lent_books, fp, indent=4)
