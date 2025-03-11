import datetime
from data.conexao import Conexao

class Mensagem:
    def cadastrar_mensagem(usuario, mensagem):
        data_hora = datetime.datetime.today()

        #Cadastrando  as informações no banco de dados
        #criando a conexão
        conexao = Conexao.criar_conexao()
        
        #O cursor será responsável por manipular o banco de dados
        cursor = conexao.cursor()

        #Criando o SQL que será executado
        sql = """INSERT INTO tbcomentario
                (nome, comentario, data_comentario)
                VALUES
                (%s,%s,%s)"""
        valores = (usuario, mensagem, data_hora)

        #Executando o comando SQL
        cursor.execute(sql,valores)

        #Confirmo a alteração
        conexao.commit()

        #Fecho a conexão com o banco
        cursor.close()
        conexao.close()
    
    def recuperar_mensagens():
        #Criar conexão
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor(dictionary = True)

        #Criando o SQL que será executado
        sql = """SELECT nome as usuario, 
                comentario as mensagem, data_comentario 
                FROM tbcomentario"""
        
        #Executando o comando SQL
        cursor.execute(sql)

        #Recuperando os dados guardando em uma variável
        resultado = cursor.fetchall()

        #Fecho a conexão com o banco
        cursor.close()

        return resultado

