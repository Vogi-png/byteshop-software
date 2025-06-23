import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_tela_sobre import Ui_Sobre
import res_rc

class SobreWindow(QMainWindow):

    def __init__(self, parent_window):
        super().__init__()
        self.ui = Ui_Sobre()
        self.ui.setupUi(self)
        
        self.parent = parent_window
        
        # Conexões
        self.ui.voltar_button.clicked.connect(self.voltar_para_tela_anterior)
    
# -----------------------------------------------------------------------------------
    
    def voltar_para_tela_anterior(self):
        self.parent.show()
        self.close()