import sys
import locale
from PySide6.QtWidgets import QApplication, QMainWindow
from views.tela_menu_adm import MenuADMWindow
from views.tela_menu_fun import MenuFunWindow

from ui.ui_tela_login import Ui_Login
import res_rc

try:
    locale.setlocale(locale.LC_ALL, '')
except locale.Error:
    print("AVISO: Não foi possível definir o locale padrão do sistema.")
# ------------------------------------


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowTitle("ByteShop - Login")
        self.ui.login_button.clicked.connect(self.tentar_login)
        self.ui.redefinir_button.clicked.connect(self.redefinir_senha)

    def redefinir_senha(self):
        from PySide6.QtWidgets import QInputDialog, QMessageBox
        from database.redefinir_senha import email_existe, redefinir_senha
        email, ok = QInputDialog.getText(self, "Redefinir senha", "Digite seu email cadastrado:")
        if not ok or not email.strip():
            return
        email = email.strip()
        if not email_existe(email):
            QMessageBox.warning(self, "Email não encontrado", "O email informado não está cadastrado.")
            return
        nova_senha, ok2 = QInputDialog.getText(self, "Nova senha", "Digite a nova senha:")
        if not ok2 or not nova_senha.strip():
            return
        nova_senha = nova_senha.strip()
        if redefinir_senha(email, nova_senha):
            QMessageBox.information(self, "Sucesso", "Senha redefinida com sucesso!")
        else:
            QMessageBox.critical(self, "Erro", "Não foi possível redefinir a senha. Tente novamente.")

    def tentar_login(self):
        from database.autenticacao import autenticar_usuario
        email = self.ui.email_usuario.text().strip()
        senha = self.ui.senha_usuario.text().strip()
        if not email or not senha:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.warning(self, "Erro de login", "Preencha todos os campos.")
            return
        usuario = autenticar_usuario(email, senha)
        if usuario:
            if usuario.get('cargo', '').lower() == 'administrador':
                self.janela_menu = MenuADMWindow(parent_window=self)
            else:
                self.janela_menu = MenuFunWindow(parent_window=self)
            self.janela_menu.show()
            self.hide()
        else:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.critical(self, "Login falhou", "Email ou senha incorretos.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
