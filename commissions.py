# Problem 4: Sales Commission Calculator

sales = {
    "Alice": 5000,
    "Bob": 7000,
    "Carol": 3000
}

def calculate_commission(sale):
    return sale * 0.10


for employee in sorted(sales, key=sales.get, reverse=True):
    commission = calculate_commission(sales[employee])
    print(f"{employee}: ${commission:.2f}")