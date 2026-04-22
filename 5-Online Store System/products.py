# base class
class Product :
    def __init__(self, product_id, name, base_price) :
        if base_price < 0 :
            raise ValueError("Base price cannot be negative.")
        self.id = product_id
        self.name = name
        self.base_price = base_price
        
    def get_price(self) :
        return self.base_price
        
    def get_details(self) :
        return (
            f"[ ID : {self.id}] {self.name} |"
            f"Type : {self.__class__.__name__}" # returning the name of the class as a string at runtime
            f"Price : ${self.get_price():.2f}"
        )
            
    def __str__(self) :
        return self.get_details()
        
# child classes
class PhysicalProduct(Product) :
    def __init__(self, product_id, name, base_price, shipping_cost) :
        # passing the values up to the parent class to do the actual setup
        super().__init__(product_id, name, base_price)
        if shipping_cost < 0 :
            raise ValueError("Shipping cost cannot be negative.")
        self.shipping_cost = shipping_cost
        
    def get_price(self) :
        return self.base_price + self.shipping_cost
    
    def get_details(self) :
        return (
            f"[ID: {self.id}] {self.name} | Type: PhysicalProduct | "
            f"Base: ${self.base_price:.2f} + Shipping: ${self.shipping_cost:.2f} "
            f"= Total: ${self.get_price():.2f}"
        )
        
class DigitalProduct(Product) :
    def __init__(self, product_id, name, base_price) :
        super().__init__(product_id, name, base_price)
        
    def get_price(self) :
        return self.base_price
    
    def get_details(self) :
        return (
            f"[ID: {self.id}] {self.name} | Type: DigitalProduct | "
            f"Price: ${self.get_price():.2f}"
        )
        
class DiscountedProduct(Product) :
    def __init__(self, product_id, name, base_price, discount_percentage) :
        super().__init__(product_id, name, base_price)
        if not (0 <= discount_percentage <= 100) :
            raise ValueError("Discount percentage must be between 0 and 100.")
        self.discount_percentage = discount_percentage
        
    def get_price(self) :
        discount = self.base_price * (self.discount_percentage / 100)
        return self.base_price - discount
    
    def get_details(self) :
        return (
            f"[ID: {self.id}] {self.name} | Type: DiscountedProduct | "
            f"Base: ${self.base_price:.2f} | Discount: {self.discount_percentage}% "
            f"| Final Price: ${self.get_price():.2f}"
        )
        
class SubscriptionProduct(Product) :
    def __init__(self, product_id, name, duration_in_months, monthly_fee) :
        if monthly_fee < 0 :
            raise ValueError("Monthly fee cannot be negative.")
        if duration_in_months <= 0 :
            raise ValueError("Duration in months cannot be zero or less.")
        super().__init__(product_id, name, base_price = 0)
        self.duration_in_months = duration_in_months
        self.monthly_fee = monthly_fee
        
    def get_price(self) : 
        return self.duration_in_months * self.monthly_fee
    
    def get_details(self) :
        return (
            f"[ID: {self.id}] {self.name} | Type: SubscriptionProduct | "
            f"{self.duration_in_months} months × ${self.monthly_fee:.2f}/mo "
            f"= Total: ${self.get_price():.2f}"
        )
