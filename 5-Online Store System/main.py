import feature_handlers as handlers
from store import StoreSystem
from utilities import get_int

MENU = """
╔═══════════════════════════════════╗
║       ONLINE STORE SYSTEM         ║
╠═══════════════════════════════════╣
║  1. Add a new product             ║
║  2. Display all products          ║
║  3. Search product by ID          ║
║  4. Add product to cart           ║
║  5. Remove product from cart      ║
║  6. View cart                     ║
║  7. Calculate total price         ║
║  8. Clear cart                    ║
║  0. Exit                          ║
╚═══════════════════════════════════╝ """

def main() :
    store = StoreSystem()
    
    while True : 
        print(MENU)
        choice = get_int("Select an option :  ", 0, 8)
        
        if choice == 0 :
            print("  \n Goodbye!~  \n")
            break
        
        match choice : 
            case 1: handlers.handle_add_product(store)
            case 2: handlers.handle_display_all(store)
            case 3: handlers.handle_search(store)
            case 4: handlers.handle_add_to_cart(store)
            case 5: handlers.handle_remove_from_cart(store)
            case 6: handlers.handle_view_cart(store)
            case 7: handlers.handle_total(store)
            case 8: handlers.handle_clear_cart(store)
            
if __name__ == "__main__" : 
    main()
