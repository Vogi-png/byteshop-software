import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_tela_tabela_produto import Ui_TabelaProduto
import res_rc


class TabelaProdutoWindow(QMainWindow):

    def __init__(self, parent_window):
        super().__init__()
        self.ui = Ui_TabelaProduto()
        self.ui.setupUi(self)
        
        self.parent = parent_window
        
        # Conexões
        self.ui.cliente_button.clicked.connect(self.abrir_tela_cliente)
        self.ui.compras_button.clicked.connect(self.abrir_tela_carrinho)
        self.ui.sobre_button.clicked.connect(self.abrir_tela_sobre)
        self.ui.add_button.clicked.connect(self.abrir_tela_cadastro_produto)
        
# -----------------------------------------------------------------------------------
    # Função que abre a tela cliente     
    def abrir_tela_cliente(self):
        from views.tela_tabela_usuario import TabelaUsuarioWindow
        
        self.janela_cliente = TabelaUsuarioWindow(parent_window=self)
        self.janela_cliente.show()
        self.hide()
    
    # Função que abre a tela carrinho     
    def abrir_tela_carrinho(self):
        from views.tela_carrinho import CarrinhoWindow 
        
        self.janela_carrinho = CarrinhoWindow(parent_window=self)
        self.janela_carrinho.show()
        self.hide()
     
    # Função que abre a tela sobre     
    def abrir_tela_sobre(self):
        from views.tela_sobre import SobreWindow
        
        self.janela_sobre = SobreWindow(parent_window=self)
        self.janela_sobre.show()
        self.hide() 
    
    # Função que abre a tela cadastrar produto (+)    
    def abrir_tela_cadastro_produto(self):
        from views.tela_cadastro_produto import CadastroProdutoWindow
        
        self.janela_sobre = CadastroProdutoWindow(parent_window=self)
        self.janela_sobre.show()
        self.hide() 
