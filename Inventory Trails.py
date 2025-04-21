items={}
while True:
    print("-----Menu-----")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show Items")
    print("4. Exit")
    print("--------------")
    
    try:
        z = int(input("Enter your option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if z == 1:
        name = input("Enter the item name: ")
        try:
            rate = float(input("Enter the item rate: "))
        except ValueError:
            print("Please enter a valid rate.")
            continue
        items[name] = rate
        print(f"'{name}' added with rate {rate}")
    elif z == 2:
        name = input("Enter the item name to remove: ")
        if name in items:
            del items[name]
            print(f"'{name}' removed.")
        else:
            print("Item not found.")
    elif z == 3:
        if items:
            print("Current items:")
            for item, rate in items.items():
                print(f"- {item}: {rate}")
        else:
            print("No items in the list.")
    elif z == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")