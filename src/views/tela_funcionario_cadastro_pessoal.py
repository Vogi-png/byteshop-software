# Arquivo: src/views/tela_funcionario_cadastro_pessoal.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QIntValidator
from datetime import datetime
from database.conexao import criar_conexao
from views.tela_funcionario_cadastro_profissional import CadastroProfissionalWindow
from ui.ui_tela_funcionario_cadastro_pessoal import Ui_FuncionarioCadastroPessoal
import res_rc

class CadastroFuncionarioWindow(QMainWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.ui = Ui_FuncionarioCadastroPessoal()
        self.ui.setupUi(self)
        self.parent = parent_window
        
        self.ui.fun_nome.setMaxLength(100)
        self.ui.fun_rua.setMaxLength(100)
        self.ui.fun_bairro.setMaxLength(50)
        self.ui.fun_numero.setValidator(QIntValidator())
        self.ui.fun_complemento.setMaxLength(50)

        self.ui.voltar_button.clicked.connect(self.voltar_para_tela_anterior)
        self.ui.seguir_button.clicked.connect(self.ir_para_tela_profissional)
        
        self.ui.fun_cpf.textChanged.connect(self.formatar_cpf)
        self.ui.fun_aniversario.textChanged.connect(self.formatar_data)
        self.ui.fun_aniversario.editingFinished.connect(self.validar_data)
        self.ui.fun_cep.textChanged.connect(self.formatar_cep)

        self.carregar_estados()
        self.ui.fun_estado.currentIndexChanged.connect(self.carregar_cidades)

    def ir_para_tela_profissional(self):
        dados_pessoais = {
            "nome": self.ui.fun_nome.text().strip(),
            "cpf": self.ui.fun_cpf.text(),
            "aniversario": self.ui.fun_aniversario.text(),
            "cep": self.ui.fun_cep.text(),
            "rua": self.ui.fun_rua.text().strip(),
            "numero": self.ui.fun_numero.text().strip(),
            "complemento": self.ui.fun_complemento.text().strip(),
            "bairro": self.ui.fun_bairro.text().strip(),
            "cidade_id": self.ui.fun_cidade.currentData(),
            "estado_id": self.ui.fun_estado.currentData()
        }

        campos_obrigatorios = ["nome", "cpf", "aniversario", "cep", "rua", "numero", "bairro", "cidade_id", "estado_id"]
        for campo in campos_obrigatorios:
            if not dados_pessoais[campo] or dados_pessoais[campo] == -1:
                self.mostrar_mensagem("Atenção", f"O campo '{campo.replace('_id', '').capitalize()}' é obrigatório.")
                return
        
        self.janela_profissional = CadastroProfissionalWindow(dados_pessoais, parent_window=self)
        self.janela_profissional.show()
        self.hide()

    # ... (suas outras funções como carregar_estados, formatar_cpf, etc. continuam aqui, sem alterações) ...
    def carregar_estados(self):
        conn = None
        try:
            conn = criar_conexao()
            cursor = conn.cursor()
            cursor.execute("SELECT id, sigla FROM estados ORDER BY sigla")
            self.ui.fun_estado.clear()
            self.ui.fun_estado.addItem("Selecione...", -1) 
            for estado_id, sigla in cursor.fetchall():
                self.ui.fun_estado.addItem(sigla, estado_id)
        except Exception as e:
            self.mostrar_mensagem("Erro", f"Não foi possível carregar os estados: {e}")
        finally:
            if conn and conn.is_connected(): conn.close()

    def carregar_cidades(self):
        estado_id = self.ui.fun_estado.currentData() 
        self.ui.fun_cidade.clear()
        if not estado_id or estado_id == -1: return 
        conn = None
        try:
            conn = criar_conexao()
            cursor = conn.cursor() 
            sql = "SELECT id, nome FROM cidades WHERE estado_id = %s ORDER BY nome"
            cursor.execute(sql, (estado_id,))
            for cidade_id, nome in cursor.fetchall():
                self.ui.fun_cidade.addItem(nome, cidade_id)
        except Exception as e:
            self.mostrar_mensagem("Erro", f"Não foi possível carregar as cidades: {e}")
        finally:
            if conn and conn.is_connected(): conn.close()

    def voltar_para_tela_anterior(self):
        self.parent.show()
        self.close()
        
    def formatar_cpf(self, texto):
        cpf_lineEdit = self.sender()
        texto_limpo = ''.join(filter(str.isdigit, texto))
        texto_limpo = texto_limpo[:11]
        
        if len(texto_limpo) > 9: texto_formatado = f"{texto_limpo[:3]}.{texto_limpo[3:6]}.{texto_limpo[6:9]}-{texto_limpo[9:]}"
        elif len(texto_limpo) > 6: texto_formatado = f"{texto_limpo[:3]}.{texto_limpo[3:6]}.{texto_limpo[6:]}"
        elif len(texto_limpo) > 3: texto_formatado = f"{texto_limpo[:3]}.{texto_limpo[3:]}"
        else: texto_formatado = texto_limpo
        
        cpf_lineEdit.blockSignals(True)
        cpf_lineEdit.setText(texto_formatado)
        cpf_lineEdit.blockSignals(False)
        cpf_lineEdit.setCursorPosition(len(texto_formatado))
        
    def formatar_cep(self, texto):
        cep_lineEdit = self.sender()
        texto_limpo = ''.join(filter(str.isdigit, texto))
        texto_limpo = texto_limpo[:8]
        if len(texto_limpo) > 5: texto_formatado = f"{texto_limpo[:5]}-{texto_limpo[5:]}"
        else: texto_formatado = texto_limpo
        cep_lineEdit.blockSignals(True)
        cep_lineEdit.setText(texto_formatado)
        cep_lineEdit.blockSignals(False)
        cep_lineEdit.setCursorPosition(len(texto_formatado))
    
    def formatar_data(self, texto):
        data_lineEdit = self.sender()
        texto_limpo = ''.join(filter(str.isdigit, texto))
        texto_limpo = texto_limpo[:8]
        if len(texto_limpo) > 4: texto_formatado = f"{texto_limpo[:2]}/{texto_limpo[2:4]}/{texto_limpo[4:]}"
        elif len(texto_limpo) > 2: texto_formatado = f"{texto_limpo[:2]}/{texto_limpo[2:]}"
        else: texto_formatado = texto_limpo
        data_lineEdit.blockSignals(True)
        data_lineEdit.setText(texto_formatado)
        data_lineEdit.blockSignals(False)
        data_lineEdit.setCursorPosition(len(texto_formatado))

    def validar_data(self):
        data_lineEdit = self.sender()
        texto_data = data_lineEdit.text()
        if not texto_data or len(texto_data) != 10: return
        try:
            data_digitada = datetime.strptime(texto_data, "%d/%m/%Y").date()
            if data_digitada > datetime.now().date():
                self.mostrar_mensagem("Erro de Data", "A data de aniversário não pode ser no futuro.")
                data_lineEdit.clear()
        except ValueError:
            self.mostrar_mensagem("Erro de Data", "Data inválida.")
            data_lineEdit.clear()
            
    def mostrar_mensagem(self, titulo, mensagem):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(mensagem)
        msg_box.setWindowTitle(titulo)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()