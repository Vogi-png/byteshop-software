import mysql.connector
from .conexao import criar_conexao

def autenticar_usuario(email, senha):
    # Conta ADM fixa
    if email == "adm1@gmail.com" and senha == "12345":
        return {
            'id': 0,
            'email': email,
            'senha': senha,
            'cargo': 'Administrador',
            'nome': 'Administrador Fixo'
        }
    try:
        conn = criar_conexao()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM funcionarios WHERE email = %s AND senha = %s"
        cursor.execute(query, (email, senha))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        return usuario
    except mysql.connector.Error as erro:
        print(f"Erro ao autenticar usuário: {erro}")
        return None
