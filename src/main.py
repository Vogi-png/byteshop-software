import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_tela_login import Ui_Login
from views.tela_menu_fun import MenuFunWindow
from views.tela_menu_adm import MenuADMWindow #pra aparecer a parte do adm é só trocar pelo "MenuADMWindow" no def abrir_tela_menu
import res_rc

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()     
        self.ui.setupUi(self)
        self.ui.login_button.clicked.connect(self.abrir_tela_menu)

    def abrir_tela_menu(self):
 
        self.janela_menu = MenuFunWindow()
        self.janela_menu.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())