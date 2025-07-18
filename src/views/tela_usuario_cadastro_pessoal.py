import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QIntValidator
from database.conexao import criar_conexao
from ui.ui_tela_usuario_cadastro_pessoal import Ui_UsuarioCadastroPessoal
import res_rc


class CadastroClienteWindow(QMainWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.ui = Ui_UsuarioCadastroPessoal()
        self.ui.setupUi(self)
        self.parent = parent_window
        
        self.ui.usu_nome.setMaxLength(100)

        self.ui.voltar_button.clicked.connect(self.voltar_para_tela_anterior)
        self.ui.usu_cpf.textChanged.connect(self.formatar_cpf)
        self.ui.usu_cadastrar_button.clicked.connect(self.realizar_cadastro)
        
    def voltar_para_tela_anterior(self):
        self.parent.show()
        self.close()
        
    def formatar_cpf(self, texto):
        usu_cpf = self.sender()
        texto_limpo = ''.join(filter(str.isdigit, texto))
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

    def realizar_cadastro(self):
        # Pega TODOS os dados do formulário
        nome = self.ui.usu_nome.text().strip()
        cpf = self.ui.usu_cpf.text()
        email = self.ui.usu_email.text().strip()
        senha = self.ui.usu_senha.text()
        confirmar_senha = self.ui.usu_senha_confirmar.text()

        # Validação de campos vazios
        if not nome or not cpf or not email or not senha or not confirmar_senha:
            self.mostrar_mensagem("Atenção", "Todos os campos são obrigatórios!")
            return

        # Validação de senhas
        if senha == confirmar_senha:
            # Se as senhas conferem, tenta salvar no banco
            conn = None
            try:
                conn = criar_conexao()
                cursor = conn.cursor()

                # Usando os nomes corretos das colunas da sua tabela
                sql = "INSERT INTO clientes (nome, CPF, email, senha) VALUES (%s, %s, %s, %s)"
                valores = (nome, cpf, email, senha)

                cursor.execute(sql, valores)
                conn.commit()

                self.mostrar_mensagem("Sucesso", "Cliente cadastrado com sucesso!")
                
                # ATUALIZA A TABELA NA TELA ANTERIOR
                if self.parent and hasattr(self.parent, 'carregar_dados_usuarios'):
                    self.parent.carregar_dados_usuarios()
                
                self.parent.show()
                self.close()

            except Exception as e:
                if conn:
                    conn.rollback()
                self.mostrar_mensagem("Erro de Banco de Dados", f"Não foi possível cadastrar o cliente.\nErro: {e}")
            
            finally:
                if conn and conn.is_connected():
                    conn.close()
        else:
            # Se as senhas forem diferentes
            self.mostrar_mensagem("Erro", "As senhas não conferem.")

    def mostrar_mensagem(self, titulo, mensagem):
        msg_box = QMessageBox()
        if titulo.lower() in ['erro', 'atenção']:
            msg_box.setIcon(QMessageBox.Warning)
        else:
            msg_box.setIcon(QMessageBox.Information)
            
        msg_box.setText(mensagem)
        msg_box.setWindowTitle(titulo)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()