
from PyQt5 import QtCore, QtGui, QtWidgets

from .ui.mainwindow_Ui import Ui_MainWindow
from .dialog_trade import DialogTrade
from .db import Trades


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.header = ['ID', 'Exchange', 'Market', 'Type', 'Price', 'Amount', 'LastPrice']

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            
            value = self._data[index.row()][index.column()]
            
            if isinstance(value, float):
                return "%.8f" % value
            
            return value
    
    def row(self, row):
        return self._data[row]

    def headerData(self, int, QtOrientation, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if QtOrientation == QtCore.Qt.Horizontal and role ==QtCore.Qt.ItemDataRole.DisplayRole:
            return self.header[int]
        return None

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

# ─── MAIN ───────────────────────────────────────────────────────────────────────

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, ctx, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.ctx = ctx
        #
        self.btn_add.clicked.connect(self.onAddTrade)
        self.btn_edit.clicked.connect(self.onEditTrade)
        self.btn_delete.clicked.connect(self.onDeleteTrade)
        self.load_trades()
    
    def onAddTrade(self):
        dialog = DialogTrade(self)
        if dialog.exec_():
            dialog.create_trade()
        
    def onEditTrade(self):
        dialog = DialogTrade(self)
        if dialog.exec_():
            print("okk")
    
    def onDeleteTrade(self):
        row = self.tabla.currentIndex().row()
        item = self.model.row(row)
        Trades.delete_by_id(item[0])
        self.load_trades()
    
    def load_trades(self):
        data = []
        for t in Trades.get_all():
            data.append(t.get_data_model())
        self.model = TableModel(data)
        self.tabla.setModel(self.model)
        