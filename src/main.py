import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_tela_login import Ui_Login
from tela_menu import MenuWindow
import res_rc

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()     
        self.ui.setupUi(self)
        self.ui.login_button.clicked.connect(self.abrir_tela_menu)

    def abrir_tela_menu(self):
        # (Aqui você pode colocar uma verificação de senha no futuro)

        self.janela_menu = MenuWindow()
        self.janela_menu.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())