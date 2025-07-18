import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_tela_menu_adm import Ui_MenuADM
import res_rc

class MenuADMWindow(QMainWindow):
    def __init__(self, parent_window=None):
        super().__init__()
        self.ui = Ui_MenuADM()
        self.ui.setupUi(self)
        self.parent = parent_window
        
    # Conexões
        self.ui.produtos_button.clicked.connect(self.abrir_tela_produto_adm)
        self.ui.cliente_button.clicked.connect(self.abrir_tela_usuario_adm)
        self.ui.funcionario_button.clicked.connect(self.abrir_tela_funcionario)
        self.ui.logout_button.clicked.connect(self.logout)

    def abrir_tela_produto_adm(self):
        from views.tela_tabela_produto_adm import TabelaProdutoAdmWindow
        self.janela_produto_adm = TabelaProdutoAdmWindow(parent_window=self)
        self.janela_produto_adm.show()
        self.hide()

    def abrir_tela_usuario_adm(self):
        from views.tela_tabela_usuario_adm import TabelaUsuarioAdmWindow
        self.janela_usuario_adm = TabelaUsuarioAdmWindow(parent_window=self)
        self.janela_usuario_adm.show()
        self.hide()

    def logout(self):
        from main import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
   
    def abrir_tela_funcionario(self):
        from views.tela_tabela_funcionario import TabelaFuncionarioWindow 
        
        self.janela_produto = TabelaFuncionarioWindow(parent_window=self)
        self.janela_produto.show()
        self.hide()
        

