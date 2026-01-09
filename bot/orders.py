# bot/orders.py
import logging

logger = logging.getLogger("TradingBot.Orders")


def place_market_order(client, symbol, side, quantity):
    logger.info(
        f"Placing MARKET order | Symbol={symbol} | Side={side} | Qty={quantity}"
    )

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    logger.info(f"MARKET order response: {order}")
    return order


def place_limit_order(client, symbol, side, quantity, price):
    logger.info(
        f"Placing LIMIT order | Symbol={symbol} | Side={side} | Qty={quantity} | Price={price}"
    )

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )

    logger.info(f"LIMIT order response: {order}")
    return order
