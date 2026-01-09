

import logging
from binance import Client

logger = logging.getLogger("TradingBot.Client")

class BinanceClient:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)

        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com"
            logger.info("Using Binance Futures Testnet")

    def get_account_info(self):
        logger.info("Fetching futures account info")
        return self.client.futures_account()
