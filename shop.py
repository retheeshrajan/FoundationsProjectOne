####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Get Baked"#complete me!
signature_flavors = ["tuna","salmon","red herring"]#complete me!
order_list = []
listCnt=0


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print ("Our menu:")
    for k,v in menu.items():
        print ("- " + k + " (KD " + str(v) + ")")

def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    for fl in original_flavors:
    	print ("- " + fl)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for sg in signature_flavors:
    	print ("- " + sg)

def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    proceed=1
    if order.lower() not in original_flavors:
        proceed=0
    else:
        proceed=1
    
    if proceed==0 and order.lower() not in signature_flavors:
        proceed=0
    else:
        proceed=1

    if proceed==0 and order.lower() not in menu:
        proceed=0
    else:
        proceed=1
    
    return proceed

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    #order_list = []
    listCnt=0
    inp=str(input())

    #print (is_valid_order(inp))
    if inp=="Exit":
        print_order(order_list)
        #return order_list
    else:
        if is_valid_order(inp)==1:
            order_list.insert(listCnt,inp)
            listCnt+=1
            get_order()
        else:
            print ("The item doesn't exists in our menu. Please check the spelling or go through the menu list. Thank you.")
            get_order()
    
def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total>=5:
    	print ("This order is eligible for credit card payment")
    else:
    	print ("Total amount must be above 5 KD for credit card payment")


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for tl in order_list:
        for k,v in menu.items():
            if tl==k:
                total=total+v
        for fl in original_flavors:
            if tl==fl:
                total=total+original_price
        for sg in signature_flavors:
            if tl==sg:
                total=total+signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    #print (order_list)
    for ord in order_list:
        print ("- " + ord)
    
    print ("")
    print ("That\'ll be KD " + str(get_total_price(order_list)))
    accept_credit_card(get_total_price(order_list))
    print ("Thank you for shopping at " + cupcake_shop_name)