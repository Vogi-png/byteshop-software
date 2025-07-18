import sys
import locale 
from database.conexao import criar_conexao
from PySide6.QtGui import QIntValidator 
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
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
        self.ui.prod_cadastrar_button.clicked.connect(self.realizar_cadastro)
     
# -----------------------------------------------------------------------------------


    # Dentro da classe CadastroProdutoWindow

    def realizar_cadastro(self):
        # 1. Pega TODOS os dados do formulário
        nome = self.ui.nome_produto.text().strip()
        preco_formatado = self.ui.preco_produto.text()
        estoque = self.ui.quantidade_produto.text().strip()
        marca = self.ui.marca_produto.text().strip()
        # Supondo que você tenha um campo para descrição
        # descricao = self.ui.descricao_produto.toPlainText() 

        # 2. Validação de campos vazios
        if not nome or not preco_formatado or not estoque or not marca:
            self.mostrar_mensagem("Atenção", "Todos os campos são obrigatórios!")
            return

        # 3. PREPARA O PREÇO PARA O BANCO DE DADOS
        try:
            # Remove o "R$", espaços e troca a vírgula por ponto
            preco_limpo = preco_formatado.replace("R$", "").replace(".", "").replace(",", ".").strip()
            preco_final = float(preco_limpo)
            # Converte o estoque para inteiro
            estoque_final = int(estoque)
        except ValueError:
            self.mostrar_mensagem("Erro", "O valor do preço ou do estoque é inválido.")
            return

        # 4. LÓGICA DE INSERÇÃO NO BANCO DE DADOS
        conn = None
        try:
            conn = criar_conexao()
            cursor = conn.cursor()

            # Use os nomes exatos das suas colunas na tabela 'produtos'
            sql = "INSERT INTO produtos (nome, marca, preco, estoque) VALUES (%s, %s, %s, %s)"
            valores = (nome, marca, preco_final, estoque_final)

            cursor.execute(sql, valores)
            conn.commit()

            self.mostrar_mensagem("Sucesso", "Produto cadastrado com sucesso!")
            
            # Atualiza a tabela na tela anterior (se ela existir e tiver o método)
            if self.parent and hasattr(self.parent, 'carregar_dados_produtos'):
                self.parent.carregar_dados_produtos()
            
            # Volta para a tela anterior
            self.parent.show()
            self.close()

        except Exception as e:
            if conn:
                conn.rollback()
            self.mostrar_mensagem("Erro de Banco de Dados", f"Não foi possível cadastrar o produto.\nErro: {e}")
        
        finally:
            if conn and conn.is_connected():
                conn.close()

    # Não se esqueça de ter a função mostrar_mensagem na sua classe também
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