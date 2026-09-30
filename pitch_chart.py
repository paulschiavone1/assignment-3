# Problem 10: Startup Pitch Deck Visualizer

revenue = {
    "Year 1": 3,
    "Year 2": 5,
    "Year 3": 8
}

# Loop through each year
for year in revenue:
    print(f"{year}: ", end="")

    # Create the bar using #
    for i in range(revenue[year]):
        print("#", end="")

    print()