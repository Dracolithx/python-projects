print("Welcome to our Restaurant!")

# menu prices
prices = {
        "burger": 12,
        "fries": 7,
        "drink": 5
}

# ask user for order
item = input("What would you like to order? (burger/fries/drink): ").lower()
quantity = int(input("How many would you like?: "))

# calculate total price
if item in prices:
    total = prices[item] * quantity

    # discount for order above 5 items
    if quantity > 5:
        print("You get a 10% discount!")
        total *= 0.9

    print(f"Your total for {quantity} {item}(s) is: {total:.2f} €")
else:
    print("Sorry, we don't have that item on the menu")
