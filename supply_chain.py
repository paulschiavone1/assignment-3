# Problem 7: Simple Supply Chain Tracker

warehouses = [
    {"name": "Warehouse A", "inventory": {"Apples": 100, "Bananas": 150}},
    {"name": "Warehouse B", "inventory": {"Apples": 200, "Bananas": 100}}
]

total_stock = {}

# Loop through each warehouse
for warehouse in warehouses:

    # Loop through each product in the warehouse
    for product in warehouse["inventory"]:
        amount = warehouse["inventory"][product]

        if product in total_stock:
            total_stock[product] += amount
        else:
            total_stock[product] = amount

# Display total stock
for product in total_stock:
    print(f"{product}: {total_stock[product]}")