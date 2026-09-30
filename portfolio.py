# Problem 5: Stock Portfolio Tracker

portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130}
}

total_value = 0

for stock in portfolio:
    shares = portfolio[stock]["shares"]
    price = portfolio[stock]["price"]
    value = shares * price

    print(f"{stock}: ${value:.2f}")

    total_value += value

print(f"Total Portfolio Value: ${total_value:.2f}")