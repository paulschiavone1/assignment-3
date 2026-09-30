# Problem 2: Market Survey Analyzer

preferences = ["coffee", "tea", "coffee", "soda"]

counts = {}

for product in preferences:
    if product in counts:
        counts[product] += 1
    else:
        counts[product] = 1

total = len(preferences)

for product in counts:
    market_share = (counts[product] / total) * 100
    print(f"{product}: {market_share:.0f}%")