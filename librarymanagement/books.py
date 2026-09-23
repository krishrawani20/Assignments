books = []
def add_books(book):
    books.append(book)
    return "Book Added Successfully..."

def search_book(book):
    if book in books:
        return "Book Found"
    else:
        return " Book Not Found"
    
def display_books():
    if len(books) == 0:
        return "No Book present"
    else:
        print("\n Avaliable books")
        for book in books:
            
            return book
        
    
