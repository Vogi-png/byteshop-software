import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_tela_menu import Ui_Menu 
from tela_carrinho import CarrinhoWindow
from tela_tabela_usuario import TabelaUsuarioWindow
from tela_tabela_produto import TabelaProdutoWindow
from tela_sobre import SobreWindow

import res_rc

class MenuWindow(QMainWindow):
    def __init__(self, parent_window=None):
        super().__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.parent = parent_window
   
        self.ui.produtos_button.clicked.connect(self.abrir_tela_produto)
        self.ui.cliente_button.clicked.connect(self.abrir_tela_cliente)
        self.ui.compras_button.clicked.connect(self.abrir_tela_carrinho)
        self.ui.sobre_button.clicked.connect(self.abrir_tela_sobre)
        
    def abrir_tela_produto(self):
        
        self.janela_produto = TabelaProdutoWindow(parent_window=self) # <-- MUDANÇA 1
        self.janela_produto.show()
        self.hide()
        
    def abrir_tela_cliente(self):
        self.janela_cliente = TabelaUsuarioWindow(parent_window=self) # <-- MUDANÇA 1
        self.janela_cliente.show()
        self.hide()
        
    def abrir_tela_carrinho(self):
        self.janela_carrinho = CarrinhoWindow(parent_window=self) # <-- MUDANÇA 1
        self.janela_carrinho.show()
        self.hide()
        
    def abrir_tela_sobre(self):
        self.janela_sobre = SobreWindow(parent_window=self) # <-- MUDANÇA 1
        self.janela_sobre.show()
        self.hide()