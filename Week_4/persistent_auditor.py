def get_valid_input():
    item = input("Enter the item name (or type 'quit' to finish): ")

    if item.lower() == "quit":
        return "quit"

    quantity_input = input(f"Enter the quantity for {item}: ")

    if not quantity_input.isdigit():
        print("Invalid quantity. Please enter a number.")
        return None

    quantity = int(quantity_input)

    if quantity < 0:
        print("Quantity cannot be negative. Please enter a valid number.")
        return None

    return item, quantity


def process_delivery(history, item, quantity):
    history.append([item, quantity])
    return history


def calculate_tax(amount):
    return amount * 0.10


def generate_report(history, failed_attempts):
    total_units = 0

    for item in history:
        total_units += item[1]

    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

        if len(lines) == 0:
            return []

        history = eval(lines[0])

        return history

    except FileNotFoundError:
        return []


def save_inventory(history):
    with open("inventory.txt", "w") as file:
        file.write(str(history))


def main():
    history = load_inventory()
    errors = 0

    while True:
        result = get_valid_input()

        if result == "quit":
            save_inventory(history)
            generate_report(history, errors)
            break

        elif result is None:
            errors += 1
            continue

        item, quantity = result

        history = process_delivery(history, item, quantity)

        tax = calculate_tax(quantity)
        print(f"Tax for this delivery: {tax}")

        total_inventory = 0

        for entry in history:
            total_inventory += entry[1]

        print("Current inventory:", total_inventory)

        if total_inventory > 500:
            print("Inventory exceeds 500 units.")
            generate_report(history, errors)
            save_inventory(history)
            break


main()