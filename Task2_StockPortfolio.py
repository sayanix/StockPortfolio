stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 175,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("====================================")
print("       STOCK PORTFOLIO TRACKER")
print("====================================")

print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock} - ${price}")

while True:

    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("Please enter a valid number.")

print("\n====================================")
print("          PORTFOLIO SUMMARY")
print("====================================")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    value = price * quantity

    total_investment += value

    print(
        f"{stock}: "
        f"{quantity} shares × ${price} = ${value}"
    )

print("------------------------------------")
print(f"Total Investment: ${total_investment}")
print("====================================")