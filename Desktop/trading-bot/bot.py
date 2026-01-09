from binance.exceptions import BinanceAPIException
from logger import setup_logger

logger = setup_logger()

class BasicBot:
    def __init__(self, client):
        self.client = client

    def place_market_order(self, symbol, side, quantity):
        try:
            logger.info(f"Market Order | {side} | {symbol} | Qty: {quantity}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                positionSide="LONG" if side == "BUY" else "SHORT",
                type="MARKET",
                quantity=quantity
            )
            logger.info(order)
            return order
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message}")
            print("ERROR:", e.message)
            return {"error": e.message}

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            logger.info(f"Limit Order | {side} | {symbol} | Qty: {quantity} | Price: {price}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                positionSide="LONG" if side == "BUY" else "SHORT",
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price,
                recvWindow=5000,
                newOrderRespType="RESULT"
            )

            logger.info(f"Order placed successfully: {order}")
            print("LIMIT order sent successfully (check Open Orders on Testnet)")
            return order

        except Exception as e:
            logger.error(f"Limit Order Error: {str(e)}")
            print("ERROR:", str(e))
            return {"error": str(e)}

    # Bonus: Stop-Limit Order
    def place_stop_limit(self, symbol, side, quantity, stop_price, limit_price):
        try:
            logger.info(f"Stop-Limit | {side} | {symbol}")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                positionSide="LONG" if side == "BUY" else "SHORT",
                type="STOP",
                quantity=quantity,
                stopPrice=stop_price,
                price=limit_price,
                timeInForce="GTC"
            )
            logger.info(order)
            return order
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message}")
            print("ERROR:", e.message)
            return {"error": e.message}
