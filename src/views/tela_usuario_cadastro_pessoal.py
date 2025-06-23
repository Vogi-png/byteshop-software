# Imports necessários no topo do arquivo
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QIntValidator
from ui.ui_tela_usuario_cadastro_pessoal import Ui_UsuarioCadastroPessoal
import res_rc


class CadastroClienteWindow(QMainWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.ui = Ui_UsuarioCadastroPessoal()
        self.ui.setupUi(self)
        self.parent = parent_window
        
        # Limite de caracteres no nome
        self.ui.usu_nome.setMaxLength(100)

        # Conexões
        self.ui.voltar_button.clicked.connect(self.voltar_para_tela_anterior)
        self.ui.usu_cpf.textChanged.connect(self.formatar_cpf)
        self.ui.usu_cadastrar_button.clicked.connect(self.realizar_cadastro)
        
# -----------------------------------------------------------------------------------
    # Função que faz o botão de voltar ir pra tela anterior  
    def voltar_para_tela_anterior(self):
        self.parent.show()
        self.close()
     
    # Regra do CPF   
    def formatar_cpf(self, texto):
        usu_cpf = self.sender()
        
        # Mantem apenas os números
        texto_limpo = ''.join(filter(str.isdigit, texto))
        
        # Limita o texto limpo a 11 dígitos (tamanho de um CPF)
        texto_limpo = texto_limpo[:11]

        
        if len(texto_limpo) > 9:
            texto_formatado = f"{texto_limpo[:3]}.{texto_limpo[3:6]}.{texto_limpo[6:9]}-{texto_limpo[9:]}"
        elif len(texto_limpo) > 6:
            texto_formatado = f"{texto_limpo[:3]}.{texto_limpo[3:6]}.{texto_limpo[6:]}"
        elif len(texto_limpo) > 3:
            texto_formatado = f"{texto_limpo[:3]}.{texto_limpo[3:]}"
        else:
            texto_formatado = texto_limpo
    
        
        usu_cpf.blockSignals(True)
        usu_cpf.setText(texto_formatado)
        usu_cpf.blockSignals(False)

        usu_cpf.setCursorPosition(len(texto_formatado))
        
# -----------------------------------------------------------------------------------

    def realizar_cadastro(self):
        usu_senha = self.ui.usu_senha.text()
        usu_senha_confirmar = self.ui.usu_senha_confirmar.text()

        
        # verifica se os campos não estão vazios
        if not usu_senha or not usu_senha_confirmar:
            self.mostrar_mensagem("Atenção", "Os campos de senha não podem estar vazios! ")
            return 

        #  verifica se os textos são iguais
        if usu_senha == usu_senha_confirmar:
            # SE FOREM IGUAIS:
            print("Senhas conferem! Prosseguindo com o cadastro...")
            
            self.mostrar_mensagem("Sucesso", "Cliente cadastrado com sucesso!")
            self.close() # Fecha a janela de cadastro
            self.parent.show() # Mostra a tela anterior

        else:
            # SE FOREM DIFERENTES:
            # Mostra uma mensagem de erro para o usuário
            self.mostrar_mensagem("Erro", "As senhas não conferem. Por favor, digite novamente! ")

    # Função auxiliar para mostrar caixas de mensagem
    def mostrar_mensagem(self, titulo, mensagem):
        msg_box = QMessageBox()
        # Define o ícone com base no título
        if titulo.lower() == 'erro':
            msg_box.setIcon(QMessageBox.Warning)
        else:
            msg_box.setIcon(QMessageBox.Information)
            
        msg_box.setText(mensagem)
        msg_box.setWindowTitle(titulo)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()


