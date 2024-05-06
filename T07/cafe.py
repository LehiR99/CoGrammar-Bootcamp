# create a menu list store each drink
menu = ["Latte", "Cappucino", "Espresso", "Tea"]

# create stock and price dictionaries to store the correspoing amounts and values of each drink
stock = {"Latte":20, "Cappucino":10, "Espresso":30, "Tea":5}
price = {"Latte": 3.0, "Cappucino":4.0, "Espresso":2.5, "Tea":2.0}

#initialise the total_stock_value variable
total_stock_value = 0

# Create for loop to multiply to stock and price for each drink from their corresponding dictionaries
for drink in menu:
    drink_value = stock[drink] * price[drink]
    total_stock_value += drink_value

# Print the total stock using f string to call the variable
print(f"The total stock value is £{total_stock_value}")