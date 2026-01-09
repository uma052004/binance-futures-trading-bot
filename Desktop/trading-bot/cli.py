from config import get_client
from bot import BasicBot

def main():
    api_key = input("Enter API Key: ").strip()
    api_secret = input("Enter API Secret: ").strip()

    client = get_client(api_key, api_secret)
    bot = BasicBot(client)

    print("\nOrder Types:")
    print("1. Market Order")
    print("2. Limit Order")
    print("3. Stop-Limit Order (Bonus)")

    choice = input("Select order type (1/2/3): ").strip()

    symbol = input("Symbol (e.g. BTCUSDT): ").upper()
    side = input("Side (BUY/SELL): ").upper()
    quantity = float(input("Quantity: "))

    if choice == "1":
        result = bot.place_market_order(symbol, side, quantity)

    elif choice == "2":
        price = float(input("Limit Price: "))
        result = bot.place_limit_order(symbol, side, quantity, price)

    elif choice == "3":
        stop_price = float(input("Stop Price: "))
        limit_price = float(input("Limit Price: "))
        result = bot.place_stop_limit(symbol, side, quantity, stop_price, limit_price)

    else:
        print("Invalid choice")
        return

    print("\nOrder Response:")
    print(result)

if __name__ == "__main__":
    main()
