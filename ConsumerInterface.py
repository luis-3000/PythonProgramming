# Simple Consumer interface for some products
"""Stocking Out
	Now you need your compute_bill function to take the stock/inventory
	of a particular item into account when computing the cost.

	Ultimately, if an item isn't in stock, then it shouldn't be included
	in the total. You can't buy or sell what you don't have! """

shopping_list = ["banana", "orange", "apple"]
food = ["banana", "apple", "orange", "pear"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for key in food:
        if stock[key] > 0: # At least 1 item to sell
            total = total + prices[key] #Add price of that item to total
            stock[key]-= 1 # update stock count
        
    return total