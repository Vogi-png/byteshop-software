import mysql.connector
from .conexao import criar_conexao

def email_existe(email):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM funcionarios WHERE email = %s"
        cursor.execute(query, (email,))
        existe = cursor.fetchone()[0] > 0
        cursor.close()
        conn.close()
        return existe
    except mysql.connector.Error as erro:
        print(f"Erro ao verificar email: {erro}")
        return False

def redefinir_senha(email, nova_senha):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        query = "UPDATE funcionarios SET senha = %s WHERE email = %s"
        cursor.execute(query, (nova_senha, email))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except mysql.connector.Error as erro:
        print(f"Erro ao redefinir senha: {erro}")
        return False
