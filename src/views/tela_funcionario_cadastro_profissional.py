import sys
import locale
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from datetime import datetime
from ui.ui_tela_funcionario_cadastro_profissional import Ui_FuncionarioCadastroProfissional
from database.conexao import criar_conexao
import res_rc

class CadastroProfissionalWindow(QMainWindow):
    def __init__(self, dados_pessoais, parent_window):
        super().__init__()
        self.ui = Ui_FuncionarioCadastroProfissional()
        self.ui.setupUi(self)
        
        self.dados_funcionario = dados_pessoais
        self.parent = parent_window
        
        try:
            locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
        except locale.Error:
            locale.setlocale(locale.LC_MONETARY, 'Portuguese_Brazil.1252')

        # Conexões
        self.ui.fun_cadastrar_button.clicked.connect(self.salvar_funcionario_completo)
        self.ui.voltar_button.clicked.connect(self.voltar_para_tela_pessoal)
        self.ui.fun_salario.textChanged.connect(self.formatar_salario)
        


    def salvar_funcionario_completo(self):
        # Coleta dados desta tela
        cargo = self.ui.fun_cargo.text().strip()
        salario_formatado = self.ui.fun_salario.text()
        email = self.ui.fun_email.text().strip()
        senha = self.ui.fun_senha.text()
        confirmar_senha = self.ui.fun_confirmar_senha.text()
        
        # Validação (sem telefone e categoria)
        if not all([cargo, salario_formatado, email, senha, confirmar_senha]):
            self.mostrar_mensagem("Atenção", "Todos os campos profissionais são obrigatórios.")
            return

        if senha != confirmar_senha:
            self.mostrar_mensagem("Erro", "As senhas não conferem.")
            return

        # Prepara os dados
        try:
            salario_limpo = salario_formatado.replace("R$", "").replace(".", "").replace(",", ".").strip()
            salario_final = float(salario_limpo) if salario_limpo else 0.0
            data_nasc_obj = datetime.strptime(self.dados_funcionario['aniversario'], "%d/%m/%Y")
            data_nasc_db = data_nasc_obj.strftime("%Y-%m-%d")
        except (ValueError, KeyError) as e:
            self.mostrar_mensagem("Erro de Dados", f"Formato de dado inválido: {e}")
            return
            
        # Junta todos os dados (sem telefone e categoria)
        self.dados_funcionario.update({
            "cargo": cargo, "salario": salario_final,
            "email": email, "senha": senha, "data_nascimento_db": data_nasc_db
        })

        # Salva no banco de dados
        conn = None
        try:
            conn = criar_conexao()
            cursor = conn.cursor()
            
            # COMANDO SQL FINAL: 'telefone' e 'categoria' foram removidos
            sql = """INSERT INTO funcionarios 
                     (nome, cpf, data_nascimento, cep, rua, numero, complemento, bairro, cidade_id, estado_id, 
                      cargo, salario, email, senha) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            
            # TUPLA DE VALORES FINAL: 'telefone' e 'categoria' foram removidos
            valores = (
                self.dados_funcionario['nome'], self.dados_funcionario['cpf'], self.dados_funcionario['data_nascimento_db'],
                self.dados_funcionario['cep'], self.dados_funcionario['rua'], self.dados_funcionario['numero'],
                self.dados_funcionario['complemento'], self.dados_funcionario['bairro'], 
                self.dados_funcionario['cidade_id'], self.dados_funcionario['estado_id'],
                self.dados_funcionario['cargo'], self.dados_funcionario['salario'],
                self.dados_funcionario['email'], self.dados_funcionario['senha']
            )
            
            cursor.execute(sql, valores)
            conn.commit()
            
            self.mostrar_mensagem("Sucesso", "Funcionário cadastrado com sucesso!")
            
            tabela_principal = self.parent.parent
            if tabela_principal and hasattr(tabela_principal, 'carregar_dados_funcionarios'):
                tabela_principal.carregar_dados_funcionarios()
            
            tabela_principal.show()
            self.parent.close()
            self.close()

        except Exception as e:
            if conn: conn.rollback()
            self.mostrar_mensagem("Erro de Banco de Dados", f"Não foi possível cadastrar o funcionário.\nErro: {e}")
        finally:
            if conn and conn.is_connected(): conn.close()
            
    def voltar_para_tela_pessoal(self):
        self.parent.show()
        self.close()

    def formatar_salario(self, texto):
        salario_lineEdit = self.sender()
        texto_limpo = ''.join(filter(str.isdigit, texto))
        if not texto_limpo: 
            salario_lineEdit.clear()
            return
        valor_real = int(texto_limpo) / 100.0
        texto_formatado = locale.currency(valor_real, grouping=True)
        salario_lineEdit.blockSignals(True)
        salario_lineEdit.setText(texto_formatado)
        salario_lineEdit.blockSignals(False)
        salario_lineEdit.end(False)
        
    # A função formatar_telefone foi completamente removida

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