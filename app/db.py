from peewee import *
from .utils import Client


db = SqliteDatabase('database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Trades(BaseModel):
    types = {
        0: "Long",
        1: "Short"
    }
    id = AutoField()
    exchange = CharField()
    market = DateField()
    type = IntegerField()
    price = FloatField()
    amount = FloatField()
    
    def __str__(self):
        return f"[{self.id}][{self.exchange}][{self.market}]"

    def get_type(self):
        return self.types[self.type]

    @classmethod
    def get_all(cls):
        return cls.select()
    
    @property
    def price_str(self):
        return "%.8f" % self.price
    
    @property
    def amount_str(self):
        return "%.8f" % self.amount

    def get_data_model(self):
        c = Client(self.exchange.lower())
        c.update_prices()
        data = [
                self.id, self.exchange.title(), self.market.upper(), self.get_type(), self.price, self.amount,
                c.get_price(self.market)
            ]
        return data

# ─── CREA ───────────────────────────────────────────────────────────────────────

def create_tables():
    with db:
        db.create_tables([Trades])
