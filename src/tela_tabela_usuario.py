import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_tela_tabela_usuario import Ui_TabelaUsuario
import res_rc

class TabelaUsuarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TabelaUsuario()
        self.ui.setupUi(self)
        
        self.ui.produtos_button.clicked.connect(self.abrir_tela_produto)
        self.ui.compras_button.clicked.connect(self.abrir_tela_carrinho)
        self.ui.sobre_button.clicked.connect(self.abrir_tela_sobre)

        
    def abrir_tela_produto(self):
        from tela_tabela_produto import TabelaProdutoWindow

        self.janela_menu = TabelaProdutoWindow()
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
        
    