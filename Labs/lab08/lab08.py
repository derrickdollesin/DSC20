"""
DSC 20 Winter 2024 Lab 08
Name: TODO
PID: TODO
Source: TODO
"""

# Question 1
def q1_answers():
    """
    Write your answers to the question in the list

    >>> ans = q1_answers()
    >>> isinstance(ans, list)
    True
    >>> all(isinstance(elem, int) and 1 <= elem <= 9 for elem in ans)
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (1-9)
    return [...]

# Question 2
# TODO: Uncomment structure below and fix the code
#class Item:
    """
    >>> p = Item("Magic Wand", 50, 100)
    >>> p.name
    'Magic Wand'
    >>> p.price
    50
    >>> p.stock
    100
    >>> p.display_item_info()
    'Magic Wand - Price: $50, Stock: 100'
    >>> p.apply_discount(10)
    >>> p.price
    45.0
    >>> p.reduce_stock(20)
    >>> p.stock
    80
    >>> ep = EnchantedItem("Enchanted Shield", 150, 50, 3)
    >>> ep.apply_magical_boost(17)
    >>> ep.enchantment_level
    20
    >>> ep.display_item_info()
    'Enchanted Shield - Price: $150, Stock: 50, Enchantment Level: 20'
    >>> ep.set_discount(10)
    >>> ep.price
    121.5
    """
    #def __init__(self, name, price, stock):
    #    self.name = name
    #    self.price = price
    #    self.stock = stock

    #def display_item_info(self):
    #    return f"{name} - Price: ${price}, Stock: {stock}"

    #def apply_discount(self, discount_percent):
    #    """
    #    Applies a discount to the item's price.
    #    """
    #    price -= (discount_percent / 100) * price

    #def reduce_stock(self, quantity):
    #    """
    #    Reduces the stock of the item by the given quantity.
    #    If the quantity is greater than the current stock, set the stock to 0.
    #    """
    #    stock = max(0, stock - quantity)

    #def restock(self, quantity):
    #    """
    #    Increases the stock of the item by the given quantity.
    #    """
    #    stock += quantity

#class EnchantedItem(Item):

    #def __init__(self, name, price, stock, enchantment_level):
    #    super(name, price, stock)
    #    enchantment_level = enchantment_level

    #def apply_magical_boost(self, boost_factor):
    #    """
    #    Applies a magical boost to the item's enchantment level.
    #    """
    #    enchantment_level += boost_factor

    #def display_item_info(self):
    #    """
    #    Displays information about the enchanted item, including its 
    #        enchantment level.
    #    """
    #    basic_info = display_item_info()
    #    return f"{basic_info}, Enchantment Level: {enchantment_level}"

    #def set_discount(self, discount_percent):
    #    """
    #    Applies a discount to the enchanted item's price, with an 
    #    additional enchantment bonus. Applies the regular discount 
    #       first and then calculates the bonus discount. 
    #    """
    #    super().
    #    bonus_discount = enchantment_level / 2
    #    price -= (bonus_discount / 100) * price



# Question 3
class Product:
    """
    >>> plush_toy = Product(product_id=0, name="Toy Plushie", price=25, \
        quantity=50)
    >>> plush_toy.product_id
    0
    >>> plush_toy.get_product_description()
    Product ID: 0, Name: Toy Plushie, Price: $25.00, Quantity Available: 50
    >>> laptop = ElectronicProduct(product_id=1, name="Laptop", price=1000, \
        warranty_period="2 years", quantity=200)
    >>> laptop.product_id
    1
    >>> laptop.name
    'Laptop'
    >>> laptop.price
    1000
    >>> laptop.warranty_period
    '2 years'
    >>> laptop.get_product_description()
    Product ID: 1, Name: Laptop, Price: $1000.00, Quantity Available: 200
    Warranty: 2 years
    >>> shirt = ClothingProduct(product_id=2, name="Casual Shirt", price=30, \
        size="M", quantity=550)
    >>> shirt.size
    'M'
    >>> shirt.quantity
    550
    >>> shirt.get_product_description()
    Product ID: 2, Name: Casual Shirt, Price: $30.00, Quantity Available: 550
    Size: M
    """
    pass

class ShoppingCart:
    """
    Implementation of ShoppingCart Class and subclasses.
    
    >>> laptop = ElectronicProduct(product_id=1, name="Laptop", price=1000, \
        warranty_period="2 years", quantity=200)
    >>> shirt = ClothingProduct(product_id=2, name="Casual Shirt", price=30, \
        size="M", quantity=550)
    >>> cart = ShoppingCart()
    >>> laptop.quantity
    200
    >>> cart.add_to_cart(laptop)
    >>> laptop.quantity
    199
    >>> cart.add_to_cart(shirt)
    >>> cart.display_cart()
    Shopping Cart:
    Product ID: 1, Name: Laptop, Price: $1000.00, Quantity Available: 199
    Warranty: 2 years
    Product ID: 2, Name: Casual Shirt, Price: $30.00, Quantity Available: 549
    Size: M
    >>> cart.calculate_total()
    1030.0
    >>> discounted_cart = DiscountedShoppingCart(discount_percentage=10)
    >>> discounted_cart.add_to_cart(laptop)
    >>> discounted_cart.add_to_cart(shirt)
    >>> discounted_cart.apply_discount()
    >>> discounted_cart.display_cart()
    Shopping Cart:
    Product ID: 1, Name: Laptop, Price: $900.00, Quantity Available: 198
    Warranty: 2 years
    Product ID: 2, Name: Casual Shirt, Price: $27.00, Quantity Available: 548
    Size: M
    >>> discounted_cart.calculate_total()
    927.0
    """
    pass 