
from PyQt5 import QtCore, QtGui, QtWidgets

from ui.mainwindow_Ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, ctx, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.ctx = ctx
