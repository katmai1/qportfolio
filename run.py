"""
QPortfolio

Usage:
  qportfolio [--debug]
  qportfolio -h | --help
  qportfolio -v | --version


Options:
  -h --help     Show this screen.
  -v --version  Show version.
  --debug       Execute in debug mode.
"""

import docopt
import os

from signal import signal, SIGINT, SIG_DFL
from cached_property import cached_property

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QLibraryInfo, QLocale, QTranslator

from app.mainwindow import MainWindow
from app.db import db, create_tables


# ─── CONTEXTO APP ───────────────────────────────────────────────────────────────

class ContextoApp:

    language = "en_EN"

    def __init__(self, args):
        self.app = QApplication([])
        self.debug = args['--debug']
        signal(SIGINT, SIG_DFL)
        create_tables()

    def run(self):
        self.window.showMaximized()
        return self.app.exec()

    def tr(self, context, message):
        return self.app.translate(context, message)

    # ─── PROPIEDADES ────────────────────────────────────────────────────────────────

    @cached_property
    def window(self):
        return MainWindow(self)
    
    @cached_property
    def db(self):
        return db

    @cached_property
    def app_language(self):
        qtrans = QTranslator()
        qtrans.load(self.language, os.path.join("app", "i18n"))
        return qtrans

    @cached_property
    def system_language(self):
        qtrans = QTranslator()
        lang = f"qtbase_{self.language}"
        qtrans.load(lang, QLibraryInfo.location(QLibraryInfo.TranslationsPath))
        return qtrans

# ────────────────────────────────────────────────────────────────────────────────


# ─── MAIN ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    args = docopt.docopt(__doc__)
    appctx = ContextoApp(args)
    appctx.app.installTranslator(appctx.app_language)
    appctx.app.installTranslator(appctx.system_language)
    exit_code = appctx.run()
