from Library import Library

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
                "\n5. Search book by id",
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
                    book = library.add_new_book(title,author)
                    if book:
                        print(f"✅ Book added successfully! [ ID : {book.id} ]")
                    else:
                        print(f"❌ Book '{title}' by {author} already exists!")
                    
            case '2' : 
                name = input("Enter user name : ").strip()
                if name :
                    user = library.register_new_user(name)
                    if user:
                        print(f"✅ User added successfully! [ ID : {user.id} ]")
                    else:
                        print(f"❌ User '{name}' already exists!")
                    
            case '3' : 
                print(library.display_books())
                
            case '4' : 
                print(library.display_users())
                
            case '5' :
                try :
                    book_id = int(input("Enter Book ID to search : ").strip())
                    book = library.find_book_by_id(book_id)
                    if book :
                        print(f"✅ Found : {book}")
                    else :
                        print(f"❌ Book with ID '{book_id}' not found!")
                except ValueError : 
                    print("❌ Please enter a valid numerical ID.")
                        
            case '6' :
                user_name = input("Enter your name : ").strip()
                user = library.find_user_by_name(user_name)
                if not user :
                    print("❌ User not found! Please register first.")
                    continue
                try :
                    book_id = int(input("Enter Book ID to borrow : ").strip())
                    book = library.find_book_by_id(book_id)
                    if book and user.borrow_book(book) :
                        print(f"✅ {user.name} successfully borrowed '{book.title}'")
                    else :
                        print("❌ Book is not available or ID not found!")
                except ValueError :
                    print("❌ Please enter a valid numerical ID.")
                    
            case '7' :
                user_name = input("Enter your name : ").strip()
                user = library.find_user_by_name(user_name)
                if not user :
                    print("❌ User not found! Please register first.")
                    continue
                try :
                    book_id = int(input("Enter Book ID to return : ").strip())
                    book_to_return = next((b for b in user.borrowed_books if b.id == book_id), None)
                    if book_to_return and user.return_book(book_to_return) :
                        print(f"✅ {user.name} successfully returned '{book_to_return.title}'")
                    else :
                        print("❌ You don't have this book ID borrowed!")
                except ValueError :
                    print("❌ Please enter a valid numerical ID.")
                    
            case '8' :
                user_name = input("Enter user name : ").strip()
                if user_name :
                    user = library.find_user_by_name(user_name)
                    if user :
                        print(f"\n 📖 Books borrowed by {user.name} :")
                        if not user.borrowed_books :
                            print("No books borrowed yet.")
                        else :
                            for book in user.borrowed_books :
                                print(f"{book}")
                    else :
                        print(f"❌ User '{user_name}' not found!")
                    
            case '9' :
                print("\n👋 Thank you for using the library management system! Bye~")
                break
            
            case _ :
                print("❌ Invalid choice! Please enter a number between 1 to 9 : ")
                
main()