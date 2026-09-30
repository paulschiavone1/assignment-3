# Problem 8: Customer Loyalty Tiers

customers = {
    "Alice": 800,
    "Bob": 2500,
    "Carol": 6000,
    "David": 1200
}

tiers = {
    "Bronze": 0,
    "Silver": 0,
    "Gold": 0
}

# Check each customer's purchase amount
for customer in customers:
    amount = customers[customer]

    if amount < 1000:
        tiers["Bronze"] += 1
    elif amount < 5000:
        tiers["Silver"] += 1
    else:
        tiers["Gold"] += 1

# Print the summary
print(f"Bronze: {tiers['Bronze']}")
print(f"Silver: {tiers['Silver']}")
print(f"Gold: {tiers['Gold']}")