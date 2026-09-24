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
        
    return quantity


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

        total = int(lines[0])
        history = eval(lines[1])

        return total, history

    except FileNotFoundError:
        return 0, []


def main():
    inventory, history = load_inventory()
    errors = 0
    
    while True:
        result = get_valid_input()
        
        if result == "quit":
            generate_report(inventory, errors)
            break
            
        elif result is None:
            errors += 1
            continue
        
        quantity = result
        inventory = process_delivery(inventory, quantity)
        history.append(quantity)
        
        tax = calculate_tax(quantity)
        print(f"Tax for this delivery: {tax}")
        print("Current inventory:", inventory)
        
        if inventory > 500:
            print("Inventory exceeds 500 units.")
            generate_report(inventory, errors)
            break

main()