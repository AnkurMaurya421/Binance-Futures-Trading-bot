📈 Binance Futures Trading Bot (Testnet)

A simplified Python-based trading bot for placing MARKET and LIMIT orders on the Binance Futures Testnet (USDT-M).
Built as part of a hiring assignment to demonstrate API integration, input validation, logging, and clean code structure.



Features:

Binance Futures Testnet support (USDT-M)

MARKET and LIMIT orders

BUY and SELL 
 
Command Line Interface (CLI)

Input validation

logging (requests, responses, errors)

Simple web frontend (Streamlit)


tradingbot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py        # Binance client setup (Testnet)
│   ├── orders.py        # Market & Limit order logic
│   ├── validator.py    # Input validation
│
├── logs/
│   └── bot.log          # Application logs
│
├── config.py            # API keys & logging config
├── main.py              # CLI entry point
├── ui.py                # Simple Streamlit frontend (bonus)
└── README.md



Prerequisites

Binance Futures Testnet account

Testnet API Key & Secret

Install dependencies:

pip install python-binance streamlit


Update config.py with your Binance Futures Testnet credentials:
API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_API_SECRET"
USE_TESTNET = True


CLI Usage
▶ Place a MARKET order
python main.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01

▶ Place a LIMIT order
python main.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.01 --price 30000

❌ Validation example (LIMIT without price)
python main.py --symbol BTCUSDT --side BUY --type LIMIT --qty 0.01

📝 Logging

The bot uses Python’s built-in logging module to log:

Bot startup

API requests

API responses

Errors and stack traces

Logs are written to:

logs/bot.log

🌐 Simple Frontend (Bonus)

A lightweight Streamlit UI is included for placing orders via a browser.

▶ Run the UI
streamlit run ui.py


Then open:

http://localhost:8501


The UI allows:

Selecting BUY / SELL

Choosing MARKET / LIMIT

Entering quantity and price

Viewing raw API response

ℹ️ Notes on Binance Futures Testnet

MARKET orders on Futures Testnet may return minimal responses

Order IDs or status may not always be included immediately

This is expected behavior and handled safely by the bot

All activity uses fake funds