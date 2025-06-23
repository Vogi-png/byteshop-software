import sys
import locale 
from PySide6.QtGui import QIntValidator 
from PySide6.QtWidgets import QApplication, QMainWindow
from ui.ui_tela_cadastro_produto import Ui_CadastroProduto
import res_rc


class CadastroProdutoWindow(QMainWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.ui = Ui_CadastroProduto()
        self.ui.setupUi(self)
        
        self.parent = parent_window
        
        try:
            locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
        except locale.Error:
            locale.setlocale(locale.LC_MONETARY, 'Portuguese_Brazil.1252')
        
        # Mantem apenas os números
        self.ui.quantidade_produto.setValidator(QIntValidator())
        self.ui.preco_produto.setValidator(QIntValidator())
        
        # Limite de caracteres no nome e marca
        self.ui.nome_produto.setMaxLength(50)
        self.ui.marca_produto.setMaxLength(50)
        
        # Conexões
        self.ui.voltar_button.clicked.connect(self.voltar_para_tela_anterior)
        self.ui.preco_produto.textChanged.connect(self.formatar_preco)
     
# -----------------------------------------------------------------------------------
    # Função que faz o botão de voltar ir pra tela anterior  
    def voltar_para_tela_anterior(self):
        self.parent.show()
        self.close()
    
    # Regra do preço     
    def formatar_preco(self, texto):
        preco_produto_lineEdit = self.sender()
        texto_limpo = ''.join(filter(str.isdigit, texto))

        if not texto_limpo:
            # Se o campo for apagado, o texto também é limpo sem formatação
            return

        valor_em_centavos = int(texto_limpo)
        valor_real = valor_em_centavos / 100.0
        
        texto_formatado = locale.currency(valor_real, grouping=True)
        
        preco_produto_lineEdit.blockSignals(True)
        preco_produto_lineEdit.setText(texto_formatado)
        preco_produto_lineEdit.blockSignals(False)
        preco_produto_lineEdit.end(False)