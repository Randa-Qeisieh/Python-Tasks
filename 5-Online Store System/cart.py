from products import Product

class Cart :
    def __init__(self) :
        # to store product_id : { "product" : product, "quantity" : int}
        self._items = {}
        
    def add_products(self, product, quantity) :
        if quantity <= 0 :
            raise ValueError("Quantity must be a positive integer.")
        if product.id in self._items :
            self._items[product.id]["quantity"] += quantity
        else :
            self._items[product.id] = {"product" : product, "quantity" : quantity}
            
    def remove_product(self, product_id, quantity) :
        if product_id not in self._items :
            raise ValueError(f"Product ID '{product_id}' is not in the cart.")
        if quantity <= 0 :
            raise ValueError("Quantity to remove must be a positive integer.")
        
        current_qty = self._items[product_id]["quantity"]
        if quantity >= current_qty :
            del self._items[product_id]
        else :
            self._items[product_id]["quantity"] -= quantity
            
    def clear(self) :
        self._items.clear()
        
    def get_total(self) :
        total = 0
        for item in self._items.values() :
            total += item["product"].get_price() * item["quantity"]
        return total
    
    def get_items(self) :
        return list(self._items.values())
    
    def is_empty(self) :
        return len(self._items) == 0
    
    def get_cart_summary(self) :
        if self.is_empty() :
            return "Your cart is empty."
        lines = ["=" * 50, f"{'CART CONTAINS':^55}", "=" * 50]
        for item in self._items.values() :
            product = item["product"]
            qty = item["quantity"]
            subtotal = product.get_price() * qty
            lines.append(
                # styling for alignment
                f"{product.name[:28]:<28} x {qty:<4} ${subtotal:>8.2f}"
            )
        lines.append("-" * 50)
        lines.append(f"{'TOTAL':<32} ${self.get_total():>8.2f}")
        lines.append("=" * 50)
        return "\n".join(lines)