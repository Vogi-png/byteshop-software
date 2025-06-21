import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_tela_tabela_produto import Ui_TabelaProduto
import res_rc

class TabelaProdutoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TabelaProduto()
        self.ui.setupUi(self)
    
        self.ui.cliente_button.clicked.connect(self.abrir_tela_cliente)
        self.ui.compras_button.clicked.connect(self.abrir_tela_carrinho)
        self.ui.sobre_button.clicked.connect(self.abrir_tela_sobre)

        
    def abrir_tela_cliente(self):
        from tela_tabela_usuario import TabelaUsuarioWindow
        
        self.janela_menu = TabelaUsuarioWindow()
        self.janela_menu.show()
        self.close()
        
    def abrir_tela_carrinho(self):
        from tela_carrinho import CarrinhoWindow 
        
        self.janela_menu = CarrinhoWindow()
        self.janela_menu.show()
        self.close()
        
    def abrir_tela_sobre(self):
        from tela_sobre import SobreWindow
        
        self.janela_menu = SobreWindow()
        self.janela_menu.show()
        self.close()
