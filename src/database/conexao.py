import mysql.connector

def criar_conexao():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='byteshop'
    )
    return conexao

if __name__ == '__main__':
    try:
        conexao = criar_conexao()
        if conexao.is_connected():
            print("Conexão com MySQL estabelecida com sucesso!")
            conexao.close()
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
