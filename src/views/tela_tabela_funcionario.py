import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_tela_tabela_funcionario import Ui_TabelaFuncionario
import res_rc


class TabelaFuncionarioWindow(QMainWindow):

    def __init__(self, parent_window):
        super().__init__()
        self.ui = Ui_TabelaFuncionario()
        self.ui.setupUi(self)
        
        self.parent = parent_window
        
        self.ui.add_button.clicked.connect(self.abrir_tela_cadastro_funcionario)
        
        # Função que abre a tela cadastrar produto (+)    
    def abrir_tela_cadastro_funcionario(self):
        from views.tela_funcionario_cadastro_pessoal import CadastroFuncionarioWindow
        
        self.janela_sobre = CadastroFuncionarioWindow(parent_window=self)
        self.janela_sobre.show()
        self.hide() 
