# Problem 3: Expense Report Categorizer

expenses = {
    "Travel": [500, 200],
    "Meals": [40, 60, 30],
    "Supplies": [100]
}

grand_total = 0

for category in expenses:
    category_total = 0

    for amount in expenses[category]:
        category_total += amount

    print(f"{category}: ${category_total:.2f}")

    grand_total += category_total

print(f"Grand Total: ${grand_total:.2f}")