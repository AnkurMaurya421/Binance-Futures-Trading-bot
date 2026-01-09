# main.py
import argparse
from bot.validator import validate_order_args
from bot.client import BinanceClient
from bot.orders import place_market_order, place_limit_order
from config import API_KEY, API_SECRET, USE_TESTNET, logger


def main():
    parser = argparse.ArgumentParser(
        description="Basic Binance Futures Trading Bot (Testnet)"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--qty", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    # Validate input
    try:
        validate_order_args(args)
    except ValueError as e:
        logger.error(f"Input validation failed: {e}")
        return

    logger.info("Starting Trading Bot")

    # Connect to Binance
    try:
        bot = BinanceClient(API_KEY, API_SECRET, USE_TESTNET)
        bot.get_account_info()
        logger.info("Connected to Binance Futures Testnet")
    except Exception:
        logger.error("Failed to connect to Binance", exc_info=True)
        return

    # Place order
    try:
        if args.type == "MARKET":
            place_market_order(
                client=bot.client,
                symbol=args.symbol,
                side=args.side,
                quantity=args.qty
            )
        else:
            place_limit_order(
                client=bot.client,
                symbol=args.symbol,
                side=args.side,
                quantity=args.qty,
                price=args.price
            )

        logger.info("Order request sent successfully")

    except Exception:
        logger.error("Order placement failed", exc_info=True)


if __name__ == "__main__":
    main()
