from Book import Book
from User import User

# library class
class Library : 
    def __init__(self) : 
        self.books = []
        self.users = []
        
    def add_new_book(self, title, author) :
        for book in self.books : 
            if book.title.lower() == title.lower() and book.author.lower() == author.lower() :
                # returning none instead of printing
                return None
        #creating a new book object
        new_book = Book(title, author)
        self.books.append(new_book)
        # returning the book added instead of printing a message
        return new_book
    
    # helper methods added 
    def find_user_by_name(self, name) : 
        for user in self.users :
            if user.name.lower() == name.lower() :
                return user
        return None
    
    def find_book_by_id(self, book_id: int) :
        for book in self.books :
            if book.id == book_id :
                return book
        return None
    
    def register_new_user(self, name) :
        if self.find_user_by_name(name) : 
            return None
        # creating a user object
        new_user = User(name)
        self.users.append(new_user)
        return new_user
    
    
    def display_books(self):
        if not self.books:
            return "No books in the library yet."
        
        # returning a list instead of printing
        output = ["\n 📚 All Books :"]
        for book in self.books:
            output.append(str(book))
        return "\n".join(output)

    def display_users(self):
        if not self.users:
            return "No users registered yet."
            
        output = ["\n 👥 All Users :"]
        for user in self.users:
            output.append(str(user))
        return "\n".join(output)