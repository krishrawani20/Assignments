issued_books = {}

def issue_book(book, member):

    if book in issued_books:
        print("Book Already Issued")
    else:
        issued_books[book] = member
        print("Book Issued Successfully")

def return_book(book):

    if book in issued_books:
        del issued_books[book]
        print("Book Returned Successfully")
    else:
        print("Book Was Not Issued")

def display_issued():

    if len(issued_books) == 0:
        print("No Books Issued")

    else:
        print("\nIssued Books")

        for book, member in issued_books.items():
            print(book, "->", member)