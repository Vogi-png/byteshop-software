import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_tela_usuario_cadastro_pessoal import Ui_UsuarioCadastroPessoal
import res_rc


class CadastroClienteWindow(QMainWindow):

    def __init__(self, parent_window):
        super().__init__()
        self.ui = Ui_UsuarioCadastroPessoal()
        self.ui.setupUi(self)
        
        self.parent = parent_window
        
        self.ui.voltar_button.clicked.connect(self.voltar_para_tela_anterior)
        
    def voltar_para_tela_anterior(self):
        self.parent.show()
        self.close()