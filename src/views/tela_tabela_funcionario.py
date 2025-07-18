# Arquivo: src/views/tela_tabela_funcionario.py
import sys
import locale
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QAbstractItemView, QHeaderView
from ui.ui_tela_tabela_funcionario import Ui_TabelaFuncionario
from database.conexao import criar_conexao
import res_rc


class TabelaFuncionarioWindow(QMainWindow):
    def __init__(self, parent_window):
        super().__init__()
        self.ui = Ui_TabelaFuncionario()
        self.ui.setupUi(self)
        self.ui.funcionario_table.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.SelectedClicked)
        self.parent = parent_window
        
        # --- Configuração da Aparência da Tabela ---
        # Certifique-se que o objectName da sua tabela no Qt Designer é "fun_tabela"
        self.ui.funcionario_table.verticalHeader().setVisible(False)
        self.ui.funcionario_table.horizontalHeader().setStretchLastSection(True)
        self.ui.funcionario_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.funcionario_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        
        # Conexões (use o nome do seu botão, ex: "fun_add_button")
        self.ui.add_button.clicked.connect(self.abrir_tela_cadastro_funcionario)
        self.ui.deletar_button.clicked.connect(self.deletar_funcionarios_selecionados)
        self.ui.buscar_button.clicked.connect(self.buscar_funcionario)
        self.ui.produtos_button.clicked.connect(self.abrir_tela_produto)
        self.ui.barra_pesquisa.returnPressed.connect(self.buscar_funcionario)
        self.ui.editar_button.clicked.connect(self.editar_funcionario_selecionado)
        self.ui.cliente_button.clicked.connect(self.abrir_tela_usuario_adm)# Enter chama buscar_funcionario
        self.carregar_dados_funcionarios()
        # Logout
        self.ui.logout_button.clicked.connect(self.logout)

    def logout(self):
        from main import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()
        
    def abrir_tela_produto(self):
        from views.tela_tabela_produto_adm import TabelaProdutoAdmWindow 
        
        self.janela_produto = TabelaProdutoAdmWindow(parent_window=self)
        self.janela_produto.show()
        self.hide()

    def carregar_dados_funcionarios(self):
        """Busca os funcionários no banco e preenche a tabela."""
        conn = None
        try:
            conn = criar_conexao()
            cursor = conn.cursor()
            sql = "SELECT id, cpf, nome, email, cargo, salario FROM funcionarios ORDER BY nome ASC"
            cursor.execute(sql)
            lista_funcionarios = cursor.fetchall()

            self.ui.funcionario_table.setRowCount(0)
            self.ui.funcionario_table.setColumnCount(6)
            self.ui.funcionario_table.setHorizontalHeaderLabels(['ID', 'CPF', 'Nome', 'Email', 'Cargo', 'Salário'])

            for linha, dados_funcionario in enumerate(lista_funcionarios):
                self.ui.funcionario_table.insertRow(linha)
                id_func, cpf, nome, email, cargo, salario = dados_funcionario
                
                salario_formatado = locale.currency(float(salario), grouping=True) if salario else "N/A"

                self.ui.funcionario_table.setItem(linha, 0, QTableWidgetItem(str(id_func)))
                self.ui.funcionario_table.setItem(linha, 1, QTableWidgetItem(cpf))
                self.ui.funcionario_table.setItem(linha, 2, QTableWidgetItem(nome))
                self.ui.funcionario_table.setItem(linha, 3, QTableWidgetItem(email))
                self.ui.funcionario_table.setItem(linha, 4, QTableWidgetItem(cargo))
                self.ui.funcionario_table.setItem(linha, 5, QTableWidgetItem(salario_formatado))

            self.ui.funcionario_table.setColumnHidden(0, True)

        except Exception as e:
            self.mostrar_mensagem("Erro", f"Não foi possível carregar os funcionários.\nErro: {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()
                
    def deletar_funcionarios_selecionados(self):
        """Deleta todos os funcionários que foram selecionados na tabela."""
        # Pega os itens da tabela correta: 'funcionario_table'
        itens_selecionados = self.ui.funcionario_table.selectedItems()

        if not itens_selecionados:
            # Mensagem correta para funcionário
            self.mostrar_mensagem("Atenção", "Nenhum funcionário selecionado para deletar.")
            return
        
        # Pega os IDs únicos das linhas selecionadas
        ids_para_deletar = set(self.ui.funcionario_table.item(item.row(), 0).text() for item in itens_selecionados)

        # Mensagem de confirmação correta
        titulo = "Confirmar Deleção"
        texto = f"Você tem certeza que deseja deletar {len(ids_para_deletar)} funcionário(s)?\nEsta ação não pode ser desfeita."
        resposta = QMessageBox.question(self, titulo, texto, QMessageBox.Yes | QMessageBox.No)

        if resposta == QMessageBox.Yes:
            conn = None
            try:
                conn = criar_conexao()
                cursor = conn.cursor()
                
                # Comando SQL correto para a tabela 'funcionarios'
                sql = "DELETE FROM funcionarios WHERE id = %s"
                dados_para_deletar = [(int(id_str),) for id_str in ids_para_deletar]
                
                cursor.executemany(sql, dados_para_deletar)
                conn.commit()

                # Mensagem de sucesso correta
                self.mostrar_mensagem("Sucesso", f"{len(ids_para_deletar)} funcionário(s) deletado(s) com sucesso.")
                
                # Atualiza a tabela para refletir a deleção
                self.carregar_dados_funcionarios()

            except Exception as e:
                if conn: conn.rollback()
                self.mostrar_mensagem("Erro", f"Não foi possível deletar os funcionários.\nErro: {e}")
            finally:
                if conn and conn.is_connected(): conn.close()

    def editar_funcionario_selecionado(self):
        itens_selecionados = self.ui.funcionario_table.selectedItems()
        if not itens_selecionados:
            self.mostrar_mensagem("Atenção", "Nenhum funcionário selecionado para editar.")
            return

        row = itens_selecionados[0].row()

        id_func = self.ui.funcionario_table.item(row, 0).text()
        cpf = self.ui.funcionario_table.item(row, 1).text()
        nome = self.ui.funcionario_table.item(row, 2).text()
        email = self.ui.funcionario_table.item(row, 3).text()
        cargo = self.ui.funcionario_table.item(row, 4).text()
        salario_str = self.ui.funcionario_table.item(row, 5).text().replace("R$", "").replace(".", "").replace(",", ".").strip()

        try:
            salario = float(salario_str)
        except ValueError:
            self.mostrar_mensagem("Erro", "Salário inválido.")
            return

        conn = None
        try:
            conn = criar_conexao()
            cursor = conn.cursor()
            sql = "UPDATE funcionarios SET cpf=%s, nome=%s, email=%s, cargo=%s, salario=%s WHERE id=%s"
            valores = (cpf, nome, email, cargo, salario, id_func)
            cursor.execute(sql, valores)
            conn.commit()
            self.mostrar_mensagem("Sucesso", "Funcionário editado com sucesso!")
            self.carregar_dados_funcionarios()
        except Exception as e:
            if conn:
                conn.rollback()
            self.mostrar_mensagem("Erro", f"Não foi possível editar o funcionário.\nErro: {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()


    def abrir_tela_cadastro_funcionario(self):
        from views.tela_funcionario_cadastro_pessoal import CadastroFuncionarioWindow
        self.janela_cadastro = CadastroFuncionarioWindow(parent_window=self)
        self.janela_cadastro.show()
        self.hide() 
        
    def abrir_tela_usuario_adm(self):
        from views.tela_tabela_usuario_adm import TabelaUsuarioAdmWindow
        self.janela_usuario_adm = TabelaUsuarioAdmWindow(parent_window=self)
        self.janela_usuario_adm.show()
        self.hide()
        
    def mostrar_mensagem(self, titulo, mensagem):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(mensagem)
        msg_box.setWindowTitle(titulo)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def buscar_funcionario(self):
        """Busca funcionários pelo nome, CPF, cargo ou email digitado na barra de pesquisa."""
        termo = self.ui.barra_pesquisa.text().strip()
        if not termo:
            self.carregar_dados_funcionarios()
            return
        conn = None
        try:
            conn = criar_conexao()
            cursor = conn.cursor()
            sql = (
                "SELECT id, cpf, nome, email, cargo, salario FROM funcionarios "
                "WHERE nome LIKE %s OR cpf LIKE %s OR cargo LIKE %s OR email LIKE %s ORDER BY nome ASC"
            )
            like_termo = f"%{termo}%"
            cursor.execute(sql, (like_termo, like_termo, like_termo, like_termo))
            lista_funcionarios = cursor.fetchall()
            self.ui.funcionario_table.setRowCount(0)
            self.ui.funcionario_table.setColumnCount(6)
            self.ui.funcionario_table.setHorizontalHeaderLabels(['ID', 'CPF', 'Nome', 'Email', 'Cargo', 'Salário'])
            for linha, dados_funcionario in enumerate(lista_funcionarios):
                self.ui.funcionario_table.insertRow(linha)
                id_func, cpf, nome, email, cargo, salario = dados_funcionario
                salario_formatado = locale.currency(float(salario), grouping=True) if salario else "N/A"
                self.ui.funcionario_table.setItem(linha, 0, QTableWidgetItem(str(id_func)))
                self.ui.funcionario_table.setItem(linha, 1, QTableWidgetItem(cpf))
                self.ui.funcionario_table.setItem(linha, 2, QTableWidgetItem(nome))
                self.ui.funcionario_table.setItem(linha, 3, QTableWidgetItem(email))
                self.ui.funcionario_table.setItem(linha, 4, QTableWidgetItem(cargo))
                self.ui.funcionario_table.setItem(linha, 5, QTableWidgetItem(salario_formatado))
            self.ui.funcionario_table.setColumnHidden(0, True)
        except Exception as e:
            self.mostrar_mensagem("Erro", f"Não foi possível buscar funcionários.\nErro: {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()