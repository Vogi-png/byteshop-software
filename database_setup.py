import mysql.connector
from mysql.connector import errorcode
import os


DB_CONFIG = {
    'user': 'root',
    'password': 'root', # Coloque a SUA senha do banco de dados.
    'host': 'localhost'
}
DB_NAME = 'byteshop'
DUMP_FOLDER = os.path.join('database', 'Dump20250623 - Copia')

# ---------------------------------------------

def criar_banco_e_tabelas():
    conn = None
    try:
        print("Conectando ao servidor MySQL...")
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        print("Conexão bem-sucedida!")

        print(f"Verificando/Criando o banco de dados '{DB_NAME}'...")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
        cursor.execute(f"USE {DB_NAME}")
        print(f"Banco de dados '{DB_NAME}' pronto e selecionado.")

        # Verifica se já existem tabelas no banco de dados
        cursor.execute("SHOW TABLES")
        tabelas_existentes = cursor.fetchall()

        if tabelas_existentes:
            print("\nO banco de dados já parece estar populado. A importação do dump será ignorada.")
            return 

        # Se não houver tabelas, prossegue com a importação
        print("\nBanco de dados vazio. Iniciando importação do dump...")
        
        print(f"Procurando por arquivos .sql na pasta '{DUMP_FOLDER}'...")
        sql_files = sorted([f for f in os.listdir(DUMP_FOLDER) if f.endswith('.sql')])
        
        if not sql_files:
            print("AVISO: Nenhum arquivo .sql encontrado na pasta de dump.")
            return

        print(f"Encontrados {len(sql_files)} arquivos .sql. Importando...")
        for sql_file in sql_files:
            file_path = os.path.join(DUMP_FOLDER, sql_file)
            print(f"  - Executando {sql_file}...")
            with open(file_path, 'r', encoding='utf-8') as f:
                sql_script = f.read()
                comandos = sql_script.split(';')
                for comando in comandos:
                    if comando.strip():
                        cursor.execute(comando)
        
        print("\nImportação do dump concluída com sucesso!")
        conn.commit()

    except mysql.connector.Error as err:
        print(f"ERRO de MySQL: {err}")
    except FileNotFoundError:
        print(f"ERRO: A pasta de dump '{DUMP_FOLDER}' não foi encontrada.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("Conexão com o MySQL foi fechada.")


if __name__ == '__main__':
    criar_banco_e_tabelas()