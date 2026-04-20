# book class
class Book :
    # generating unique ids automatically
    id_counter = 0
    def __init__(self, title, author) :
        Book.id_counter += 1
        self.id = Book.id_counter
        self.title = title
        self.author = author
        self.available = True 
        
    def mark_as_borrowed(self) :
        # a user can borrow a book only if it's available
        if self.available : 
            self.available = False
            return True
        return False # already borrowed
        
    def mark_as_returned(self) :
        self.available = True 
        
    def __str__(self) : 
        status = "Available" if self.available else "Borrowed"
        return f"ID : {self.id} '{self.title}' by {self.author} - {status}"