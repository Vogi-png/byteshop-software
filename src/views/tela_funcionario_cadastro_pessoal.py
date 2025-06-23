# Imports necessários no topo do arquivo
import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QIntValidator
from ui.ui_tela_funcionario_cadastro_pessoal import Ui_FuncionarioCadastroPessoal
import res_rc

class CadastroFuncionarioWindow(QMainWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.ui = Ui_FuncionarioCadastroPessoal()
        self.ui.setupUi(self)
        self.parent = parent_window
        
        # Limite de caracteres no nome
        self.ui.fun_nome.setMaxLength(100)
        self.ui.fun_complemento.setMaxLength(30)
        self.ui.fun_rua.setMaxLength(50)
        self.ui.fun_bairro.setMaxLength(50)
        self.ui.fun_cidade.setMaxLength(20)
        self.ui.fun_estado.setMaxLength(2)
        
        # Mantem apenas os números
        self.ui.fun_numero.setValidator(QIntValidator())

        # Conexões
        self.ui.voltar_button.clicked.connect(self.voltar_para_tela_anterior)
        self.ui.fun_cpf.textChanged.connect(self.formatar_cpf)
        self.ui.fun_aniversario.textChanged.connect(self.formatar_data)
        self.ui.fun_aniversario.editingFinished.connect(self.validar_data)
        self.ui.fun_cep.textChanged.connect(self.formatar_cep)
        
    # Função que faz o botão de voltar ir pra tela anterior  
    def voltar_para_tela_anterior(self):
        self.parent.show()
        self.close()
        
    # Regra do CPF (Formatação)  
    def formatar_cpf(self, texto):
        fun_cpf = self.sender()
        
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
    
        
        fun_cpf.blockSignals(True)
        fun_cpf.setText(texto_formatado)
        fun_cpf.blockSignals(False)

        fun_cpf.setCursorPosition(len(texto_formatado))
     
    # Regra do CEP (Formatação)      
    def formatar_cep(self, texto):
        fun_cep = self.sender()
        
        # Mantem apenas os números
        texto_limpo = ''.join(filter(str.isdigit, texto))
        
        # Limita a 8 dígitos (tamanho de um CEP)
        texto_limpo = texto_limpo[:8]

        # Adiciona o traço
        if len(texto_limpo) > 5:
            texto_formatado = f"{texto_limpo[:5]}-{texto_limpo[5:]}"
        else:
            texto_formatado = texto_limpo
        
        fun_cep.blockSignals(True)
        fun_cep.setText(texto_formatado)
        fun_cep.blockSignals(False)

        fun_cep.setCursorPosition(len(texto_formatado))
    
    # Regra da Data (Formatação)
    def formatar_data(self, texto):
        data_lineEdit = self.sender()
        texto_limpo = ''.join(filter(str.isdigit, texto))
        texto_limpo = texto_limpo[:8] # Limita a 8 dígitos (ddmmyyyy)

        if len(texto_limpo) > 4:
            texto_formatado = f"{texto_limpo[:2]}/{texto_limpo[2:4]}/{texto_limpo[4:]}"
        elif len(texto_limpo) > 2:
            texto_formatado = f"{texto_limpo[:2]}/{texto_limpo[2:]}"
        else:
            texto_formatado = texto_limpo

        data_lineEdit.blockSignals(True)
        data_lineEdit.setText(texto_formatado)
        data_lineEdit.blockSignals(False)
        data_lineEdit.setCursorPosition(len(texto_formatado))

    # Regra da Data (Validação)
    def validar_data(self):
        data_lineEdit = self.sender()
        texto_data = data_lineEdit.text()

        # Se o campo estiver vazio, não faz nada
        if not texto_data:
            return

        # Verifica se a data tem o formato completo
        if len(texto_data) != 10:
            self.mostrar_mensagem("Erro de Data", "Data incompleta. Use o formato DD/MM/AAAA. ")
            data_lineEdit.clear() 
            return
            
        try:
            data_digitada = datetime.strptime(texto_data, "%d/%m/%Y").date()
            hoje = datetime.now().date()

            # Compara com a data atual
            if data_digitada > hoje:
                self.mostrar_mensagem("Erro de Data", "Data inválida! ")
                data_lineEdit.clear() 
        
        except ValueError:
            # Acontece se a data for inválida, ex: 32/01/2024
            self.mostrar_mensagem("Erro de Data", "Data inválida! ")
            data_lineEdit.clear() 
            
    
    def mostrar_mensagem(self, titulo, mensagem):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(mensagem)
        msg_box.setWindowTitle(titulo)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

