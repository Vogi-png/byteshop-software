import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QAbstractItemView
from PySide6.QtWidgets import QHeaderView
from database.conexao import criar_conexao
from ui.ui_tela_tabela_usuario_adm import Ui_TabelaUsuarioAdm
import res_rc


class TabelaUsuarioAdmWindow(QMainWindow):
    def __init__(self, parent_window):
        
        super().__init__()
        self.ui = Ui_TabelaUsuarioAdm()
        self.ui.setupUi(self)
        self.parent = parent_window
        
        self.ui.cliente_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.cliente_table.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # Conexões
        self.ui.produtos_button.clicked.connect(self.abrir_tela_produto)
        self.ui.funcionario_button.clicked.connect(self.abrir_tela_funcionario)
        self.ui.logout_button.clicked.connect(self.logout)
        self.ui.add_button.clicked.connect(self.abrir_tela_cadastro_cliente)
        self.ui.deletar_button.clicked.connect(self.deletar_clientes_selecionados)
        self.ui.barra_pesquisa.returnPressed.connect(self.buscar_cliente)
        self.ui.buscar_button.clicked.connect(self.buscar_cliente) 
        self.ui.editar_button.clicked.connect(self.editar_cliente_selecionado) 

        self.carregar_dados_usuarios()
        # Logout
        self.ui.logout_button.clicked.connect(self.logout)

    def logout(self):
        from main import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
        
# -----------------------------------------------------------------------------------

    def carregar_dados_usuarios(self):
        print("Recarregando a tabela de usuários...")
        conn = None
        try:
            conn = criar_conexao()
            cursor = conn.cursor()
            cursor.execute("SELECT ID, CPF, nome, email FROM clientes ORDER BY nome ASC")
            lista_clientes = cursor.fetchall()

            self.ui.cliente_table.setRowCount(0)
            self.ui.cliente_table.setColumnHidden(0, True)
            self.ui.cliente_table.setColumnHidden(4, True)

            
            for linha, cliente_data in enumerate(lista_clientes):
                self.ui.cliente_table.insertRow(linha)
                
                id_cliente, cpf, nome, email = cliente_data
                
                self.ui.cliente_table.setItem(linha, 0, QTableWidgetItem(str(id_cliente)))
                self.ui.cliente_table.setItem(linha, 1, QTableWidgetItem(cpf))
                self.ui.cliente_table.setItem(linha, 2, QTableWidgetItem(nome))
                self.ui.cliente_table.setItem(linha, 3, QTableWidgetItem(email))
        
        except Exception as e:
            self.mostrar_mensagem("Erro", f"Não foi possível carregar os clientes.\nErro: {e}")
        
        finally:
            if conn and conn.is_connected():
                conn.close()
                
    def deletar_clientes_selecionados(self):
        itens_selecionados = self.ui.cliente_table.selectedItems()

        if not itens_selecionados:
            self.mostrar_mensagem("Atenção", "Nenhum cliente selecionado para deletar.")
            return

        
        ids_para_deletar = set()
        for item in itens_selecionados:
            id_cliente = self.ui.cliente_table.item(item.row(), 0).text()
            ids_para_deletar.add(id_cliente)

        # Confirmação pra deletar
        titulo = "Confirmar Deleção"
        texto = f"Você tem certeza que deseja deletar {len(ids_para_deletar)} cliente(s)?\nEsta ação não pode ser desfeita."
        
        resposta = QMessageBox.question(self, titulo, texto, QMessageBox.Yes | QMessageBox.No)

        # Se o usuário clicou em "Sim", executa a deleção
        if resposta == QMessageBox.Yes:
            conn = None
            try:
                conn = criar_conexao()
                cursor = conn.cursor()
                
                sql = "DELETE FROM clientes WHERE ID IN (%s)"
                dados_para_deletar = [(int(id_str),) for id_str in ids_para_deletar]
                cursor.executemany(sql, dados_para_deletar)
                conn.commit()

                self.mostrar_mensagem("Sucesso", f"{len(ids_para_deletar)} cliente(s) deletado(s) com sucesso.")
                
                # ATUALIZA A TABELA para mostrar o resultado
                self.carregar_dados_usuarios()

            except Exception as e:
                if conn:
                    conn.rollback()
                self.mostrar_mensagem("Erro", f"Não foi possível deletar os clientes.\nErro: {e}")
            
            finally:
                if conn and conn.is_connected():
                    conn.close()
    def editar_cliente_selecionado(self):
            itens_selecionados = self.ui.cliente_table.selectedItems()
            if not itens_selecionados:
                self.mostrar_mensagem("Atenção", "Nenhum cliente selecionado para editar.")
                return
            row = itens_selecionados[0].row()
            id_cliente = self.ui.cliente_table.item(row, 0).text()
            cpf = self.ui.cliente_table.item(row, 1).text()
            nome = self.ui.cliente_table.item(row, 2).text()
            email = self.ui.cliente_table.item(row, 3).text()
            # Edita diretamente no banco sem abrir a tela de cadastro e sem pedir senha
            conn = None
            try:
                conn = criar_conexao()
                cursor = conn.cursor()
                sql = "UPDATE clientes SET nome=%s, CPF=%s, email=%s WHERE ID=%s"
                valores = (nome, cpf, email, id_cliente)
                cursor.execute(sql, valores)
                conn.commit()
                self.mostrar_mensagem("Sucesso", "Cliente editado com sucesso!")
                self.carregar_dados_usuarios()
            except Exception as e:
                if conn:
                    conn.rollback()
                self.mostrar_mensagem("Erro", f"Não foi possível editar o cliente.\nErro: {e}")
            finally:
                if conn and conn.is_connected():
                    conn.close()
                    
    def buscar_cliente(self):
        """Busca clientes pelo nome, CPF ou email digitado na barra de pesquisa."""
        termo = self.ui.barra_pesquisa.text().strip()
        if not termo:
            self.carregar_dados_usuarios()
            return
        conn = None
        try:
            conn = criar_conexao()
            cursor = conn.cursor()
            sql = (
                "SELECT ID, CPF, nome, email FROM clientes "
                "WHERE nome LIKE %s OR CPF LIKE %s OR email LIKE %s ORDER BY nome ASC"
            )
            like_termo = f"%{termo}%"
            cursor.execute(sql, (like_termo, like_termo, like_termo))
            lista_clientes = cursor.fetchall()

            self.ui.cliente_table.setRowCount(0)
            self.ui.cliente_table.setColumnHidden(0, True)
            
            for linha, cliente_data in enumerate(lista_clientes):
                self.ui.cliente_table.insertRow(linha)
                id_cliente, cpf, nome, email = cliente_data
                self.ui.cliente_table.setItem(linha, 0, QTableWidgetItem(str(id_cliente)))
                self.ui.cliente_table.setItem(linha, 1, QTableWidgetItem(cpf))
                self.ui.cliente_table.setItem(linha, 2, QTableWidgetItem(nome))
                self.ui.cliente_table.setItem(linha, 3, QTableWidgetItem(email))
        except Exception as e:
            self.mostrar_mensagem("Erro", f"Não foi possível buscar clientes.\nErro: {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()

    def abrir_tela_produto(self):
        from views.tela_tabela_produto_adm import TabelaProdutoAdmWindow 
        
        self.janela_produto = TabelaProdutoAdmWindow(parent_window=self)
        self.janela_produto.show()
        self.hide()
        
    def logout(self):
        from main import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
   
    def abrir_tela_funcionario(self):
        from views.tela_tabela_funcionario import TabelaFuncionarioWindow 
        
        self.janela_produto = TabelaFuncionarioWindow(parent_window=self)
        self.janela_produto.show()
        self.hide()
        
    def abrir_tela_cadastro_cliente(self):
        from views.tela_usuario_cadastro_pessoal import CadastroClienteWindow
        self.janela_cadastro = CadastroClienteWindow(parent_window=self)
        self.janela_cadastro.show()
        self.hide() 
        
    def mostrar_mensagem(self, titulo, mensagem):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(mensagem)
        msg_box.setWindowTitle(titulo)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()