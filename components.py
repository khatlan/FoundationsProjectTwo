# CLASSES AND METHODS
class Store():

    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name = name
        self.products = []
    
        # your code goes here!

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        self.products.append(product)
        # your code goes here!

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        for item in products:
            print item


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return "(%s, %s, %d)" % (self.name, self.description, self.price)   
        # your code goes here!

class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        cart_list = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        cart_list.append(product)
        # your code goes here!

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        total = 0
        for item in cart_list:
            total = total + item(price)
        return total

        # your code goes here!

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        for item in cart_list:
            print item
        print (" your total is: %d") % (get_total_price())
        # your code goes here!

    def checkout(self):
        """
        Does the checkout.
        """
        print_receipt()
        x = raw_input("please confirm your order by typing Yes/No")
        if x == "Yes":
            print ("order is confirmed")
        elif x == "No":
            print ("order is cancelled")
        else: 
            print("Error")

        # your code goes here!
