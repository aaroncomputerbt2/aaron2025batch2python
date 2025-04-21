class ItemManager:
    def __init__(self):
        self.items = {}

    def add_item(self):
        name = input("Enter the item name: ")
        try:
            rate = float(input("Enter the item rate: "))
        except ValueError:
            print("Please enter a valid rate.")
            return
        self.items[name] = rate
        print(f"'{name}' added with rate {rate}")

    def remove_item(self):
        name = input("Enter the item name to remove: ")
        if name in self.items:
            del self.items[name]
            print(f"'{name}' removed.")
        else:
            print("Item not found.")

    def show_items(self):
        if self.items:
            print("Current items:")
            for item, rate in self.items.items():
                print(f"- {item}: {rate}")
        else:
            print("No items in the list.")

    def menu(self):
        while True:
            print("-----Menu-----")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Show Items")
            print("4. Exit")
            print("--------------")

            try:
                choice = int(input("Enter your option: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if choice == 1:
                self.add_item()
            elif choice == 2:
                self.remove_item()
            elif choice == 3:
                self.show_items()
            elif choice == 4:
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please choose 1, 2, 3, or 4.")


# Running the program
if __name__ == "__main__":
    manager = ItemManager()
    manager.menu()