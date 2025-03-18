import datetime
from data.conexao import Conexao

class Mensagem:
    def cadastrar_mensagem(usuario, mensagem):
        data_hora = datetime.datetime.today()

        #Cadastrando  as informações no banco de dados
        #criando a conexão
        conexao = Conexao.criar_conexao()
        
        #O cursor será responsável por manipular o banco de dados
        cursor = conexao.cursor(dictionary = True)

        #Criando o SQL que será executado
        sql = """INSERT INTO tb_comentarios
                (nome, data_hora, comentario)
                VALUES
                (%s,%s,%s)"""
        valores = (usuario, data_hora, mensagem)

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
        sql = """SELECT cod_comentario, nome as usuario, 
                comentario as mensagem, data_hora, curtidas 
                FROM tb_comentarios"""
        
        #Executando o comando SQL
        cursor.execute(sql)

        #Recuperando os dados guardando em uma variável
        resultado = cursor.fetchall()

        #Fecho a conexão com o banco
        cursor.close()

        return resultado

    def deletar_mensagem(codigo):
        #criando a conexão
        conexao = Conexao.criar_conexao()
        
        #O cursor será responsável por manipular o banco de dados
        cursor = conexao.cursor(dictionary = True)
        
        #Criando o SQL que será executado
        sql = """DELETE FROM tb_comentarios
                WHERE cod_comentario = %s"""
        valores = (codigo,)
        
        #Executando o comando SQL
        cursor.execute(sql, valores)
        
        #Comitando para gravar as alterações
        conexao.commit()
        
        #Fechando a conexão
        conexao.close()