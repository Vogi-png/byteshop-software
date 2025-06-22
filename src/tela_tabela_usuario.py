import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_tela_tabela_usuario import Ui_TabelaUsuario
import res_rc

class TabelaUsuarioWindow(QMainWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.ui = Ui_TabelaUsuario()
        self.ui.setupUi(self)
        
        self.parent = parent_window
        
        self.ui.produtos_button.clicked.connect(self.abrir_tela_produto)
        self.ui.compras_button.clicked.connect(self.abrir_tela_carrinho)
        self.ui.sobre_button.clicked.connect(self.abrir_tela_sobre)
        self.ui.add_button.clicked.connect(self.abrir_tela_cadastro_cliente)
        
    def abrir_tela_produto(self):
        from tela_tabela_produto import TabelaProdutoWindow

        self.janela_produto = TabelaProdutoWindow(parent_window=self)
        self.janela_produto.show()
        self.hide()
        
    def abrir_tela_carrinho(self):
        from tela_carrinho import CarrinhoWindow 
        
        self.janela_carrinho = CarrinhoWindow(parent_window=self)
        self.janela_carrinho.show()
        self.hide()
        
    def abrir_tela_sobre(self):
        from tela_sobre import SobreWindow
        
        self.janela_sobre = SobreWindow(parent_window=self)
        self.janela_sobre.show()
        self.hide()
        
    def abrir_tela_cadastro_cliente(self):
        from tela_usuario_cadastro_pessoal import CadastroClienteWindow
        
        self.janela_sobre = CadastroClienteWindow(parent_window=self)
        self.janela_sobre.show()
        self.hide() 