import sys
import locale
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QAbstractItemView, QHeaderView, QInputDialog
from ui.ui_tela_tabela_produto import Ui_TabelaProduto
from database.conexao import criar_conexao
import res_rc


class TabelaProdutoWindow(QMainWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.ui = Ui_TabelaProduto()
        self.ui.setupUi(self)
        self.ui.produto_table.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked)
        self.parent = parent_window
        
        self.ui.produto_table.horizontalHeader().setStretchLastSection(True)
        self.ui.produto_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.ui.produto_table.setColumnHidden(0, True) # Esconde a coluna ID
        
        # Conexões
        self.ui.cliente_button.clicked.connect(self.abrir_tela_cliente)
        self.ui.sobre_button.clicked.connect(self.abrir_tela_sobre)
        self.ui.add_button.clicked.connect(self.abrir_tela_cadastro_produto)
        self.ui.deletar_button.clicked.connect(self.deletar_produtos_selecionados)
        self.ui.barra_pesquisa.returnPressed.connect(self.buscar_produto)
        self.ui.buscar_button.clicked.connect(self.buscar_produto)
        self.ui.editar_button.clicked.connect(self.editar_produto_selecionado)
        
        self.carregar_dados_produtos()
        # Logout
        self.ui.logout_button.clicked.connect(self.logout)

    def logout(self):
        from main import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
        
    def carregar_dados_produtos(self):
        print("Recarregando a tabela de produtos...")
        conn = None
        try:
            try:
                locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
            except locale.Error:
                locale.setlocale(locale.LC_MONETARY, 'Portuguese_Brazil.1252')

            conn = criar_conexao()
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, preco, marca, estoque FROM produtos ORDER BY nome ASC")
            lista_produtos = cursor.fetchall()

            self.ui.produto_table.setRowCount(0) 

            for linha, dados_produto in enumerate(lista_produtos):
                self.ui.produto_table.insertRow(linha)
                id_prod, nome, preco_db, marca, estoque = dados_produto
                preco_formatado = locale.currency(float(preco_db), grouping=True)
                
                self.ui.produto_table.setItem(linha, 0, QTableWidgetItem(str(id_prod)))
                self.ui.produto_table.setItem(linha, 1, QTableWidgetItem(nome))
                self.ui.produto_table.setItem(linha, 2, QTableWidgetItem(preco_formatado))
                self.ui.produto_table.setItem(linha, 3, QTableWidgetItem(marca))
                self.ui.produto_table.setItem(linha, 4, QTableWidgetItem(str(estoque)))
        except Exception as e:
            self.mostrar_mensagem("Erro", f"Não foi possível carregar os produtos.\nErro: {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()

    def deletar_produtos_selecionados(self):
        itens_selecionados = self.ui.produto_table.selectedItems()
        if not itens_selecionados:
            self.mostrar_mensagem("Atenção", "Nenhum produto selecionado para deletar.")
            return
        
        ids_para_deletar = set(self.ui.produto_table.item(item.row(), 0).text() for item in itens_selecionados)

        titulo = "Confirmar Deleção"
        texto = f"Você tem certeza que deseja deletar {len(ids_para_deletar)} produto(s)?\nEsta ação não pode ser desfeita."
        resposta = QMessageBox.question(self, titulo, texto, QMessageBox.Yes | QMessageBox.No)

        if resposta == QMessageBox.Yes:
            conn = None
            try:
                conn = criar_conexao()
                cursor = conn.cursor()
                sql = "DELETE FROM produtos WHERE id = %s"
                dados_para_deletar = [(int(id_str),) for id_str in ids_para_deletar]
                cursor.executemany(sql, dados_para_deletar)
                conn.commit()
                self.mostrar_mensagem("Sucesso", f"{len(ids_para_deletar)} produto(s) deletado(s) com sucesso.")
                self.carregar_dados_produtos()
            except Exception as e:
                if conn: conn.rollback()
                self.mostrar_mensagem("Erro", f"Não foi possível deletar os produtos.\nErro: {e}")
            finally:
                if conn and conn.is_connected(): conn.close()

    def buscar_produto(self):
        """Busca produtos pelo nome, marca ou preço digitado na barra de pesquisa."""
        termo = self.ui.barra_pesquisa.text().strip()
        if not termo:
            self.carregar_dados_produtos()
            return
        conn = None
        try:
            try:
                locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
            except locale.Error:
                locale.setlocale(locale.LC_MONETARY, 'Portuguese_Brazil.1252')

            conn = criar_conexao()
            cursor = conn.cursor()
            sql = (
                "SELECT id, nome, preco, marca, estoque FROM produtos "
                "WHERE nome LIKE %s OR marca LIKE %s OR CAST(preco AS CHAR) LIKE %s ORDER BY nome ASC"
            )
            like_termo = f"%{termo}%"
            cursor.execute(sql, (like_termo, like_termo, like_termo))
            lista_produtos = cursor.fetchall()

            self.ui.produto_table.setRowCount(0)
            for linha, dados_produto in enumerate(lista_produtos):
                self.ui.produto_table.insertRow(linha)
                id_prod, nome, preco_db, marca, estoque = dados_produto
                preco_formatado = locale.currency(float(preco_db), grouping=True)
                self.ui.produto_table.setItem(linha, 0, QTableWidgetItem(str(id_prod)))
                self.ui.produto_table.setItem(linha, 1, QTableWidgetItem(nome))
                self.ui.produto_table.setItem(linha, 2, QTableWidgetItem(preco_formatado))
                self.ui.produto_table.setItem(linha, 3, QTableWidgetItem(marca))
                self.ui.produto_table.setItem(linha, 4, QTableWidgetItem(str(estoque)))
        except Exception as e:
            self.mostrar_mensagem("Erro", f"Não foi possível buscar produtos.\nErro: {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()

    def editar_produto_selecionado(self):
        itens_selecionados = self.ui.produto_table.selectedItems()
        if not itens_selecionados:
            self.mostrar_mensagem("Atenção", "Nenhum produto selecionado para editar.")
            return

        row = itens_selecionados[0].row()

        id_produto = self.ui.produto_table.item(row, 0).text()
        nome = self.ui.produto_table.item(row, 1).text()
        preco_str = self.ui.produto_table.item(row, 2).text().replace("R$", "").replace(".", "").replace(",", ".").strip()
        marca = self.ui.produto_table.item(row, 3).text()
        estoque_str = self.ui.produto_table.item(row, 4).text()

        try:
            preco = float(preco_str)
            estoque = int(estoque_str)
        except ValueError:
            self.mostrar_mensagem("Erro", "Preço ou estoque inválido.")
            return

        conn = None
        try:
            conn = criar_conexao()
            cursor = conn.cursor()
            sql = "UPDATE produtos SET nome=%s, preco=%s, marca=%s, estoque=%s WHERE id=%s"
            valores = (nome, preco, marca, estoque, id_produto)
            cursor.execute(sql, valores)
            conn.commit()
            self.mostrar_mensagem("Sucesso", "Produto editado com sucesso!")
            self.carregar_dados_produtos()
        except Exception as e:
            if conn:
                conn.rollback()
            self.mostrar_mensagem("Erro", f"Não foi possível editar o produto.\nErro: {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()


    # Suas funções de navegação
    def abrir_tela_cliente(self):
        from views.tela_tabela_usuario import TabelaUsuarioWindow
        self.janela_cliente = TabelaUsuarioWindow(parent_window=self)
        self.janela_cliente.show()
        self.hide()
     
    def abrir_tela_sobre(self):
        from views.tela_sobre import SobreWindow
        self.janela_sobre = SobreWindow(parent_window=self)
        self.janela_sobre.show()
        self.hide() 
    
    def abrir_tela_cadastro_produto(self):
        from views.tela_cadastro_produto import CadastroProdutoWindow
        self.janela_cadastro = CadastroProdutoWindow(parent_window=self)
        self.janela_cadastro.show()
        self.hide() 

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