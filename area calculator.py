inventory = {}
def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def remove_item(item, quantity):
    if item in inventory:
        if inventory[item] >= quantity:
            inventory[item] -= quantity
        else:
            print("Not enough stock to remove")
    else:
        print("Item not found in inventory")

def show_inventory():
    print("Inventory:")
    for item, quantity in inventory.items():
        print(item, ":", quantity)
        
add_item("Apples", 10)
add_item("Oranges", 5)
remove_item("Apples", 3)
show_inventory()
