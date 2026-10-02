import json

def add_product(inventory):
    print("\nAdd New Product")

    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))

    inventory[product_id] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    print("\nProduct added successfully!")

    return inventory


def display_all(inventory):
    print("\nCurrent Inventory")
    print("------------------------------------------------")

    for product_id, product in inventory.items():
        print(
            f"ID: {product_id} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )
    print("------------------------------------------------")

def update_stock(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ")

    if product_id in inventory:
        print("\nProduct Found:")
        print(f"Name: {inventory[product_id]['name']}")
        print(f"Current Stock: {inventory[product_id]['stock']}")

        stock_input = input("\nNew Stock Quantity: ")

        if not stock_input.isdigit():
            print("Invalid stock quantity.")
            return inventory

        inventory[product_id]["stock"] = int(stock_input)

        print("\nStock updated successfully!")

    else:
        print("\nProduct not found.")

    return inventory

def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ")

    if product_id in inventory:
        product = inventory[product_id]

        print("\nProduct Found")
        print("------------------------------------------------")
        print(f"ID: {product_id}")
        print(f"Name: {product['name']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Stock: {product['stock']}")
        print("------------------------------------------------")

    else:
        print("\nProduct not found.")

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
        return inventory

    except FileNotFoundError:
        with open("inventory.json", "w") as file:
            json.dump({}, file)

        return {}

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)
    print("\nSaving inventory...")
    print("Inventory saved successfully to invetory.json.")

def main():

    inventory = load_inventory()

    print("\n===========================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("===========================")
    
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

    while True:

        option = input("\nEnter option: ")

        if option == "1":
            display_all(inventory)

        elif option == "2":
            inventory = add_product(inventory)

        elif option == "3":
            inventory = update_stock(inventory)

        elif option == "4":
            search_product(inventory)

        elif option == "5":
            save_inventory(inventory)

        elif option == "6":
            save_inventory(inventory)

            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")

            break

        else:
            print("\nInvalid option. Please enter 1-6.")


main()