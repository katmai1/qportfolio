from PyQt5 import QtCore, QtWidgets, QtGui
from .ui.dialog_trade_Ui import Ui_DialogTrade
from .db import Trades


class DialogTrade(QtWidgets.QDialog, Ui_DialogTrade):
    
    def __init__(self, parent=None):
        super().__init__(parent=parent) 
        self.setupUi(self)
        #
        
    @property
    def exchange(self):
        return self.combo_exchange.currentText().lower()

    @property
    def market(self):
        return self.ed_market.text().lower().strip()
    
    @property
    def type(self):
        return self.combo_type.currentIndex()
    
    @property
    def price(self):
        return self.spin_price.value()
    
    @property
    def amount(self):
        return self.spin_amount.value()
    
    def is_valid(self):
        if len(self.exchange) <= 2:
            return False
        if self.spin_price == 0.0 or self.spin_amount == 0.0:
            return False
        return True
        
    def create_trade(self):
        t = Trades.create(
            exchange=self.exchange,
            market=self.market,
            type=self.type,
            price=self.price,
            amount=self.amount
        )
        t.save()
    
    def accepted(self):
        if self.is_valid():
            return super().accepted()
        else:
            print("check values")