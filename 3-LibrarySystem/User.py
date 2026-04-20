# user class
class User :
    id_counter = 0
    
    def __init__(self, name) : 
        User.id_counter += 1
        self.id = User.id_counter
        self.name = name
        self.borrowed_books = []
        
    def borrow_book(self, book) :
        if book.mark_as_borrowed() :
            self.borrowed_books.append(book)
            return True
        return False
    
    def return_book(self, book) : 
        if book in self.borrowed_books :
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            return True
        return False
    
    def __str__(self) :
        if not self.borrowed_books :
            borrowed_info = "No books borrowed"
        else : 
            borrowed_info = ", ".join([b.title for b in self.borrowed_books])
        return f"ID : {self.id} User : {self.name} | Borrowed : {borrowed_info}"
