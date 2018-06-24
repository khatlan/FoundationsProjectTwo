# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "Khatlan E-shop"  

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    print("these are the stores") 
    for item in stores:
        print item.name
    # your code goes here!

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for item in stores:
        if item == store_name:
            return item.name
    else:
        return False


    # your code goes here!

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    
    k = raw_input("pick a store by typing the name of the store or typying checkout to finish and pay\n")
    if k == "checkout":
        Cart.checkout(cart_list)
    elif k == get_store(k):
        print get_store(store_name)
    else:

        print("invalid input try again")
        pick_store()

    # your code goes here!

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """

    # your code goes here!

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    print_stores()
    pick_store()
    pick_products()
    # your code goes here!

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
