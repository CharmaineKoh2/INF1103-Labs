inventory = 0
errors = 0

while True:
    item = input("Enter the item name (or type 'quit' to finish): ")

    if item.lower() == "quit":
        print("Total Units Processed:", inventory)
        print("Number of Failed/Rejected Entries:", errors)
        break

    quantity_input = input(f"Enter the quantity for {item}: ")

    if not quantity_input.isdigit():
        print("Invalid quantity. Please enter a number.")
        errors += 1
        continue

    quantity = int(quantity_input)

    if quantity < 0:
        print("Quantity cannot be negative. Please enter a valid number.")
        errors += 1
        continue

    if inventory > 500:
            print("Inventory exceeds 500 units.")
            break

    inventory += quantity

    print("Current inventory:", inventory)

    if inventory > 500:
        print("Inventory exceeds 500 units.")
        break