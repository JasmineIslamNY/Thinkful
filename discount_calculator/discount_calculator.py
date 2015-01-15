import argparse

def calculate_discount(item_cost, relative_discount, absolute_discount):
    """
    Calculate the discounted price of item given the item cost, 
    a relative discount, and an additional price discount
    """
    item_cost = float(item_cost)
    relative_discount = float(relative_discount)
    absolute_discount = float(absolute_discount)
    
    if relative_discount < 1:
        relative_discount *= 100
    
    discounted_price = (item_cost - (item_cost * (relative_discount / 100)) - absolute_discount)
    
    if discounted_price < 0:
        discounted_price = 0
        
    #trying to get rid of extra digits
    discounted_price *= 100
    discounted_price = int(discounted_price)
    discounted_price /= 100.00

    return discounted_price

def validate_entry(entry):
    """ Validate for positive number or 0 """
    try:
        entry = float(entry)
        if (entry < 0):
            entry = -1
    except TypeError: 
        entry = -1
    return entry

def make_parser():
    """ Construct the command line parser """
    description = "This app allows you to enter a cost and discounts to get the discounted price"
    parser = argparse.ArgumentParser(description = description)
    parser.add_argument("Cost", help="The cost before discount")
    parser.add_argument("Percentage", help="Enter the % discount without the % sign, e.g. 10 for 10%")
    parser.add_argument("Dollar", help="Enter the $ discount without the $ sign, e.g. 20 for $20")
    return parser
        
def get_amounts():
    """ This will get the cost and discounts from the user if CLI inputs are invalid """
    print "Some of your entries were invalid, please re-enter..."
    item_cost = raw_input("Please enter how much the item cost: ")
    relative_discount = raw_input("Please enter the discount amount: ")
    absolute_discount = raw_input("Please enter the $ amount discount: ")
    
    return item_cost, relative_discount, absolute_discount


def discount_calculator(item_cost, relative_discount, absolute_discount):
    cost = validate_entry(item_cost)
    relative = validate_entry(relative_discount)
    absolute = validate_entry(absolute_discount)
    
    if (cost == -1 or relative == -1 or absolute == -1):
        print "Invalid number entered for cost and/or discount"
        raise ValueError("Invalid entry")
        # return -1 - in production would remove the ValueError and just prompt user to reinput values
    else:
        discounted_price = calculate_discount(cost, relative, absolute)
        print "Discounted price is ${:.2f}".format(discounted_price)
        return discounted_price

def main():
    parser = make_parser()
    args = parser.parse_args()
    item_cost = args.Cost
    relative_discount = args.Percentage
    absolute_discount = args.Dollar
    
    discounted_price = discount_calculator(item_cost, relative_discount, absolute_discount)
    
    if discounted_price == -1:
        item_cost, relative_discount, absolute_discount = get_amounts()
        discounted_price = discount_calculator(item_cost, relative_discount, absolute_discount)
    
    return discounted_price

if __name__ == "__main__":
    main()