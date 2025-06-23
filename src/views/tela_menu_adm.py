import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_tela_menu_adm import Ui_MenuADM

import res_rc

class MenuADMWindow(QMainWindow):
    def __init__(self, parent_window=None):
        super().__init__()
        self.ui = Ui_MenuADM()
        self.ui.setupUi(self)
        self.parent = parent_window
   

