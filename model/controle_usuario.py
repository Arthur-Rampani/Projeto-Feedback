import datetime
from data.conexao import Conexao
from hashlib import sha256

class Usuario:  
    def recuperar_usuarios():
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary=True)
        sql = """SELECT login, nome, senha FROM tb_usuarios"""
        cursor.execute(sql)
        resultado = cursor.fetchall()
        cursor.close()
        conexao.close()
    
    def adicionar_usuario(login, nome, senha):
        senha = sha256(senha.encode()).hexdigest()
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary=True)
        sql = """INSERT INTO tb_usuarios (login, nome, senha) VALUES (%s, %s, %s);"""
        valores = (login, nome, senha)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()

    def verificar_usuario(login, senha):
        senha = sha256(senha.encode()).hexdigest()

        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor(dictionary=True)

        sql = """SELECT login, senha FROM tb_usuarios WHERE login = %s AND senha = %s"""

        valores = (login, senha)

        cursor.execute(sql, valores)

        usuario = cursor.fetchone()

        conexao.commit()

        cursor.close()

        conexao.close()

        return usuario is not None  