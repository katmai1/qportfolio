import ccxt


class Client:
    
    def __init__(self, exchange):
        self.exchange = exchange.lower()
        self.client = getattr(ccxt, self.exchange)()
        self.client.enableRateLimit = True
    
    def update_prices(self):
        self.prices = self.client.fetch_tickers()
    
    def get_price(self, market):
        return self.prices[market.upper()]['last']