import mysql.connector

class Conexao:
    def criar_conexao():
        #criando a conexão
        conexao = mysql.connector.connect(host = "10.110.142.70", 
                                        port = 3306, 
                                        user = "3ds", 
                                        password = "banana", 
                                        database = "db_feedback")
        return conexao