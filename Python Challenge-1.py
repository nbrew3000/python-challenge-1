# Initialize an empty order list
order_list = []

# Sample menu items
menu_items = {
    1: {"name": "Apple", "price": 0.49},
    2: {"name": "Thai Iced Tea", "price": 3.99},
    3: {"name": "Fried Banana", "price": 4.49}
}

# Function to display menu
def display_menu(menu):
    print("Menu:")
    for key, item in menu.items():
        print(f"{key}: {item['name']} - ${item['price']}")

# Function to get menu selection
def get_menu_selection():
    while True:
                    menu_selection = int(input("1,2,3: "))
            if menu_selection in menu_items:
                return menu_selection
            else:
                print(" ")
        
        

# Display the menu
display_menu(menu_items)
menu_selection = get_menu_selection()

# Function to get quantity
def get_quantity(item_name):
    try:
        quantity = int(input(f"How many {item_name}s would you like to order? "))
        return quantity if quantity > 0 else 1
    except ValueError:
        return 1

# Get the selected item name and price
selected_item = menu_items[menu_selection]
item_name = selected_item["name"]
item_price = selected_item["price"]
quantity = get_quantity(item_name)

# Append order to order list
order_list.append({
    "Item name": item_name,
    "Price": item_price,
    "Quantity": quantity
})

# Function to ask if the customer wants to keep ordering
def ask_to_continue():
    while True:
        choice = input("Would you like to order another item? (y/n): ").lower()
        match choice:
            case 'y':
                return True
            case 'n':
                print("Thank you for your order.")
                return False
            case _:
                print("Invalid input. Please enter 'y' or 'n'.")

# Repeat the process until the customer is done ordering
place_order = True
while place_order:
    display_menu(menu_items)
    menu_selection = get_menu_selection()
    selected_item = menu_items[menu_selection]
    item_name = selected_item["name"]
    item_price = selected_item["price"]
    quantity = get_quantity(item_name)
    order_list.append({
        "Item name": item_name,
        "Price": item_price,
        "Quantity": quantity
    })
    place_order = ask_to_continue()
    
    # Function to print the receipt
def print_receipt(order):
    print("\nOrder Receipt")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")
    for item in order:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]
        item_name_spaces = " " * (26 - len(item_name))
        price_spaces = " " * (6 - len(f"${price:.2f}"))
        print(f"{item_name}{item_name_spaces}| ${price:.2f}{price_spaces}| {quantity}")

    # Calculate the total price
    total_price = sum(item["Price"] * item["Quantity"] for item in order)
    print(f"\nTotal Price: ${total_price:.2f}")

# Print the receipt
print_receipt(order_list)


# Initialize an empty order list
order_list = []

# Sample menu items
menu_items = {
    1: {"name": "Apple", "price": 0.49},
    2: {"name": "Thai Iced Tea", "price": 3.99},
    3: {"name": "Fried Banana", "price": 4.49}
}

# Function to display menu
def display_menu(menu):
    print("Menu:")
    for key, item in menu.items():
        print(f"{key}: {item['name']} - ${item['price']}")

# Function to get menu selection
def get_menu_selection():
    while True:
    
            menu_selection = int(input("1,2,3: "))
            if menu_selection in menu_items:
                return menu_selection
            else:
                print("get_menu_selection")
        

# Function to get quantity
def get_quantity(item_name):
    try:
        quantity = int(input(f"How many {item_name}s would you like to order? "))
        return quantity if quantity > 0 else 1
    except :
        return 1

# Function to ask if the customer wants to keep ordering
def ask_to_continue():
    while True:
        choice = input("Would you like to order another item? (y/n): ").lower()
        match choice:
            case 'y':
                return True
            case 'n':
                print("Thank you for your order.")
                return False
            case _:
                print("enter 'y' or 'n'.")

# Function to print the receipt
def print_receipt(order):
    print("\nOrder Receipt")
    print("Item name                 | Price  | Quantity")
    print("--------------------------|--------|----------")
    for item in order:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]
        item_name_spaces = " " * (26 - len(item_name))
        price_spaces = " " * (6 - len(f"${price:.2f}"))
        print(f"{item_name}{item_name_spaces}| ${price:.2f}{price_spaces}| {quantity}")

    # Calculate the total price
    total_price = sum(item["Price"] * item["Quantity"] for item in order)
    print(f"\nTotal Price: ${total_price:.2f}")

# Main loop for ordering process
place_order = True
while place_order:
    display_menu(menu_items)
    menu_selection = get_menu_selection()
    selected_item = menu_items[menu_selection]
    item_name = selected_item["name"]
    item_price = selected_item["price"]
    quantity = get_quantity(item_name)
    order_list.append({
        "Item name": item_name,
        "Price": item_price,
        "Quantity": quantity
    })
    place_order = ask_to_continue()

# Print the receipt
print_receipt(order_list)






