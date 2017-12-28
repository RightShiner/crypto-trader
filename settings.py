import os
from decimal import Decimal

API_VERSION = 1
API_URL = 'https://api.gemini.com'
API_WS_URL = 'wss://api.gemini.com'
STARTING_NONCE = 600                # must always increase incrementally

SYMBOL = 'ethusd'                   # currency pair to trade
POLL_DELAY = 30                     # runloop interval in seconds
MAX_ACTIVE_ORDERS = 3               # maximum number of active orders to track
USD_MIN_ORDER_AMT = Decimal(1.00)   # min amount to use when making new orders
USD_MAX_ORDER_AMT = Decimal(5.00)   # max amount to use when making new orders
MAX_GAIN_RATIO = Decimal(0.01)      # maximum percentage gains before selling the order
MAX_LOSS_RATIO = Decimal(-0.006)    # maximum percentage losses before selling the order
OVERPAY_RATIO = Decimal(0.005)      # percentage to pay over current price in order to guarantee orders closing quickly

USD_MAX_NET_GAINS = 100             # total maximum USD gains before quitting the program
USD_MAX_NET_LOSS = -20              # total maximum USD losses before quitting the program

DATA_DIR = f'./data/{SYMBOL}'       # where to store the state and logs

try:
    from secrets import *               # copy and edit secrets_default.py to secrets.py
except ImportError:
    print('Copy secrets_default.py to secrets.py to add your API credentials')
    raise SystemExit(1)

try:
    os.makedirs(DATA_DIR)
except Exception:
    pass
