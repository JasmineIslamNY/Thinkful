import argparse
import sys

def calculate_discount(item_cost, relative_discount, absolute_discount):
    """
    Calculate the discounted price of item given the item cost, 
    a relative discount, and an additional price discount
    """
    discounted_price = item_cost - (item_cost * relative_discount) - absolute_discount 
    
    if discounted_price < 0:
        discounted_price = 0
        
    return discounted_price

def validate_entry(entry):
    """ Validate for positive number or 0 """
    try:
        float(entry)
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
    item_cost = validate_entry(item_cost)
    relative_discount = validate_entry(relative_discount)
    absolute_discount = validate_entry(absolute_discount)
    
    if (item_cost == -1 or relative_discount == -1 or absolute_discount == -1):
        print "Invalid number entered for cost and/or discount"
        raise ValueError("Invalid entry")
        return -1
    else:
        discounted_price = calculate_discount(item_cost, relative_discount, absolute_discount)
        print discounted_price
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