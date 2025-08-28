"""
Assignment: Online Store Inventory & Sales System

Create a Python program to manage an online store’s products, track inventory, process sales, and generate reports. 

Data structure(Sample)




Functions to Implement
add_product(store_dict, name, price, quantity)


Add a new product with the given price and quantity.


Return a success message if added, or a message if the product already exists.


update_stock(store_dict, name, quantity)


Update the stock of an existing product.


Return a success message if updated, or an error message if the product does not exist.


sell_product(store_dict, name, quantity)


Process a sale for the given product and quantity.


If enough stock exists, reduce the quantity and return the total sale price.


If stock is insufficient or product does not exist, return an appropriate error message.


display_inventory(store_dict)


Print all products with their prices and remaining quantity.


Return the total number of products displayed.


most_expensive_product(store_dict)


Find and return the product with the highest price along with its price.


total_potential_sales(store_dict)


Calculate the total value of all remaining stock  and return it.
"""

store = {}

# 1. Add a new product
def add_product(store_dict, name, price, quantity):
    if name in store_dict:
        return f"Product '{name}' already exists!"
    else:
        store_dict[name] = {"price": price, "quantity": quantity}
        return f"Product '{name}' added successfully."

# 2. Update stock
def update_stock(store_dict, name, quantity):
    if name in store_dict:
        store_dict[name]["quantity"] += quantity
        return f"Stock updated. '{name}' now has {store_dict[name]['quantity']} units."
    else:
        return f"Product '{name}' does not exist in inventory."

# 3. Process a sale
def sell_product(store_dict, name, quantity):
    if name not in store_dict:
        return f"Product '{name}' not found."
    if store_dict[name]["quantity"] < quantity:
        return f"Not enough stock of '{name}'. Available: {store_dict[name]['quantity']}."
    else:
        total_price = store_dict[name]["price"] * quantity
        store_dict[name]["quantity"] -= quantity
        return f"Sale successful! Total price: ${total_price}. Remaining stock of '{name}': {store_dict[name]['quantity']}."

# 4. Display inventory
def display_inventory(store_dict):
    if not store_dict:
        print("Inventory is empty.")
        return 0

    print("\nStore Inventory:")
    print("{:<15} {:<10} {:<10}".format("Product", "Price($)", "Quantity"))
    print("-" * 40)
    for product, details in store_dict.items():
        print("{:<15} {:<10} {:<10}".format(product, details["price"], details["quantity"]))
    print("-" * 40)
    return len(store_dict)

# 5. Find most expensive product
def most_expensive_product(store_dict):
    if not store_dict:
        return "No products in store."
    max_product = max(store_dict.items(), key=lambda item: item[1]["price"])
    return f"Most expensive product: {max_product[0]} at ${max_product[1]['price']}"

# 6. Calculate total potential sales
def total_potential_sales(store_dict):
    total_value = sum(details["price"] * details["quantity"] for details in store_dict.values())
    return f"Total potential sales value (all stock): ${total_value}"

# ----------------- DEMO -----------------
if __name__ == "__main__":
    print(add_product(store, "Laptop", 1200, 5))
    print(add_product(store, "Phone", 800, 10))
    print(add_product(store, "Headphones", 150, 20))
    print(add_product(store, "Laptop", 1400, 2))   # Duplicate

    print(update_stock(store, "Phone", 5))
    print(update_stock(store, "Tablet", 3))  # Not exist

    print(sell_product(store, "Phone", 3))
    print(sell_product(store, "Headphones", 25))  # More than stock

    display_inventory(store)

    print(most_expensive_product(store))
    print(total_potential_sales(store))

