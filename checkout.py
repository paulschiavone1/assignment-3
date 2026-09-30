# Problem 1: Retail Checkout Simulation

prices = []

price = float(input("Enter item price (0 to finish): "))

while price != 0:
    prices.append(price)
    price = float(input("Enter item price (0 to finish): "))

total = sum(prices)
average = total / len(prices)

print(f"Total purchase amount: ${total:.2f}")
print(f"Average item cost: ${average:.2f}")
print(f"Number of items bought: {len(prices)}")