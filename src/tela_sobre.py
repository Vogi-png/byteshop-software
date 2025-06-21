import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_tela_sobre import Ui_Sobre
import res_rc

class SobreWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Sobre()
        self.ui.setupUi(self)