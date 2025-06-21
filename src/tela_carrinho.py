import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_tela_carrinho import Ui_Carrinho
import res_rc

class CarrinhoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Carrinho()
        self.ui.setupUi(self)