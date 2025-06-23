import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_tela_menu_fun import Ui_MenuFun 
import res_rc


class MenuFunWindow(QMainWindow):
    def __init__(self, parent_window=None):
        
        super().__init__()
        self.ui = Ui_MenuFun()
        self.ui.setupUi(self)
        self.parent = parent_window
    
        self.ui.produtos_button.clicked.connect(self.abrir_tela_produto)
        self.ui.cliente_button.clicked.connect(self.abrir_tela_cliente)
        self.ui.compras_button.clicked.connect(self.abrir_tela_carrinho)
        self.ui.sobre_button.clicked.connect(self.abrir_tela_sobre)
        
    def abrir_tela_produto(self):
        from views.tela_tabela_produto import TabelaProdutoWindow 
        
        self.janela_produto = TabelaProdutoWindow(parent_window=self)
        self.janela_produto.show()
        self.hide()
        
    def abrir_tela_cliente(self):
        from views.tela_tabela_usuario import TabelaUsuarioWindow 
        
        self.janela_cliente = TabelaUsuarioWindow(parent_window=self)
        self.janela_cliente.show()
        self.hide()
        
    def abrir_tela_carrinho(self):
        from views.tela_carrinho import CarrinhoWindow 
        
        self.janela_carrinho = CarrinhoWindow(parent_window=self)
        self.janela_carrinho.show()
        self.hide()
        
    def abrir_tela_sobre(self):
        from views.tela_sobre import SobreWindow 
        
        self.janela_sobre = SobreWindow(parent_window=self)
        self.janela_sobre.show()
        self.hide()