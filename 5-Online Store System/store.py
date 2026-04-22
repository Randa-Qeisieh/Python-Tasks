from cart import Cart

class StoreSystem :
    def __init__(self,) :
        self._products = {}
        self.cart = Cart()
        
    # helper functions
    def add_product(self, product) :
        if product.id in self._products :
            raise ValueError(f"Produce ID '{product.id}' already exits.")
        self._products[product.id] = product
        
    def remove_product(self, product_id) :
        if product_id not in self._products :
            raise KeyError(f"No product found with ID '{product_id}'")
        del self._products[product_id] 
        
    def find_product_by_id(self, product_id) :
        return self._products.get(product_id, None)
    
    def get_all_products(self) :
        return list(self._products.values())
    
    def add_to_cart(self, product_id, quantity) :
        product = self.find_product_by_id(product_id)
        if product is None :
            raise ValueError(f"No product found with ID '{product_id}'")
        self.cart.add_products(product, quantity)
        
    def remove_from_cart(self, product_id, quantity) :
        self.cart.remove_product(product_id, quantity)