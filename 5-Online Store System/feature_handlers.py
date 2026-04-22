from utilities import get_int, get_float, get_nonempty, header, divider
from products import PhysicalProduct, DigitalProduct, SubscriptionProduct, DiscountedProduct
from store import StoreSystem

def handle_add_product(store) :
    header("ADD NEW PRODUCT")
    print("Select product type : ",
        " 1. Physical Product ",
        "   2. Digital Product ",
        "   3. Discounted Product",
        "   4. Subscription Product")
    divider()
    
    choice = get_int(" Enter Your Choice [ 1 - 4 ] : ", 1, 4)
    
    product_id = get_nonempty("  Product ID :")
    if store.find_product_by_id(product_id) is not None :
        print(f" Product ID '{product_id}' already exists.")
        return
    
    name = get_nonempty("  Product Name :  ")
    
    try :
        if choice == 1 :
            base_price = get_float("  Base Price ($) : ", 0)
            shipping = get_float("  Shipping Cost ($) : ", 0)
            product = PhysicalProduct(product_id, name, base_price, shipping)
            
        elif choice == 2 :
            base_price = get_float("  Price ($) : ", 0)
            product = DigitalProduct(product_id, name, base_price)
            
        elif choice == 3 :
            base_price = get_float("  Base Price ($) : ", 0)
            discount = get_float("  Discount percentage ( 0 - 100 ) : ", 0, 100)
            product = DiscountedProduct(product_id, name, base_price, discount)
            
        elif choice == 4 :
            duration = get_int("  Duration ( months ) : ", 1)
            monthly = get_float("  Monthly fee ($) : ", 0)
            product = SubscriptionProduct(product_id, name, duration, monthly)
            
        store.add_product(product)
        print(f"\n '{name}' added successfully.")
            
    except ValueError as e: 
        print(f"\n Error : {e}")
        
        
def handle_display_all(store) :
    header("ALL PRODUCTS")
    products = store.get_all_products()
    if not products : 
        print("  No products in the store yet.")
        return
    for p in products :
        print(f"  {p.get_details()}")
        

def handle_search(store) :
    header("SEARCH PRODUCT BY ID")
    product_id = get_nonempty("  Enter product ID : ")
    product = store.find_product_by_id(product_id)
    if product : 
        print(f"\n Found : \n {product.get_details()}")
    else :
        print(f" No product found with ID '{product_id}'")
        

def handle_add_to_cart(store) : 
    header("ADD PRODUCT TO CART")
    product_id = get_nonempty("  Enter product ID : ")
    quantity = get_int("  Quantity : ", 1)
    try : 
        store.add_to_cart(product_id, quantity)
        product = store.find_product_by_id(product_id)
        print(f"  Added '{quantity}' '{product_id}' to cart.")
    except (KeyError, ValueError) as e:
        print(f"  {e}")
        
def handle_remove_from_cart(store) :
    header("REMOVE FROM CART")
    if store.cart.is_empty() :
        print("  Your cart is already empty.")
        return
    product_id = get_nonempty("  Enter product ID : ")
    quantity = get_int("  Enter quantity to remove : ", 1)
    try : 
        store.remove_from_cart(product_id, quantity)
        print(f"  Removed {quantity} unit(s) of product '{product_id}' from cart.")
    except (KeyError, ValueError) as e:
        print(f"  {e}")
        
def handle_view_cart(store):
    header("VIEW CART")
    print(store.cart.get_cart_summary())


def handle_total(store):
    header("CART TOTAL")
    if store.cart.is_empty():
        print("  Your cart is empty — nothing to total.")
    else:
        print(f"  Total price: ${store.cart.get_total():.2f}")


def handle_clear_cart(store):
    header("CLEAR CART")
    if store.cart.is_empty():
        print("  Cart is already empty.")
        return
    confirm = input("  Are you sure? (yes/no): ").strip().lower()
    if confirm == "yes":
        store.cart.clear()
        print("  ✓ Cart cleared.")
    else:
        print("  Cancelled.")