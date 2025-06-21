import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_tela_menu import Ui_Menu
from tela_carrinho import CarrinhoWindow
import res_rc

class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.ui.compras_button.clicked.connect(self.abrir_tela_carrinho)
        
    def abrir_tela_carrinho(self):
        # (Aqui você pode colocar uma verificação de senha no futuro)

        self.janela_menu = CarrinhoWindow()
        self.janela_menu.show()
        self.close()
