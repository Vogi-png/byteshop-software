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
        self.ui.funcionario_button.clicked.connect(self.abrir_tela_funcionario)
   
    def abrir_tela_funcionario(self):
        from views.tela_tabela_funcionario import TabelaFuncionarioWindow 
        
        self.janela_produto = TabelaFuncionarioWindow(parent_window=self)
        self.janela_produto.show()
        self.hide()
        

