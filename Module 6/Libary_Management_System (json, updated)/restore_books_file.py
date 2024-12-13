import json

def restore_all_books(all_books):
    with open("all_books.json", "r") as fp:
        all_books = json.load(fp)
    return all_books

def restore_lent_books(all_books):
    with open("all_lent_books.json", "r") as fp:
        lent_books = json.load(fp)
    return lent_books