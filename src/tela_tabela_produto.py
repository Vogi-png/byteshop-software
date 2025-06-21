import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_tela_tabela_produto import Ui_TabelaProduto
import res_rc

class TabelaProdutoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TabelaProduto()
        self.ui.setupUi(self)