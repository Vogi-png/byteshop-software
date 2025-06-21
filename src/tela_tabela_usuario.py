import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_tela_tabela_usuario import Ui_TabelaUsuario
import res_rc

class TabelaUsuarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TabelaUsuario()
        self.ui.setupUi(self)