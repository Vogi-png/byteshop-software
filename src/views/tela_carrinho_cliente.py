import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_tela_carrinho_cliente import Ui_CarrinhoCliente
import res_rc


class CarrinhoClienteWindow(QMainWindow):

    def __init__(self, parent_window):
        super().__init__()
        self.ui = Ui_CarrinhoCliente()
        self.ui.setupUi(self)
        
        self.parent = parent_window
        
        # Conexões
        self.ui.voltar_button.clicked.connect(self.voltar_para_tela_anterior)
        
# -----------------------------------------------------------------------------------
        
    def voltar_para_tela_anterior(self):
        self.parent.show()
        self.close()