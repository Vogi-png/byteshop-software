import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_tela_carrinho import Ui_Carrinho
import res_rc

class CarrinhoWindow(QMainWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.ui = Ui_Carrinho()
        self.ui.setupUi(self)
        
        self.parent = parent_window
        
        # Conexões
        self.ui.produtos_button.clicked.connect(self.abrir_tela_produto)
        self.ui.cliente_button.clicked.connect(self.abrir_tela_cliente)
        self.ui.sobre_button.clicked.connect(self.abrir_tela_sobre)
        self.ui.add_button.clicked.connect(self.abrir_tela_carrinho_cliente)
        # Logout
        self.ui.logout_button.clicked.connect(self.logout)

    def logout(self):
        from main import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
        
# -----------------------------------------------------------------------------------
    
    def abrir_tela_produto(self):
        from views.tela_tabela_produto import TabelaProdutoWindow

        self.janela_menu = TabelaProdutoWindow(parent_window=self)
        self.janela_menu.show()
        self.hide()
        
    def abrir_tela_cliente(self):
        from views.tela_tabela_usuario import TabelaUsuarioWindow

        self.janela_menu = TabelaUsuarioWindow(parent_window=self)
        self.janela_menu.show()
        self.hide()
        
    def abrir_tela_sobre(self):
        from views.tela_sobre import SobreWindow

        self.janela_menu = SobreWindow(parent_window=self)
        self.janela_menu.show()
        self.hide()
        
    def abrir_tela_carrinho_cliente(self):
        from views.tela_carrinho_cliente import CarrinhoClienteWindow

        self.janela_menu = CarrinhoClienteWindow(parent_window=self)
        self.janela_menu.show()
        self.hide()