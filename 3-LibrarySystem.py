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
            

# library class
class Library : 
    def __init__(self) : 
        self.books = []
        self.users = []
        
    def add_new_book(self, title, author) :
        for book in self.books : 
            if book.title.lower() == title.lower() and book.author.lower() == author.lower() :
                print(f"❌ Book '{title} by {author} already exists!")
                return False
        #creating a new book object
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"✅ Book added successfully! [ ID : {new_book.id} ]")
        return True
        
        
    def register_new_user(self, name) :
        for user in self.users :
            if user.name.lower() == name.lower() :
                print(f"❌ User '{name}' already exists!")
                return False
            
        # creating a user object
        new_user = User(name)
        self.users.append(new_user)
        print(f"✅ User added successfully! [ ID : {new_user.id} ]")
        return True
    
    def display_books(self) :
        print("\n 📚 All Books :\n")
        if not self.books : 
            print("No books in the library yet.")
            return 
        for book in self.books :
            print(f"{book}")
    
    def display_users(self) :
        print("\n 👥 All Users :\n")
        if not self.users :
            print("No users registered yet.")
            return
        for user in self.users :
            print(f"{user}")
            
    def search_book_by_title(self, title) :
        for book in self.books :
            if book.title.lower() == title.lower() :
                return book
        return None
    
    def show_books_borrowed_by_user(self, user_name) : 
        for user in self.users : 
            if user.name.lower() == user_name.lower() :
                print(f"\n 📖 Books borrowed by {user.name} : ")
                if not user.borrowed_books :
                    print("No books borrowed yet.")
                else :
                    for book in user.borrowed_books :
                        print(f"{book}\n")
                return
        print(f"❌ User '{user_name}' not found!")
        
def main() :
    library = Library()
    print("\n🌼 Welcome to library management system!")
    
    while True :
        print("\n"+"="*50)
        print("📌 MENU : ")
        print("="*50)
        print("\n1. Add a new book",
                "\n2. Register a new user",
                "\n3. Display all books",
                "\n4. Display all users",
                "\n5. Search book by title",
                "\n6. Borrow a book",
                "\n7. Return a book",
                "\n8. Show books borrowed by a specific user",
                "\n9. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice [1-9] : ").strip()
        
        match choice :
            case '1' : 
                title = input("Enter the book title : ").strip()
                author = input("Enter the author of the book : ").strip()
                if  title and author : 
                    library.add_new_book(title,author)
                    
            case '2' : 
                name = input("Enter user name : ").strip()
                if name :
                    library.register_new_user(name)
                    
            case '3' : 
                library.display_books()
                
            case '4' : 
                library.display_users()
                
            case '5' :
                title = input("Enter the title to search : ").strip()
                if title :
                    book = library.search_book_by_title(title)
                    if book :
                        print(f"✅ Found : {book}")
                    else :
                        print(f"❌ Book '{title}' not found!")
                        
            case '6' :
                user_name = input("Enter your name : ").strip()
                title = input("Enter book title to borrow : ").strip()
                
                # finding the user to make sure they are registered
                user = None
                for u in library.users : 
                    if u.name.lower() == user_name.lower() :
                        user = u
                        break
                if not user : 
                    print("❌ User not found! Please register first.")
                    continue
                
                # finding the book
                book = library.search_book_by_title(title)
                if not book :
                    print("❌ Book not found!")
                    continue
                
                if user.borrow_book(book) : 
                    print(f"✅ {user.name} successfully borrowed '{book.title}'")
                else :
                    print("❌ Book is not available")
                    
            case '7' :
                user_name = input("Enter your name : ").strip()
                title = input("Enter book title to return : ").strip()
                
                user = None
                for u in library.users : 
                    if u.name.lower() == user_name.lower() :
                        user = u
                        break
                if not user : 
                    print("❌ User not found! Please register first.")
                    continue
                
                book_to_return = None
                for b in user.borrowed_books :
                    if b.title.lower() == title.lower() :
                        book_to_return = b
                        break
                
                if book_to_return and user.return_book(book_to_return) :
                    print(f"✅ {user.name} successfully returned '{book_to_return}'")
                else :
                    print("❌ You don't have this book borrowed!")
                    
            case '8' :
                user_name = input("Enter user name : ").strip()
                if user_name :
                    library.show_books_borrowed_by_user(user_name)
                    
            case '9' :
                print("\n👋 Thank you for using the library management system! Bye~")
                break
            
            case _ :
                print("❌ Invalid choice! Please enter a number between 1 to 9 : ")
                
main()