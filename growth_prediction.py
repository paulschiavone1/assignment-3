# Problem 9: Business Growth Projection

revenue = float(input("Enter initial revenue: $"))
growth_rate = float(input("Enter annual growth rate (%): "))

print("\nYear\tProjected Revenue")

for year in range(1, 11):
    revenue = revenue * (1 + growth_rate / 100)
    print(f"{year}\t${revenue:,.2f}")