import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_tela_menu import Ui_Menu
import res_rc

class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
