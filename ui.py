# ui.py
import streamlit as st
from bot.client import BinanceClient
from bot.orders import place_market_order, place_limit_order
from bot.validator import validate_order_args
from config import API_KEY, API_SECRET, USE_TESTNET, logger


st.set_page_config(page_title="Trading Bot (Testnet)", layout="centered")

st.title("📈 Binance Futures Trading Bot (Testnet)")
st.caption("Simple frontend for placing MARKET and LIMIT orders")


# ---- Form inputs ----
symbol = st.text_input("Symbol", value="BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT"])
qty = st.number_input("Quantity", min_value=0.001, value=0.01, step=0.001)

price = None
if order_type == "LIMIT":
    price = st.number_input("Price", min_value=1.0, value=30000.0, step=10.0)


# ---- Submit button ----
if st.button("Place Order"):
    try:
        # Fake args object for validation reuse
        class Args:
            pass

        args = Args()
        args.symbol = symbol
        args.side = side
        args.type = order_type
        args.qty = qty
        args.price = price

        validate_order_args(args)

        bot = BinanceClient(API_KEY, API_SECRET, USE_TESTNET)
        bot.get_account_info()

        if order_type == "MARKET":
            order = place_market_order(
                client=bot.client,
                symbol=symbol,
                side=side,
                quantity=qty
            )
        else:
            order = place_limit_order(
                client=bot.client,
                symbol=symbol,
                side=side,
                quantity=qty,
                price=price
            )

        st.success("✅ Order request sent successfully!")
        st.json(order)

    except Exception as e:
        logger.error("UI order placement failed", exc_info=True)
        st.error(f"❌ Error: {e}")
