API_KEY = "LNA6oGcezyXrvUi2Q9HF8mE86sQ1JkXez8paysONqCbFQHD2hF2PKlJ00CqAcQzu"
API_SECRET = "g8dNityeD4nhswac79oVMPhrpSGu94gDeKT4O7GysGzNSa91CKDpK9AVcGC1h8V8"
USE_TESTNET = True


# config.py
import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "bot.log")

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("TradingBot")
